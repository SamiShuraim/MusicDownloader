import time
from queue import Queue

START = time.perf_counter()
MESSAGES = {
    "get_youtube_links": "Fetched YouTube links",
    "read": "Read previously downloaded songs",
    "get_new_songs": "Filtered new songs",
    "download_songs": "Downloaded all new songs",
    "write": "Added new songs to previously downloaded songs list",
    "main": "Program is terminating"
}


def make_log_message(message: str, end: float = -1) -> str:
    end = time.perf_counter() if end == -1 else end
    return "%-6s - %s" % (("%.02f" % (end - START)) + "s", message)


def logtime(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        res = func(*args, **kwargs)
        end = time.perf_counter()
        message = MESSAGES[func_name]
        print(make_log_message(message, end))
        return res

    return wrapper
