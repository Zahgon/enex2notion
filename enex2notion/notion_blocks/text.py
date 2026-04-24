from notion import block
from enex2notion.notion_blocks.base import NotionBaseBlock

def _lstrip_properties(properties):
    pass

def _rstrip_properties(properties):
    pass

class TextProp(object):

    def __init__(self, text, properties=None):
        self.text = text
        self.properties = [[text]] if properties is None else properties
        if properties is None:
            self.properties = [[text]] if text else []

    def strip(self):
        pass

    def __eq__(self, other):
        return self.text == other.text and self.properties == other.properties

    def __repr__(self):
        return '<{0}> {1}'.format(self.__class__.__name__, self.text)

class NotionTextBased(NotionBaseBlock):

    def __init__(self, text_prop: TextProp=None, **kwargs):
        super().__init__(**kwargs)
        if text_prop:
            self.attrs['title_plaintext'] = text_prop.text
            self.properties['properties.title'] = text_prop.properties
        else:
            self.attrs['title_plaintext'] = ''
            self.properties['properties.title'] = []

    @property
    def text_prop(self):
        pass

    @text_prop.setter
    def text_prop(self, text_prop: TextProp):
        pass

class NotionTextBlock(NotionTextBased):
    type = block.TextBlock
