"""Execute the Python tool excerpts that students see on the slides."""
import ast
from pathlib import Path
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'deck/week12.py'


def panel(title):
    for node in ast.walk(ast.parse(SOURCE.read_text())):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'code_panel' and len(node.args) >= 3
                and ast.literal_eval(node.args[1]) == title):
            return '\n'.join(ast.literal_eval(node.args[2]))
    raise AssertionError(title)


class ToolExcerpts(unittest.TestCase):
    def test_displayed_range_check_rejects_before_loading_or_mutation(self):
        loaded = []
        config = {'speed': 125, 'exit_x': 860}
        def load_config(path):
            loaded.append(path)
            return config
        scope = {'BOUNDS': {'speed': (60, 480)}, 'key': 'speed',
                 'value': 2000, 'path': 'example.json', 'load_config': load_config}
        code = panel('Reject the write before changing state')
        with self.assertRaises(ValueError):
            exec(code, scope)
        self.assertEqual(loaded, [])
        self.assertEqual(config, {'speed': 125, 'exit_x': 860})
        scope['value'] = 275
        exec(code, scope)
        self.assertEqual(config, {'speed': 275, 'exit_x': 860})
        self.assertEqual(loaded, ['example.json'])

    def test_displayed_reservation_counts_check_and_write_differently(self):
        class Clock:
            @staticmethod
            def clock():
                return 42
        code = panel('Reserve the action before execution')
        for action, mutations in [('check', 0), ('set', 1)]:
            state = {'actions': 0, 'mutations': 0}
            scope = {'state': state, 'action': action, 'key': 'speed',
                     'value': 275, 'self': Clock()}
            exec(code, scope)
            self.assertEqual(state, {'actions': 1, 'mutations': mutations})
            self.assertEqual(scope['event']['action'], action)
            self.assertEqual(scope['event']['time'], 42)

    def test_displayed_capture_uses_finite_real_movie_and_user_replay(self):
        calls = []
        def execute(args, timeout):
            calls.append((args, timeout))
        exec(panel('Request a finite movie'), {'execute': execute, 'movie': '/tmp/world.avi'})
        self.assertEqual(calls, [(['--write-movie', '/tmp/world.avi', '--fixed-fps', '30',
                                  '--quit-after', '120', '--', '--replay'], 90)])
        self.assertNotIn('--headless', calls[0][0])


if __name__ == '__main__':
    unittest.main()
