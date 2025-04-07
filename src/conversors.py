from htmlnode import LeafNode
from textnode import TextType, TextNode
from blocks import BlockType
import re


def text_to_children(text : str, btype: BlockType) -> list:
    lista_texto = text.split("\n")
    match btype:
        case BlockType.QUOTE:
            text = " ".join(list(map(lambda x: x.lstrip("> "), lista_texto)))
        case BlockType.ULIST:
            text = "<li>" + "<li>".join(list(map(lambda x: x.lstrip("- ")+"</li>", lista_texto)))
        case BlockType.OLIST:
            text = "<li>" + "<li>".join(list(map(lambda x: x.lstrip("1234567890. ")+"</li>", lista_texto)))

    text = " ".join(text.split("\n"))
    nodes = text_to_textnodes(text)
    fnodes = []
    for node in nodes:
        fnodes.append(text_node_to_html_node(node))
    return fnodes

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img","", {"src":text_node.url, "alt":text_node.text})
        case _:
            raise Exception("Text type not compatible")

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: TextType) -> list:


    new_nodes=[]
    for node in old_nodes:
        sub_nodes = []
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            if node.text.find(delimiter) == node.text.rfind(delimiter) and node.text.find(delimiter) != -1:
                raise Exception(f"closing delimiter not found in {node.text} from {node}")
            new_text = node.text.split(delimiter)
            for i in range(len(new_text)):
                if new_text[i] == "":
                    continue
                if i % 2 == 0:
                    sub_nodes.append(TextNode(new_text[i], TextType.TEXT))
                else:
                    sub_nodes.append(TextNode(new_text[i], text_type))
            new_nodes.extend(sub_nodes)
        
    return new_nodes

def extract_markdown_images(text: str) -> list:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    res = []
    for match in matches:
        match = (match[0].rstrip("]").lstrip("!["), match[1].rstrip(")").lstrip("("))
        res.append(match)
    return res

def extract_markdown_links(text: str) -> list:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    res = []
    for match in matches:
        match = (match[0].rstrip("]").lstrip("["), match[1].rstrip(")").lstrip("("))
        res.append(match)
    return res

def split_nodes_image(old_nodes : list) -> list:
    res = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            res.append(node)
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            res.append(node)
            continue
        new_text = node.text
        sub_res = []
        for i in range(len(images)):
            start, mid = text_special_parser(new_text)("![")("]")
            _, end = text_special_parser(new_text[mid:])("(")(")")
            if start == 0:
                sub_res.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                if mid + end == len(new_text):
                    new_text = ""
                    continue
                new_text = new_text[mid+end:]
            else:
                sub_res.append(TextNode(new_text[:start], TextType.TEXT))
                sub_res.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
                if mid + end == len(new_text):
                    new_text = ""
                    continue
                new_text = new_text[mid+end:]
        if len(new_text) > 0:
            sub_res.append(TextNode(new_text,TextType.TEXT))
        res.extend(sub_res)
    return res
            
        

def split_nodes_link(old_nodes : list) -> list:
    res = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            res.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            res.append(node)
            continue
        new_text = node.text
        sub_res = []
        for i in range(len(links)):
            start, mid = text_special_parser(new_text)("[")("]")
            _, end = text_special_parser(new_text[mid:])("(")(")")
            if start == 0:
                sub_res.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
                if mid + end == len(new_text):
                    new_text = ""
                    continue
                new_text = new_text[mid+end:]
            else:
                sub_res.append(TextNode(new_text[:start], TextType.TEXT))
                sub_res.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
                if mid + end == len(new_text):
                    new_text = ""
                    continue
                new_text = new_text[mid+end:]
        if len(new_text) > 0:
            sub_res.append(TextNode(new_text,TextType.TEXT))
        res.extend(sub_res)
    return res

def text_special_parser(text : str) -> list:
    def inner_parser_start(delimiter_start :str):
        def inner_parser_end(delimiter_end :str):
            start = len(text.split(delimiter_start, maxsplit=1)[0])
            end = len(text) - len(text[start:].split(delimiter_end,maxsplit=1)[1])
            return [start, end]
        return inner_parser_end
    return inner_parser_start

def text_to_textnodes(text: str) -> list:
    node = TextNode(text, TextType.TEXT)
    l_nodes = split_nodes_delimiter(
        split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_link(
                    split_nodes_image([node])
                ), "`", TextType.CODE
            ), "**", TextType.BOLD
        ),  "_", TextType.ITALIC
    )

    return l_nodes
