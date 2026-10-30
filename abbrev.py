"""abbrev.py

Scan a file for known "abbreviations" and replace those with the full word. May also be used for correcting common typos.

"""


def load_abbrevs(filename: str) -> dict[str, str]:
    """Load a Tab Separated Values file containing substrings for replacement"""
    return {'': ''}


def read_textfile(filename:str) -> list[str]:
    """Read a text file for substring replacement"""
    return ['']


def write_textfile(lines: list[str], filename: str) -> None:
    """Write out the corrected text"""
    return


if __name__ == '__main__':
    abbrevs = load_abbrevs('abbrev.tsv')
    lines = read_textfile('typos.txt')
    # Use abbrevs to correct the text in lines here
    write_textfile(lines, 'corrected.txt')
