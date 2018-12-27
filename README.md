# Filewatcher

Backend service for watching files on server written in Flask. It will watch a particular folder specified by the WATCH_FOLDER variable. This is specified in the config.py file (or you can override it using environment variable). Once new files are detected, it will send the new file name to the frontend for retrieval using SSE. 

