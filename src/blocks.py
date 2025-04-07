from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered list"
    OLIST = "ordered list"

def block_to_block_type(markdown : str) -> BlockType:
    if len(markdown) == 0:
        raise ValueError("no markdown text given")
    res = None
    match(markdown[0]):
        case "#":
            check = False
            for i in range(min(7,len(markdown))):
                if markdown[i] == "#":
                    continue
                elif markdown[i] ==" ":
                    check = True
                elif check == False:
                    break
            if check == True:
                res = BlockType.HEADING

        case "`":
            if markdown[:3] == "```" and markdown[-3:] == "```":
                res = BlockType.CODE
        case ">":
            quotes = markdown.split("\n")
            test = True
            for line in quotes:
                if line[0] == ">":
                    continue
                else:
                    test = False
            if test == True:
                res = BlockType.QUOTE
        case "-":
            unorder = markdown.split("\n")
            test = True
            for line in unorder:
                if line[:2] == "- ":
                    continue
                else:
                    test = False
            if test == True:
                res = BlockType.ULIST
        case "1":
            order = markdown.split("\n")
            count = 1
            test = True
            for line in order:
                if line[:3] == f"{count}. ":
                    count += 1
                    continue
                else:
                    test = False
                    break
            if test == True:
                res = BlockType.OLIST

        case _:
            res = BlockType.PARAGRAPH
    if res == None:
        res = BlockType.PARAGRAPH

    return res

def markdown_to_blocks(markdown :str) -> list:
    ilist = markdown.split("\n\n")
#    ilist = list(map(lambda x: x.strip(), ilist))
#    itext = "\n".join(ilist).lstrip("\n")+"\n"
#    mlist = itext.split("\n\n")
    flist=[]
    for item in ilist:
        if item == "":
            continue
        else: 
            item = "\n".join(map(lambda x: x.strip(), item.split("\n"))).strip("\n")
            if item == "":
                continue
            flist.append(item)
    return flist