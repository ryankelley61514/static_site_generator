class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode(\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}\n)"

    def to_html(self):
        raise NotImplementedError("Feature not yet implemented.")
    
    def props_to_html(self):
        if not self.props:
            return ""
        props_string = f""
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        
        return props_string

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode has no value.")
        if not self.tag:
            return f"{self.value}"
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode has no tag.")
        if not self.children:
            raise ValueError("ParentNode has no children.")
        node_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            node_string += child.to_html()
        node_string += f"</{self.tag}>"
        return node_string
