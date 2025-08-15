# MusicDownloader 🎵

A Python script that automates downloading songs from a YouTube playlist directly to a USB flash drive for your car.

---

## 💡 Motivation

My car's stereo system relies on a USB flash drive for music, as it lacks AUX or Bluetooth capabilities.  
The manual process of updating my music was incredibly tedious:  

1. **Find a song**
2. **Copy its link**
3. **Use a third-party website to download it**
4. **Rename the file**  
5. **Transfer it to the flash drive**  

...and repeat this for every single song.  

This project automates the entire workflow, allowing me to update my car's music library by simply running **one script**.

---

## ✨ Features

- **Playlist Integration**  
  Fetches all video titles from a specified YouTube playlist using the **YouTube Data API**.

- **Duplicate Prevention**  
  Checks against a local log file to download only songs that haven't been downloaded before.

- **Concurrent Downloads**  
  Utilizes **multithreading (10 threads)** to download multiple songs simultaneously.

- **Automatic Transfer**  
  Moves new music files directly to a designated external drive (e.g., your USB flash drive).

---

## ⚙️ How It Works

1. **Fetch Playlist**  
   Connects to the YouTube API and retrieves the titles of all songs in your specified playlist.

2. **Compare & Filter**  
   Reads a local file (`already_downloaded_songs`) containing songs already on your drive.  
   Compares this list with the playlist to determine which songs need downloading.

3. **Download Concurrently**  
   Uses a pool of **10 threads** to download multiple songs in parallel, speeding up the process.

4. **Transfer Files**  
   Moves downloaded MP3 or MP4 files from the local folder to your specified external drive path.

5. **Update Log**  
   Updates `downloaded_songs.txt` with newly added songs to avoid re-downloading them in the future.
