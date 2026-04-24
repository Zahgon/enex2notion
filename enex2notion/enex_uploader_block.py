import re
import requests
from notion.block import FileBlock
from enex2notion.enex_types import EvernoteResource
from enex2notion.notion_blocks.uploadable import NotionUploadableBlock

def upload_block(root, block):
    pass

def _upload_file(new_block, resource: EvernoteResource):
    """Copy/paste from EmbedOrUploadBlock class

    changes:
        binary resource.data_bin in put requests instead of file path
        set size and title for FileBlock
    """
    pass

def _extract_file_id(url):
    pass

def _sizeof_fmt(num):
    pass
