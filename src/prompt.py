class Prompt:
    @staticmethod
    def prompt1(ID=0):
        if ID == 0:
            prompt_text = """Your task: Condense a video transcript into a captivating and informative 250-word summary that highlights key points and engages viewers.

Guidelines:
    Focus on essential information: Prioritize the video's core messages, condensing them into point-wise sections.
    Maintain clarity and conciseness: Craft your summary using accessible language, ensuring it's easily understood by a broad audience.
    Capture the essence of the video: Go beyond mere listings. Integrate key insights and interesting aspects to create a narrative that draws readers in.
    Word count: Aim for a maximum of 250 words.

Input:
    The provided video transcript will be your content source.

Example (for illustration purposes only):
    Setting the Stage: Briefly introduce the video's topic and context.
    Key Points:
        Point A: Describe the first crucial aspect with clarity and depth.
        Point B: Elaborate on a second significant point.
        (Continue listing and describing key points)
    Conclusions: Summarize the video's main takeaways, leaving readers with a clear understanding and potential interest in learning more.

Additional Tips:
    Tailor the tone: Adjust your language to resonate with the video's intended audience and overall style.
    Weave in storytelling elements: Employ vivid descriptions and engaging transitions to make the summary more memorable.
    Proofread carefully: Ensure your final summary is free of grammatical errors and typos.

By following these guidelines, you can effectively transform video transcripts into captivating and informative summaries, drawing in readers and conveying the video's essence effectively."""

        elif ID == "timestamp":
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
            
        elif ID == "transcript":
            prompt_text = """
            """

        else:
            prompt_text = "NA" 

        return prompt_text
