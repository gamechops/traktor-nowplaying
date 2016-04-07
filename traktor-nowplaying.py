import requests, threading, logging, sys, time

### 
# START CONFIG

icecastServerURL = "http://localhost:8000"

# END CONFIG
###

logging.basicConfig(filename='nowPlaying.log', level=logging.ERROR)

def exception_handler(exctype, value, tb):
        logging.error("Error occurred at: " + time.strftime("%c"))
        logging.error("Type: ", exctype)
        logging.error("Value: ", value)
        logging.error("Traceback: ", tb)

sys.excepthook = exception_handler

icecastStatusURL = icecastServerURL + "/status-json.xsl"

def getTrackInfo():
        trackInfo = requests.get(icecastStatusURL)
        try:
                artistInfo = unicode(trackInfo.json()['icestats']['source']['artist'])
                if artistInfo == "None":
                        artistInfo = "..."
        except:
                artistInfo = "..."
        try:
                titleRaw = trackInfo.json()['icestats']['source']['title']
                if ('A - ' in titleRaw) or ('B - ' in titleRaw):
                        titleArray = titleRaw.split(" - ")
                        titleArray.pop()
                        titleArray.pop()
                        if len(titleArray) > 1:
                                titleProcessed = ' - '.join(titleArray)
                        else:
                                titleProcessed = titleArray[0]
                else:
                        titleProcessed = titleRaw

                titleInfo = unicode(titleProcessed)
        except:
                titleInfo = "..."
        artistFile = open("trackArtist.txt", "w")
        titleFile = open("trackTitle.txt", "w")
        # outfile.write(artistInfo + " - " + titleInfo)
        artistFile.write(artistInfo.encode('utf-8') + "\n")
        print(artistInfo)
        titleFile.write(titleInfo.encode('utf-8') + "\n")
        print(titleInfo)
        threading.Timer(1, getTrackInfo).start()

getTrackInfo()
