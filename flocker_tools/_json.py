"""
Tools for repairing JSON.
"""

from __future__ import print_function

import json
import sys


def repair_json(lines):
    """
    Eliot emits JSON objects one per line. journald wraps long lines. This
    function takes those wrapped lines and yields JSON objects from them.
    """
    line_buffer = []
    for line in lines:
        line = line.strip()
        if not line_buffer and not line[0] == '{':
            # Only begin processing when we detect the first object.
            continue
        line_buffer.append(line)
        try:
            yield json.loads(''.join(line_buffer))
        except ValueError:
            continue
        line_buffer = []


def main():
    filenames = sys.argv[1:]
    if not filenames:
        files = [sys.stdin]
    else:
        files = (open(filename, 'r') for filename in filenames)
    for f in files:
        for json_object in repair_json(f):
            print(json.dumps(json_object), file=sys.stdout)
