import os
from newsapi import NewsApiClient
from user_manager import save_history

# Load API key
NEWS_API_KEY = "your_newsapi_key_here"
newsapi = NewsApiClient(api_key=NEWS_API_KEY)

def fetch_news_articles(topics):
    all_articles = []
    for topic in topics:
        if not isinstance(topic, str):  
            topic = str(topic)  # Ensure it's a string
        
        articles = newsapi.get_everything(q=topic, language='en', sort_by='publishedAt', page_size=5)
        if "articles" in articles:
            article_contents = [article["content"] for article in articles["articles"] if article["content"]]
            all_articles.extend(article_contents)
        
        save_history(topic)  # Save search history
    return all_articles