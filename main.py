from get_songs import get_youtube_links, get_new_songs
from file_read_write import read, write
from download_songs import download_songs
from subprocess import run
from logtime import logtime




if __name__ == '__main__':
    # Get all songs from YouTube API
    all_songs = get_youtube_links()

    # Read old songs from file
    prev_downloaded_songs = read()

    # Compare between new and old links
    new_songs_q, new_songs_list = get_new_songs(all_songs, prev_downloaded_songs)

    if new_songs_q.empty():
        print('No new songs')
        quit(0)

    # Download all new songs
    download_songs(new_songs_q)

    # Add newly downloaded songs to already downloaded songs list
    write(new_songs_list)

    # Move songs to correct folder
    run(["mv", "*.mp3", "/d/Music/"])

    # Remove unwanted video formats
    run(["rm", "*.mp4", "*.m4a", ".webm"])
