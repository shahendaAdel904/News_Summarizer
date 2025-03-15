import json
import os

PREFERENCES_FILE = "user_preferences.json"
HISTORY_FILE = "search_history.json"

def load_json_file(filename, default_data):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return json.load(file)
    return default_data

def save_json_file(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def load_preferences():
    return load_json_file(PREFERENCES_FILE, {"topics": ["technology", "AI"]})

def save_preferences(preferences):
    save_json_file(PREFERENCES_FILE, preferences)

def load_history():
    return load_json_file(HISTORY_FILE, [])

def save_history(search_query):
    history = load_history()
    history.append(search_query)
    save_json_file(HISTORY_FILE, history)