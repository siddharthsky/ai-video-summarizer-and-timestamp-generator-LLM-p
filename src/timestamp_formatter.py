import strip_markdown

class TimestampFormatter:

    @staticmethod
    def format(gentext):
        cp_text: str = strip_markdown.strip_markdown(gentext)
        return cp_text
