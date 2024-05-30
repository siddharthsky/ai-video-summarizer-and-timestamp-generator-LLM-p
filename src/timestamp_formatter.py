import re

class TimestampFormatter:

    @staticmethod
    def format(gentext):
        pattern= r"(\d{2}:\d{2}:\d{2})\]\((?:https:\/\/youtu\.be\/[A-Za-z0-9_-]+\?t=\d+)\) ([^\n]+)"
        finder = re.findall(pattern,gentext)
        output = []
        for i in finder:
            print(f"{i[0]+' '+i[1]}")
            output.append(f"{i[0]+' '+i[1]} \n")

        cp_text = " ".join(output)
        return cp_text


