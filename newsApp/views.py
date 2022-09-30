from unicodedata import category
from django.shortcuts import render
from newsapi import NewsApiClient
import re
from datetime import datetime

# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='ba2614da832e40dd9d395e1d1c77c995')
    headLines = newsApi.get_everything(sources='national-geographic,the-verge,techcrunch,techradar,fortune,new-scientist,next-big-future')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    time =[]
    url=[]


    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        img.append(article['urlToImage'])
        test_str=article['publishedAt']
        match_str = re.search(r'\d{4}-\d{2}-\d{2}', test_str)
        time.append(str(datetime.strptime(match_str.group(), '%Y-%m-%d').date()))
        url.append(article['url'])
    mylist = zip(news, desc, img, time,url)

    return render(request, "index.html", context={"mylist": mylist})
