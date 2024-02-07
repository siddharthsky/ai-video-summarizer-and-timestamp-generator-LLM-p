class Prompt():
    def __init__():
        pass

    def prompt1(ID=0):
        if ID == 0:
            prompt_text = """Your job as an AI video summarizer is to create a short summary of the given video transcript. You need to condense the information into 250 words or less and focus on the important points. Make sure your summary is interesting and informative, highlighting the key insights and notable aspects discussed in the video. Use the provided text as the basis for your summary, and aim to engage the audience by presenting the information in a clear and easy-to-understand way.
            Use the given text as the basis for your summary : """
        
        elif ID == "transcript":
            prompt_text = """
            Generate timestamps for main chapter/topics in a YouTube video transcript.
            Given text segments with their time, generate timestamps for main topics discussed in the video. Format timestamps as hh:mm:ss and provide clear and concise topic titles.  
           
            Instructions:
            1. List only topic titles and timestamps.
            2. Do not explain the titles.
            3. Include clickable URLs.
            4. Provide output in Markdown format.

            Markdown for output:
            1. [hh:mm:ss](%VIDEO_URL?t=seconds) %TOPIC TITLE 1%
            2. [hh:mm:ss](%VIDEO_URL?t=seconds) %TOPIC TITLE 2%
            - and so on

            Markdown Example:
            1. [00:05:23](https://youtu.be/hCaXor?t=323) Introduction
            2. [00:10:45](https://youtu.be/hCaXor?t=645) Main Topic 1
            3. [00:25:17](https://youtu.be/hCaXor?t=1517) Main Topic 2
            - and so on

            The %VIDEO_URL% (YouTube video link) and transcript are provided below :
            """

        else:
            prompt_text = "NA" 

        return prompt_text
