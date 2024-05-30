import re
import requests
from datetime import datetime

def count_search_phrases(search_phrase, *texts):
    count = sum(text.lower().count(search_phrase.lower()) for text in texts if text)
    return count


def check_contains_money(*texts):
    for text in texts:
        if re.search(r"\$[\d,.]+|\d+ (?:dollars|USD)", text):
            return "True"
    return "False"


def download_picture(url):
    if url:
        picture_filename = "picture_{:%Y%m%d%H%M%S}.jpg".format(datetime.now())
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            with open(picture_filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            return picture_filename
        except Exception as e:
            print(f"Error downloading picture from {url}: {str(e)}")
            return ""
