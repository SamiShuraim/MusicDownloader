from logtime import logtime


@logtime
def read() -> list[str]:
    """
    Reads lines from "already_downloaded_songs.txt" file that represent ids of already downloaded songs.
    :return: list[str] where each string is an id of an already downloaded song.
    """
    try:
        res = []
        with open("already_downloaded_songs.txt", "r") as f:
            for i in f.readlines():
                res.append(i.strip())

            return res
    except FileNotFoundError:
        open("already_downloaded_songs.txt", "x").close()
        return []


@logtime
def write(new_songs: list[str]) -> None:
    """
    writes lines to "already_downloaded_songs.txt". Used to save the ids of new songs that were just downloaded.
    :param new_songs: list[str] where each string is an id of a new song that was just downloaded.
    :return: None.
    """
    with open("already_downloaded_songs.txt", "a") as f:
        for i in new_songs:
            f.write(i + "\n")
