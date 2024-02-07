class Prompt():
    def __init__():
        pass

    def prompt1(ID=0):
        if ID == 0:
            prompt_text = """As a YouTube video summarizer, 
            your task is to take the provided transcript text and generate a concise summary of the entire video, highlighting key points within 250 words. 
            Please provide an informative and engaging summary of the content, emphasizing important insights and notable aspects discussed in the video. 
            Use the given text as the basis for your summary : """
        
        elif ID == "0t":
            prompt_text = """
            Generate timestamps for the main chapter/topics discussed in a YouTube video transcript.

            Given a list of text segments along with their time. Generate timestamps for the main topics discussed in the video. 
            You should format the timestamps as [hh:mm:ss](%VIDEO_URL?t=seconds).

            Ensure the topics are clear and concise, and aim for 5-7 main topics within the specified video transcript.(mention only topics titles and timestamps)
            give the list of topics with time stamps
            markdown for output 
            "example :  1. [hh:mm:ss](%VIDEO_URL?t=seconds) %TOPIC TITLE 1%
                        2. [hh:mm:ss](%VIDEO_URL?t=seconds) %TOPIC TITLE 2%
                        -and so on" make time clickable

            The %VIDEO_URL% (yotube video link) and transcript are given below.        
            """

        else:
            prompt_text = "NA" 

        return prompt_text
