import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("a", "hello world", None, {"href": "https://boot.dev", "target": "_blank"})
        expected = "HTMLNode(\ntag: a\nvalue: hello world\nchildren: None\nprops: {'href': 'https://boot.dev', 'target': '_blank'}\n)"
        self.assertEqual(node.__repr__(), expected)
    
    def test_props_to_html(self):
        node = HTMLNode("a", "hello world", None, {"href": "https://boot.dev", "target": "_blank"})
        expected = ' href="https://boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_to_html(self):
        node = HTMLNode("a", "hello world", None, {"href": "https://boot.dev", "target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()