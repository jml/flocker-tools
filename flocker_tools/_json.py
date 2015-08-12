"""
Tools for repairing JSON.
"""

import json


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

