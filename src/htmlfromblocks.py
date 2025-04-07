from htmlnode import *
from blocks import *
from textnode import *
from conversors import *

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocktype_tag = {
            BlockType.CODE : "code",
            BlockType.QUOTE : "blockquote",
            BlockType.OLIST : "ol",
            BlockType.ULIST : "ul",
            BlockType.PARAGRAPH : "p"
        }
    mark_clean = markdown_to_blocks(markdown)
    hnode = ParentNode("div", [])
    for mark in mark_clean:
        btype = block_to_block_type(mark)
        if btype == BlockType.CODE:
        #criar um textnode de código e mandar direto para htmlnode de texto
            lnode = text_node_to_html_node(TextNode(mark.strip("`"), TextType.CODE))
            pnode = ParentNode("pre",[lnode])
            hnode.children.append(pnode)
        elif btype == BlockType.HEADING:
        #passar o texto por um separador e retornar um htmlnode com os filhos sendo os nós desse separador nos headings 
            tag = ""
            if mark[1] == " ":
                tag = "h1"
            elif mark[2] == " ":
                tag = "h2"
            elif mark[3] == " ":
                tag = "h3"
            elif mark[4] == " ":
                tag = "h4"
            elif mark[5] == " ":
                tag = "h5"
            elif mark[6] == " ":
                tag = "h6"
            pnode = ParentNode(tag, text_to_children(mark.lstrip("# "),btype))
            hnode.children.append(pnode)
        else:
        #passar o texto por um separador e retornar um htmlnode com os filhos sendo os nós desse separador
            pnode = ParentNode(blocktype_tag[btype], text_to_children(mark,btype))
            hnode.children.append(pnode)

    return hnode