from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url
        
    def __eq__(x, y):
        return x.text == y.text and x.text_type == y.text_type and x.url == y.url
        
    def __repr__(object):
        return "TextNode(" + object.text + ", " + object.text_type.value + ", " + object.url + ")"
        

