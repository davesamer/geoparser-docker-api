from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from mordecai3 import Geoparser
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search


def make_conn():
    """the make_conn function from mordecai 3 needs to be overwritten so that mordecai can connect to elasticsearch"""
    kwargs = dict(
        hosts=['http://elasticsearch_gp'],
        port=9200,
        use_ssl=False,
    )
    CLIENT = Elasticsearch(**kwargs)
    conn = Search(using=CLIENT, index="geonames")
    return conn


app = FastAPI()


class NewsArticle(BaseModel):
    page: str
    title: str
    time: str
    author: str
    content: str


class ProcessedNewsArticles(NewsArticle):
    location_information: List


@app.post('/geoparse/')
async def geoparse(news_article: NewsArticle):

    # Initialize Geoparser
    geo = Geoparser()
    geo.conn = make_conn()

    # initialize processed object with input values
    processed_new_articles = ProcessedNewsArticles(
        **news_article.dict(), location_information=[])

    # geoparse text
    result = geo.geoparse_doc(news_article.content)

    # iterate over identified geo-entities and write to article dict
    for geo_ent in result["geolocated_ents"]:

        geo_ent_dict = {"geonameid": geo_ent["geonameid"],
                        "placename": geo_ent["name"],
                        "longitude": geo_ent["lon"],
                        "latitude": geo_ent["lat"],
                        }
        processed_new_articles.location_information.append(geo_ent_dict)

    return processed_new_articles
