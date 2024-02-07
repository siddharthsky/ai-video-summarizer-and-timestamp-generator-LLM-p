from youtube_transcript_api import YouTubeTranscriptApi 
from bs4 import BeautifulSoup
import requests
import re


class GetVideo():
    def __init__(self):
        pass

    def Id(link):
        #video_id = link.split("=")[1]
        if "youtube.com" in link:
            pattern = r'youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'
            video_id = re.search(pattern, link).group(1)
            return video_id
        elif "youtu.be"in link:
            pattern = r"youtu\.be/([a-zA-Z0-9_-]+)"
            video_id = re.search(pattern, link).group(1)
            return video_id
        else:
            video_id = None
            return video_id

        
    def title(link):
        r = requests.get(link) 
        s = BeautifulSoup(r.text, "html.parser") 
        title = s.find("meta", itemprop="name")["content"]
        return title
        
    def transcript(link):
        video_id=GetVideo.Id(link)
        try:
            transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
            final_transcript = ""
            for i in transcript_dict:
                final_transcript += " " + i["text"]
            return final_transcript
        except Exception as e:
            print(e)

    def transcript_time(link):
        video_id=GetVideo.Id(link)
        
        try:
            transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
            final_transcript = ""
            for i in transcript_dict:
                final_transcript += " " + i["text"]
                timevar = round(float(i["start"]))
                hours = int(timevar // 3600)
                timevar %= 3600
                minutes = int(timevar // 60)
                timevar %= 60
                timevex = f"{hours:02d}:{minutes:02d}:{timevar:02d}"
                final_transcript += f' "time:{timevex}"'
            return str(final_transcript)

        except Exception as e:
            print(e)
            return video_id
            