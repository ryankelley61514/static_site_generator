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
