#!/usr/bin/env python
import sys
import textwrap
import re
from typing import Tuple, List, Iterator

MESSAGE = '\n'.join([
    '',
    '{bubble}',
    '   \\',
    '    ~<:>>>>>>>>>',

])


def snakesay(*things) -> str:
    bubble = '\n'.join(speech_bubble_lines(' '.join(things)))
    return MESSAGE.format(bubble=bubble)


def speech_bubble_lines(speech) -> Iterator[str]:
    lines, width = rewrap(speech)
    if len(lines) <= 1:
        text = ''.join(lines)
        yield f'< {text} >'

    else:
        yield '  ' + '_' * width
        yield '/ ' + (' ' * width) + ' \\'
        for line in lines:
            yield f'| {line} |'
        yield '\\ ' + (' ' * width) + ' /'
        yield '  ' + '-' * width


def rewrap(speech: str) -> Tuple[List[str], int]:
    url_pattern = r'https?://[^\s]+'
    if re.search(url_pattern, speech):
        lines = textwrap.wrap(speech, break_long_words=False, break_on_hyphens=False)
    else:
        lines = textwrap.wrap(speech)
    width = max(len(l) for l in lines) if lines else 0
    return [line.ljust(width) for line in lines], width


def main():  # pragma: no cover
    print(snakesay(*sys.argv[1:]))


if __name__ == '__main__':  # pragma: no cover
    main()
