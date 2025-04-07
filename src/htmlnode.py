class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        try:
            lista = []
            for key in self.props:
                lista.append(f' {key}="{self.props[key]}"')
            texto = "".join(lista)
        except TypeError:
            return ""
        return texto
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Node must have a value")
        if self.tag == None:
            return str(self.value)
        return fr"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Node must have a tag")
        if self.children == None:
            raise ValueError("Parent Node must have a children")
        lres = []
        for child in self.children:
            lres.append(child.to_html())
        res = "".join(lres)
        return fr"<{self.tag}{self.props_to_html()}>{res}</{self.tag}>"
