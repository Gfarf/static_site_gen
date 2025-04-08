import unittest
from blocks import *
from htmlfromblocks import *

class test_blocks_to_blocktype(unittest.TestCase):
    def test1(self):
        text = "# oi"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        text = "#### oi"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        text = "###### oi"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
        text = "####### oi"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "``` oi ```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
        text = "> oi"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
        text = "- oi"
        self.assertEqual(block_to_block_type(text), BlockType.ULIST)
        text = "1. oi"
        self.assertEqual(block_to_block_type(text), BlockType.OLIST)
        text = "1. oi\n2. segundo oi\n3. terceiro oi"
        self.assertEqual(block_to_block_type(text), BlockType.OLIST)
        text = "oi"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "1. oi\n2. segundo oi\n3. terceiro oi\n não é uma list ordenada de verdade"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "``` oi"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "- item\n- dois itens\n- tres itens"
        self.assertEqual(block_to_block_type(text), BlockType.ULIST)
        text = "- item\n- dois itens\n- tres itens\n mas na verdade não é uma lista"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
    This is **bolded** paragraph




    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    def test_paragraphs(self):
        md = """
            This is **bolded** paragraph
            text in a p
            tag here

            This is another paragraph with _italic_ text and `code` here

            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_headings(self):
        md = """
        # this is an h1

        this is paragraph text

        ## this is an h2
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
        > This is a
        > blockquote block

        this is paragraph text

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )
            

    def test_ext_title1(self):
        md = """
> This is a
> blockquote block

# this is paragraph text

        """
        title, md_fim = extract_title(md)
        self.assertEqual(
                title,
                "this is paragraph text",
            )
        self.assertEqual(
                md_fim,
                """
> This is a
> blockquote block


        """,
            )
    

if __name__ == "__main__":
    unittest.main()