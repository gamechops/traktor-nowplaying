# traktor-nowplaying
Python2 script that works with Icecast2 to provide artist and track information to be ingested by video streaming or visualization packages.

## Requirements
* python 2 and dependant modules:  requests, logging, (all dependencies can be installed / updated via pip)
* icecast2 (can be acquired from http://icecast.org/ or your OS'es source control)

## Configuration Instructions
* Install a local Icecast2 server.  Consult Icecast's documentation if you have difficulties here. 
* Edit the traktor-nowplaying.ini file.  A default Icecast2 install should use the pre-filled address and port number, but you should double check to make sure it conforms with how you have Icecast configured. 
* Configure Traktor to stream to the Icecast2 server.  Any bitrate and format is fine, but a low bitrate may save on CPU usage.  

## How to use
Start your Icecast2 server and Traktor, then run the traktor-nowplaying.py script.  

## Notes
Traktor by default updates the track information  after a song has been playing for 8-10 seconds on a deck.  This includes cueing tracks. This can be adjusted from within Traktor.

Current version of the script does attempt to strip BPM and key information generated by Mixed In Key, but falls back if it doesn't conform with a specific format.  If you do not used Mixed In Key, you do not need to worry. 

## Issues and Pull Requests
Please submit issues via Github if the script does not work.  Pull requests to expand/fix issues are welcome.

