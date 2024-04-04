### 🔞This application is primarly used for adult purposes. 🔞

# Red-Grabber

A simple Python CLI application to download videos from *certain* tube websites in bulk using bookmarks in Firefox.

## Description

This project started as a simple way for me to download and hoard video files from adult tube sites.

The application will attempt to download a video file using links supplied via Firefox Bookmarks exported into JSON.


## Getting Started

### Dependencies

* Python 3
* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* Firefox Web Browser[^1]

 [^1]: *Confirmed to work with Firefox, may work with other browsers if JSON is the same?*

### Installing

* Place program folder wherever suits your fancy.
* Update the contents of the `testconfig.py` file.
* Rename `testconfig.py` to `config.py`.

### Using Red-Grabber

* Create a new folder in your Firefox bookmarks. 
* Add any links from supported tube sites to the new folder.
* Backup your bookmarks as JSON file using the name and location in `config.py`.
* Navigate to the directory containing Red-Grabber and run the following command:
```
python3 getlinks.py
```
* After script has been run, remember to remove the bookmarks that were previously downloaded.

## Help

