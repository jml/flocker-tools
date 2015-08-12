"""
Tools for repairing JSON.
"""

from __future__ import print_function

from itertools import chain
import json
import sys


def repair_json(lines, max_lines_in_buffer=100):
    """
    Eliot emits JSON objects one per line. journald wraps long lines. This
    function takes those wrapped lines and yields JSON objects from them.
    """

    def discard(line):
        sys.stderr.write('DISCARDING: {}\n'.format(line))

    unprocessed_lines = None

    line_buffer = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if not line_buffer and not line[0] == '{':
            # Only begin processing when we detect the first object.
            # DISCARD
            discard(line)
            continue
        line_buffer.append(line)
        if len(line_buffer) > max_lines_in_buffer:
            discard(line_buffer[0])
            unprocessed_lines = chain(iter(line_buffer[1:]), lines)
            break
        try:
            yield json.loads(''.join(line_buffer))
        except ValueError:
            continue
        line_buffer = []
    # If we have unprocessed lines that means that we have the beginning of a
    # JSON object but no official "end". Therefore, DISCARD the beginning and
    # see if we can salvage anything.
    #
    # XXX: This makes the whole thing at least O(n**2) in the worst case.
    if not unprocessed_lines:
        unprocessed_lines = line_buffer[1:]
    if unprocessed_lines:
        discard(line_buffer[0])
        for item in repair_json(unprocessed_lines):
            yield item


def main():
    filenames = sys.argv[1:]
    if not filenames:
        files = [sys.stdin]
    else:
        files = (open(filename, 'r') for filename in filenames)
    for f in files:
        for json_object in repair_json(f):
            print(json.dumps(json_object), file=sys.stdout)
