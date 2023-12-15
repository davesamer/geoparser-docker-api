from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
# from mordecai import Geoparser
from mordecai_gc import Geoparser
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from colorama import Back


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
    geo = Geoparser(
        es_hosts=['http://elasticsearch_gp'], es_port=9200, es_ssl=False)

    # initialize processed object with input values
    processed_new_articles = ProcessedNewsArticles(
        **news_article.dict(), location_information=[])

    # geoparse text
    result = geo.geoparse(news_article.content)

    # iterate over identified geo-entities and write to article dict
    for geo_ent in result:

        try:
            geo_ent_dict = {"geonameid": geo_ent["geo"]["geonameid"],
                            "placename": geo_ent["geo"]["place_name"],
                            "longitude": float(geo_ent["geo"]["lon"]),
                            "latitude": float(geo_ent["geo"]["lat"]),
                            }
            processed_new_articles.location_information.append(geo_ent_dict)
        except:
            pass

    return processed_new_articles
