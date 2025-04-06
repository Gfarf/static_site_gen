from htmlnode import LeafNode
from textnode import TextType, TextNode


def text_node_to_html_node(text_node: TextNode):
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

def split_nodes_delimiter(old_nodes, delimiter, text_type):


    new_nodes=[]
    for node in old_nodes:
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
                    new_nodes.append(TextNode(new_text[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(new_text[i], text_type))
        
    return new_nodes
