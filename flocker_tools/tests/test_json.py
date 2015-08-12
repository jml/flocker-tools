from testtools import TestCase


from flocker_tools._json import repair_json


class TestRepairJSON(TestCase):


    def test_one_json_line(self):
        self.assertEqual([{'foo': 'bar'}], list(repair_json(['{"foo": "bar"}'])))

    def test_split_json_line(self):
        lines = ['{"foo":\n', ' "bar"}']
        self.assertEqual([{'foo': 'bar'}], list(repair_json(lines)))

    def test_split_across_multiple_lines(self):
        lines = ['{"f\n', 'oo\n', '":\n', ' "ba\n', 'r"}']
        self.assertEqual([{'foo': 'bar'}], list(repair_json(lines)))

    def test_begins_with_non_json(self):
        # We might have a log that starts with a line that's part of a wrapped
        # JSON expression. Just ignore it.
        lines = [
            '"bar", "baz"], "qux": 3}\n',
            '{"foo":\n',
            '"bar"}\n',
        ]
        self.assertEqual([{'foo': 'bar'}], list(repair_json(lines)))


