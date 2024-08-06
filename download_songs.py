import concurrent.futures
from subprocess import run
from logtime import logtime

NUM_OF_THREADS = 10


def download_song(new_songs_q):
    try:
        song_title = new_songs_q.get(block=False)
        res = run(['yt-dlp', '-o %(title)s.mp3', song_title], capture_output=True)
        print(res.stdout)

        if (not new_songs_q.empty()):
            download_song(new_songs_q)
    except Exception as e:
        print(e)
        return

@logtime
def download_songs(new_songs_q):
    # Start multiple threads to download songs
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=NUM_OF_THREADS)

    for i in range(NUM_OF_THREADS):
        pool.submit(download_song, new_songs_q)

    pool.shutdown(wait=True)