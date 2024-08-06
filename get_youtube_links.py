import requests
import dotenv
import os

from dotenv import load_dotenv
# from sample_data_holder import sample_data

load_dotenv()

API_KEY = os.getenv('API_KEY')


def make_request(next_page_token: str = "") -> dict:
    url = "https://content-youtube.googleapis.com/youtube/v3/playlistItems"

    querystring = {"part": "contentDetails", "maxResults": "50", "playlistId": "PLYpiyBB1zUa0N26kLSqLhDqM-trgzMoSc",
                   "key": API_KEY}

    if next_page_token != "":
        querystring["pageToken"] = next_page_token

    payload = ""
    headers = {
        "authority": "content-youtube.googleapis.com",
        "accept": "*/*",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-origin": "https://explorer.apis.google.com",
        "x-referer": "https://explorer.apis.google.com"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    return response.json()


def get_ids(video_data: list[str]) -> list[str]:
    ids = []
    for item in video_data:
        ids.append(item["contentDetails"]["videoId"])

    return ids


def get_youtube_links() -> list[str]:
    # return get_ids(sample_data)
    data = []
    res = make_request()

    data += res["items"]

    next_page_token = res.get("nextPageToken")
    next_page_token_present = next_page_token is not None

    while next_page_token_present:
        res = make_request(next_page_token)

        data += res["items"]

        next_page_token = res.get("nextPageToken")
        next_page_token_present = next_page_token is not None

    return get_ids(data)
