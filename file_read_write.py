from logtime import logtime


@logtime
def read() -> list[str]:
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
    with open("already_downloaded_songs.txt", "a") as f:
        for i in new_songs:
            f.write(i + "\n")
