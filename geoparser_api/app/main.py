from fastapi import FastAPI
from pydantic import BaseModel
import requests
import json
import logging

app = FastAPI()


class NewsArticle(BaseModel):
    page: str
    title: str
    time: str
    author: str
    content: str


@app.post('/geoparser_api/mordecai2/')
def geoparse_mordecai2(news_article: NewsArticle):

    url = 'http://mordecai2:8080/geoparse/'
    response = requests.post(url, json=news_article.dict())
    return response.json()


@app.post('/geoparser_api/mordecai3/')
def geoparse_mordecai3(news_article: NewsArticle):
    
    url = 'http://mordecai3:8080/geoparse/'
    response = requests.post(url, json=news_article.dict())
    return response.json()


    


    