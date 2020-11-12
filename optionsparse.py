# fearherbs's option file parser
# removes the file specific arguments for processing files in mkvtoolsnix
# 11-11-2020

import subprocess
import re


def removefilelines():
    # open our options file as read only and get the lines
    with open("options.json", "r") as f:
        lines = f.readlines()

    # delete our problematic file lines lines
    with open("options.json", "w") as f:
        for line in lines:
            # removes all file paths --output and the two lines with ) and ( in them
            # yep there is probably a better way to do this
            if re.match(r".*?[\w:][\w:]\\.*\.[\w:]+.*", line.strip("\n")) is None and line.strip("\n") !=\
                    "  \"--output\"," and line.strip("\n") != "  \")\"," and line.strip("\n") != "  \"(\",":
                f.write(line)


def startmkvtools():
    subprocess.call([r'mkvtoolnix-batch.bat'])


removefilelines()
startmkvtools()
