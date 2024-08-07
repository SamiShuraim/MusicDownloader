import multiprocessing as mp
import os

import requests
from dotenv import load_dotenv

from logtime import logtime

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


@logtime
def get_youtube_links() -> list[str]:
    """
    Sends request(s) to YouTube API to get links of all videos in a specific playlist.
    :return: list[str] where each string represents the id of a video in the playlist
    """
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


@logtime
def get_new_songs(all_songs: list[str], old_songs: list[str]) -> tuple[mp.Queue, list]:
    """
    Finds ids that exist in all_songs and not in old_songs. These ids represent the songs that have not been
    downloaded before (new).
    :param all_songs: list[str] where each string is an id of a song in the playlist.
    :param old_songs: list[str] where each string is an id of a song that has been downloaded before.
    :return: list[str] where each string is an id of a new song.
    """
    new_songs_q = mp.Queue()
    new_songs_list = []
    for song in all_songs:
        if song not in old_songs:
            new_songs_q.put(song)
            new_songs_list.append(song)

    return new_songs_q, new_songs_list
