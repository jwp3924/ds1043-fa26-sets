"""abbrev.py

Scan a file for known "abbreviations" and replace those with the full word. May also be used for correcting common typos.

"""


def load_abbrevs(filename: str) -> dict[str, str]:
    """Load a Tab Separated Values file containing substrings for replacement"""
    with open(filename, 'r') as abbrev_key:
        abbreviations = {}
        key = ''
        val = ''
        word = ''
        for line in abbrev_key.readlines():
            for letter in line:
                if letter == '\t':
                    key = word
                    word = ''
                elif letter == '\n' and len(word) > 0:
                    val = word
                    word = ''
                else:
                    word += letter
            abbreviations[key] = val
            key = ''
            val = ''
    return abbreviations

def read_textfile(filename:str) -> list[str]:
    """Read a text file for substring replacement"""
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    words = []
    word = ''
    with open(filename, 'r') as textfile:
        for letter in textfile.read():
            if letter in alphabet:
                word += letter
            else:
                if len(word) > 0:
                    words.append(word)
                    word = ''
                    words.append(letter)
    return words

print(read_textfile('typos.txt'))

def write_textfile(lines: list[str], filename: str) -> None:
    """Write out the corrected text"""
    output = ''
    for line in lines:
        output += line
    with open(filename, 'w') as textfile:
        textfile.write(output)
    return


if __name__ == '__main__':
    abbrevs = load_abbrevs('abbrev.tsv')
    lines = read_textfile('typos.txt')
    # Use abbrevs to correct the text in lines here
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    corrected
    for line in lines:
        if line.lower() in abbrevs:
            corrected = abbrevs[line.lower()]
            finalized = ''
            for i in range(len(corrected)):
                if i == 0 and line[0] in uppercase:
                    finalized += line[0]
                else:
                    finalized += corrected[i]

    write_textfile(lines, 'corrected.txt')
