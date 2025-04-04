import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is the text node", TextType.BOLD)
        node2 = TextNode("This is the text node", TextType.ITALIC)
        node3 = TextNode("This is the text node", TextType.IMAGE)
        node4 = TextNode("This is the text node", TextType.BOLD, "link de teste")
        node5 = TextNode("This is the text node com outro texto", TextType.BOLD)
        node6 = TextNode("This is the text node", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)
        self.assertNotEqual(node, node6)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        node3 = TextNode("This is a text node", TextType.BOLD, "tem uma url")
        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)     


if __name__ == "__main__":
    unittest.main()