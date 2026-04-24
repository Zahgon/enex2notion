import itertools
import logging
from pathlib import Path
from typing import Optional
from enex2notion.enex_parser import count_notes, iter_notes
from enex2notion.enex_types import EvernoteNote
from enex2notion.enex_uploader import upload_note
from enex2notion.enex_uploader_modes import get_notebook_database, get_notebook_page
from enex2notion.note_parser.note import parse_note
from enex2notion.utils_exceptions import NoteUploadFailException
from enex2notion.utils_static import Rules
logger = logging.getLogger(__name__)

class DoneFile(object):

    def __init__(self, path: Path):
        self.path = path
        try:
            with open(path, 'r') as f:
                self.done_hashes = {line.strip() for line in f}
        except FileNotFoundError:
            self.done_hashes = set()

    def __contains__(self, note_hash):
        return note_hash in self.done_hashes

    def add(self, note_hash):
        pass

class EnexUploader(object):

    def __init__(self, import_root, mode: str, done_file: Optional[Path], rules: Rules):
        self.import_root = import_root
        self.mode = mode
        self.rules = rules
        self.done_hashes = DoneFile(done_file) if done_file else set()
        self.notebook_root = None
        self.notebook_notes_count = None

    def upload_notebook(self, enex_file: Path):
        pass

    def upload_note(self, note: EvernoteNote, note_idx: int):
        pass

    def _parse_note(self, note):
        pass

    def _get_notebook_root(self, notebook_title):
        pass

    def _upload_note(self, notebook_root, note, note_blocks):
        pass

    def _attempt_upload(self, upload_func, error_message, *args, **kwargs):
        pass
