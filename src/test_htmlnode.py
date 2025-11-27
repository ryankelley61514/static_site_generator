import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        expected = "HTMLNode(\ntag: a\nvalue: Boot.dev\nchildren: None\nprops: {'href': 'https://boot.dev', 'target': '_blank'}\n)"
        self.assertEqual(node.__repr__(), expected)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        expected = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_to_html(self):
        node = HTMLNode("a", "Boot.dev", None, {"href": "https://boot.dev", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Boot.dev", {"href": "https://boot.dev", "target": "_blank"})
        expected = '<a href="https://boot.dev" target="_blank">Boot.dev</a>'
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()