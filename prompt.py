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
            prompt_text = """Generate timestamps for the main topics discussed in the YouTube video transcript [ONLY THE MAIN TOPICS WHICH ARE DISCUSSED PROMINENTLY]. 
            The transcript is provided in the following format: [{'text': 'sponsored by T', 'start': 0.68, 'duration': 3.24}], where 'text' represents the dialog text, 'start' indicates the time in milliseconds from the video start, and 'duration' specifies how long the subtitle was displayed on screen. Please provide the output in seconds and label each topic with a timestamp in the format '00:01:15 EXAMPLE' representing the time when the topic is discussed in the video."""

        else:
            prompt_text = "NA" 

        return prompt_text
