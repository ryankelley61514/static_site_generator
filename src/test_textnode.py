import unittest

from textnode import TextNode, TextType
from functions import text_node_to_html_node, split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is text", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_type_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.to_html(), "<b>This is a bold text node</b>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.to_html(), '<a href="https://boot.dev">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.to_html(), '<img src="https://boot.dev" alt="This is an image node">')

    def test_bold_split(self):
        node = TextNode("This is a text node with **bold Markdown**", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "**", TextType.BOLD),
            [
                TextNode("This is a text node with ", TextType.TEXT),
                TextNode("bold Markdown", TextType.BOLD)
            ]
        )

    def test_italic_split(self):
        node = TextNode("This is a text node with _italic_ Markdown", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "_", TextType.ITALIC),
            [
                TextNode("This is a text node with ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" Markdown", TextType.TEXT)
            ]
        )

    def test_multiple_code_split(self):
        node = TextNode("This is a `text node` with `multiple code` blocks", TextType.TEXT)
        self.assertEqual(
            split_nodes_delimiter([node], "`", TextType.CODE),
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("text node", TextType.CODE),
                TextNode(" with ", TextType.TEXT),
                TextNode("multiple code", TextType.CODE),
                TextNode(" blocks", TextType.TEXT)
            ]
        )

    def test_non_text_split(self):
        node = TextNode("This is a text node with bold Markdown", TextType.BOLD)
        with self.assertRaises(Exception):
            split_nodes_delimiter(node)

if __name__ == "__main__":
    unittest.main()