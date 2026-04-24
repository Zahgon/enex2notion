from bs4 import Tag
from enex2notion.note_parser.string_extractor_properties import resolve_string_properties
from enex2notion.note_parser.string_extractor_split_tag import split_tag
from enex2notion.notion_blocks.text import TextProp

def extract_string(tag: Tag) -> TextProp:
    """Convert a block content into a string with properties

     IN: <div>some text <b>bold <i>bold and italic</i></b></div>
    OUT: some text bold bold and italic
         [["some text "], ["bold ", ["b"]], ["bold and italic", ["b", "i"]]]
    """
    pass

def _extract_blocks(div_lines):
    """Get parent stack for each string in the line and convert them to properties

    IN: <div>some text <b>bold</b></div>
    OUT: [
            {"string": "some text", "properties": set()},
            {"string": "bold", "properties": {("b",)}},
         ]
    """
    pass

def _convert_newlines(element: Tag):
    pass

def _parents_upto(tag: Tag, upto: Tag):
    pass

def _add_string_block(string_blocks, string, string_properties):
    pass

def _format_blocks(string_blocks):
    """Notion properties format:

    plain text: ["some text"]
    formatted text: ["some text", ["property"]]
    multiple properties: ["some text", ["property1", "property2"]]
    property with args: ["some text", [["property", "arg"]]]
    """
    pass
