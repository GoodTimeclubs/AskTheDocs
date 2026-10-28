from pathlib import Path

global blocks
global text
text = []
blocks = []
docFolder = Path(__file__).parent / ".." / "data"


def appendBlock(h1,h2,h3):
    global text
    if text:
        blocks.append([h1,h2,h3,text])
        text = []

def blockToText(block):
    if block:
        result = ""
        for headline in block[:3]:
            if headline:
                result += headline + "\n"
        for line in block[3]:
            result += line + "\n"
        return result
    return None

def blocksToChunks():
    chunks = []
    for b in blocks:
        textBlock = blockToText(b)
        if textBlock != None:
            chunks.append(textBlock)

    return chunks
        
def createChunks():
    headline1 = None
    headline2 = None
    headline3 = None

    for file in docFolder.glob("*.md"):
        with open (file.resolve()) as f:
            line = f.readline()
            
            while line:
                if line[:1] != ">" and line[:1] != "\n":
            
                    if line.startswith("### "):
                        appendBlock(headline1,headline2,headline3)
                        headline3 = line[3:].strip()
                        
                    elif line.startswith("## "):
                        appendBlock(headline1,headline2,headline3)
                        headline2 = line[2:].strip()
                        headline3 = None
                        
                    elif line.startswith("# "):
                        appendBlock(headline1,headline2,headline3)
                        headline1 = line[1:].strip()
                        headline2 = None
                        headline3 = None
                        
                    else:
                        text.append(line.strip().lstrip("*- ").replace("**", ""))

                line = f.readline()
            appendBlock(headline1,headline2,headline3)

    return blocksToChunks()
    