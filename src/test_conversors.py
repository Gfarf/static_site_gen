import unittest
from conversors import text_node_to_html_node
from htmlnode import LeafNode, HTMLNode
from textnode import TextNode, TextType

class conversor_test(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_img(self):
        node = TextNode("texto alternativo", TextType.IMAGE, "www.algum_lugar.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "www.algum_lugar.com")
        self.assertEqual(html_node.props["alt"], "texto alternativo")

if __name__ == "__main__":
    unittest.main()