import time
from queue import Queue

START = time.perf_counter()
MESSAGES = [
    "Fetched YouTube links",
    "Read previously downloaded songs",
    "Filtered new songs",
    "Downloaded all new songs",
    "Added new songs to previously downloaded songs list",
    "Moved all new songs to flash drive",
    "Program is terminating"
]
MESSAGES_Q = Queue()
for i in range(len(MESSAGES)): MESSAGES_Q.put(MESSAGES[i])


def make_log_message(message: str, end: float = -1) -> str:
    end = time.perf_counter() if end == -1 else end
    return "%-6s - %s" % (("%.02f" % (end - START)) + "s", message)


def logtime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        end = time.perf_counter()
        message = MESSAGES_Q.get()
        print(make_log_message(message, end))
        return res

    return wrapper
