# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from get_youtube_links import get_youtube_links
from file_read_write import read, write
import multiprocessing as mp
import concurrent.futures
from subprocess import run

NUM_OF_THREADS = 10

def get_new_songs(all, old):
    new_songs_q = mp.Queue()
    new_songs_list = []
    for song in all:
        if (song not in old):
            new_songs_q.put(song)
            new_songs_list.append(song)

    return new_songs_q, new_songs_list

def download_song():
    try:
        song_title = new_songs_q.get(block=False)
        res = run(['yt-dlp', '-o %(title)s.mp3', song_title], capture_output=True)
        print(res.stdout)

        if (not new_songs_q.empty()):
            download_song()
    except:
        return




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get all songs from YouTube API
    all_songs = get_youtube_links()

    # Read old songs from file
    prev_downloaded_songs = read()

    # Compare between new and old links
    global new_songs_q
    new_songs_q, new_songs_list = get_new_songs(all_songs, prev_downloaded_songs)

    if new_songs_q.empty():
        print('No new songs')
        quit(0)

    # Start multiple threads to download songs
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=NUM_OF_THREADS)

    for i in range(NUM_OF_THREADS):
        pool.submit(download_song)

    pool.shutdown(wait=True)

    # Add newly downloaded songs to already downloaded songs list
    write(new_songs_list)

    # Move songs to correct folder
    run(["mv", "*.mp3", "/d/Music/"])

    # Remove unwanted video formats
    run(["rm", "*.mp4", "*.m4a"])
