import requests
from datetime import datetime
import re



def count_search_phrases(search_phrase, *texts):
    """
    Count occurrences of a search phrase in multiple text inputs.
    
    Args:
        search_phrase (str): The phrase to search for.
        texts (str): Variable number of text inputs to search within.
    
    Returns:
        int: The count of occurrences of the search phrase in the text inputs.
    """
    count = sum(text.lower().count(search_phrase.lower()) for text in texts if text)
    return count



def check_contains_money(*texts):
    """
    Check if any of the text inputs contain monetary values.

    Args:
        texts (str): Variable number of text inputs to check.

    Returns:
        str: "True" if any text contains monetary values, otherwise "False".
    """
    for text in texts:
        """Use regular expression to search for patterns"""
        if re.search(r"\$[\d,.]+|\d+ (?:dollars|USD)", text):
            return "True"
    return "False"



def download_picture(url):
    """
    Download a picture from a given URL and save it with a timestamped filename.

    Args:
        url (str): The URL of the picture to download.

    Returns:
        str: The filename of the downloaded picture or an empty string if there was an error.
    """
    if url:
        # Generate a filename for the picture based on the current date and time
        picture_filename = "picture_{:%Y%m%d%H%M%S}.jpg".format(datetime.now())
        try:
            # Send a GET request to the URL to download the picture
            response = requests.get(url, stream=True)
            # Raise an exception if the request was unsuccessful
            response.raise_for_status()
            # Open a file in write-binary mode to save the picture
            with open(picture_filename, "wb") as file:
                # Write the picture data to the file in chunks of 1024 bytes
                for chunk in response.iter_content(chunk_size=1024):
                    # Only write non-empty chunks
                    if chunk:
                        file.write(chunk)
            return picture_filename
        except Exception as e:
            # Print an error message if there was a problem downloading the picture
            print(f"Error downloading picture from {url}: {str(e)}")
            return ""
