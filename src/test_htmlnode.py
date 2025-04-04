import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_print(self):
        node = HTMLNode("<p>", "texto valor", "texto crianças", {"href": "link de referencia.", "target": "alvo"})
        node2 = HTMLNode(value="texto valor", children="texto crianças",props= {"href": "link de referencia.", "target": "alvo"})
        node3 = HTMLNode("<p>", "texto valor", "texto crianças")
        node4 = HTMLNode("<p>", "texto valor")
        node5 = HTMLNode()
        listnodes = []
        listnodes.append(node)
        listnodes.append(node2)
        listnodes.append(node3)
        listnodes.append(node4)
        listnodes.append(node5)
        for n in listnodes:
            print(n)
            print(n.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        node2 = LeafNode("p", "texto valor", {"href": "link de referencia.", "target": "alvo"})
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        self.assertEqual(node2.to_html(), '<p href="link de referencia." target="alvo">texto valor</p>')

def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])
    self.assertEqual(
        parent_node.to_html(),
        "<div><span><b>grandchild</b></span></div>",
    )  


if __name__ == "__main__":
    unittest.main()