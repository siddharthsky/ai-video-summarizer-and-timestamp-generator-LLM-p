
from youtube_transcript_api import YouTubeTranscriptApi 
import pafy
class GetVideo():

    def __init__(self):
        pass

    def get_title(link):
        print(2)
        pass
       

    def get_transcript(link):
        video_id = link.split("=")[1]
        transcript_dict=YouTubeTranscriptApi.get_transcript(video_id)
        final_transcript = ""
        for i in transcript_dict:
            final_transcript += " " + i["text"]
        return final_transcript




s1 = GetVideo.get_title("de")

