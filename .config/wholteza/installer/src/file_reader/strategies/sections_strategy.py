from pathlib import Path
import os
import pathlib
from src.file_reader.utilities.file import ensure_exists

SECTION_BEGINNING = ">>>"
SECTION_END = "<<<"


def get_section_indexes(rows: list[str]):
    for beginning_index, possible_beginning in rows:
        if possible_beginning.startswith(SECTION_BEGINNING):
            for end_index, possible_end in rows:
                if possible_end.startswith(SECTION_END):
                    return (beginning_index, end_index)
    return None


def read(file: Path):
    """Returns sections of a file as a list using \">>>\" and \"<<<\" to separate different sections.

    Ignores lines outside of a \">>>\" \"<<<\" section.
    """

    ensure_exists(file)

    opened_file = open(file, "rt")

    rows = []
    for row in opened_file:
        rows.append(row)
    opened_file.close()

    sections = []
    while get_section_indexes(rows) != None:
        section_indexes = get_section_indexes(rows)
        section_rows = rows[section_indexes[0]:section_indexes[1] + 1]
        sections.append("".join(section_rows))
        for row in section_rows:
            rows.remove(row)
    return sections