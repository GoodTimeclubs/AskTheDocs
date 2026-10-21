global blocks
global text
headline1 = None
headline2 = None
headline3 = None
text = []
blocks = []
chunks = []


def appendBlock(h1,h2,h3):
    global text
    if text:
        blocks.append([h1,h2,h3,text])
        text = []

def blockToText(block):
    result = ""
    for headline in block[:3]:
        if headline:
            result += headline + "\n"
    for line in block[3]:
        result += line + "\n"
    return result
        


with open ("data/01-firmenprofil.md") as f:
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



for b in blocks:
    chunks.append(blockToText(b))

for c in chunks:
    print(c)
    