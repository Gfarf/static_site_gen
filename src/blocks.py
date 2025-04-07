from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

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
                res = BlockType.UNORDERED_LIST
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
                res = BlockType.ORDERED_LIST

        case _:
            res = BlockType.PARAGRAPH
    if res == None:
        res = BlockType.PARAGRAPH

    return res