from textnode import TextType, TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import re

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", text_node.text, {"src": text_node.url, "alt": text_node.text})

    raise Exception("Invalid TextType.")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            raise Exception("Invalid Markdown syntax.")
        node_split = node.text.split(delimiter)
        for i in range(len(node_split)):
            if node_split[i] == '':
                continue
            if i % 2 == 1:
                new_nodes.append(TextNode(node_split[i], text_type))
            else:
                new_nodes.append(TextNode(node_split[i], TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return links

        
        