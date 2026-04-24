import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass(frozen=True)
class EvernoteResource(object):
    data_bin: bytes
    size: int
    md5: str
    mime: str
    file_name: str

@dataclass
class EvernoteNote(object):
    title: str
    created: datetime
    updated: datetime
    content: str
    tags: List[str]
    author: str
    url: str
    is_webclip: bool
    resources: List[EvernoteResource]
    _note_hash: str = None

    def resource_by_md5(self, md5):
        pass

    @property
    def note_hash(self):
        pass
