from notion import block

from enex2notion.notion_blocks.base import NotionBaseBlock


class NotionEmbedBlock(NotionBaseBlock):
    def __init__(self, width=None, height=None, url=None, **kwargs):
        super().__init__(**kwargs)

        self.width = width
        self.height = height
        self.source_url = url

    @property
    def height(self):
        pass

    @height.setter
    def height(self, height):
        pass

    @property
    def width(self):
        pass

    @width.setter
    def width(self, width):
        pass

    @property
    def source_url(self):
        pass

    @source_url.setter
    def source_url(self, source_url):
        pass


class NotionImageEmbedBlock(NotionEmbedBlock):
    type = block.ImageBlock
