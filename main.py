from news_retriever import fetch_news_articles
from embedding_engine import add_articles_to_vectorstore
from summarizer import summarize_articles
from user_manager import load_preferences, save_preferences, load_history, save_history

def main():
    preferences = load_preferences()
    print("User preferences:", preferences["topics"])
    
    action = input("Choose action: [1] Fetch & Summarize News, [2] Update Preferences, [3] View Search History, [4] Search News on a Custom Topic]: ")
    
    if action == "1":
        articles = fetch_news_articles(preferences["topics"])
        if not articles:
            print("No articles found for the selected topics.")
            return
        add_articles_to_vectorstore(articles)
        summary_type = input("Choose summary type: [brief/detailed]: ").strip().lower()
        summary = summarize_articles(preferences["topics"], summary_type)
        print("\nNews Summary:\n", summary)
    
    elif action == "2":
        new_topics = input("Enter new topics (comma-separated): ").split(",")
        preferences["topics"] = [t.strip() for t in new_topics]
        save_preferences(preferences)
        print("Preferences updated!")
    
    elif action == "3":
        history = load_history()
        print("\nSearch History:")
        for i, query in enumerate(history, 1):
            print(f"{i}. {query}")
    
    elif action == "4":
        custom_topic = input("Enter a topic to search: ").strip()
        articles = fetch_news_articles([custom_topic])
        if not articles:
            print(f"No articles found for '{custom_topic}'.")
            return
        add_articles_to_vectorstore(articles)
        summary_type = input("Choose summary type: [brief/detailed]: ").strip().lower()
        summary = summarize_articles(custom_topic, summary_type)
        print("\nNews Summary:\n", summary)
    
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()