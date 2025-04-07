import unittest
from blocks import *

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
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
        text = "1. oi"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
        text = "1. oi\n2. segundo oi\n3. terceiro oi"
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)
        text = "oi"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "1. oi\n2. segundo oi\n3. terceiro oi\n não é uma list ordenada de verdade"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "``` oi"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
        text = "- item\n- dois itens\n- tres itens"
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
        text = "- item\n- dois itens\n- tres itens\n mas na verdade não é uma lista"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()