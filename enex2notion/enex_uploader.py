import logging
from notion.block import CollectionViewPageBlock, PageBlock
from notion.collection import CollectionRowBlock
from notion.operations import build_operation
from requests import RequestException
from tqdm import tqdm
from enex2notion.enex_types import EvernoteNote
from enex2notion.enex_uploader_block import upload_block
from enex2notion.utils_exceptions import NoteUploadFailException
logger = logging.getLogger(__name__)
PROGRESS_BAR_WIDTH = 80

def upload_note(root, note: EvernoteNote, note_blocks, keep_failed):
    pass

def _upload_note(root, note: EvernoteNote, note_blocks, keep_failed):
    pass

def _update_edit_time(page, date):
    pass

def _make_page(note, root):
    pass
