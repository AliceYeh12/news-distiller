import requests
import random

def get_news(category, query, api_key, para="&q="):
    url = f"http://newsapi.org/v2/top-headlines?category={category}{para}{query}&country=us&apiKey={api_key}"
    print(url)
    response = requests.get(url).json()
    return response

def rand_headlines(api_key, query=""):
    topics = ["entertainment", "sports", "technology"]
    collection = []

    for _ in range(15):
        response = get_news(topics[random.randint(0, 2)], query, api_key, "")
        if len(response["articles"]):
            to_add = response["articles"][random.randint(0, len(response["articles"]) - 1)]
            if to_add not in collection:
                collection.append(to_add)

    return collection

def fetch_results(topics, query, api_key):
    print(topics)
    collection = []

    for topic in topics:
        for article in get_news(topic, query, api_key)["articles"]:
            collection.append(article)

    if not collection:
        collection = get_news("", query, api_key)["articles"]

    return collection
