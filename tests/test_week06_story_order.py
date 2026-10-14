"""Week 6 moves from sound to music, then transcript-driven speech interaction."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'deck'))


class StoryOrderTests(unittest.TestCase):
    def test_music_and_strudel_precede_song_api_and_speech(self):
        import week06

        titles = [slide.title for slide in week06.S]
        sound = titles.index('A vibration travels through air')
        score = titles.index('A click changes the score')
        strudel = titles.index('Hi-hat')
        request = titles.index('A request describes the intended sound')
        speech = titles.index('Speech to text. Text to speech.')
        console = titles.index('Speak into Python. Check each chunk.')
        diagram = titles.index('One recognizer, two microphone paths')
        browser = titles.index('The same transcript moves into the browser')
        reply = titles.index('A response begins with a checked transcript')
        self.assertTrue(sound < score < strudel < request < speech < console < diagram < browser < reply)
        self.assertTrue(all(index < titles.index('Try the existing mock') for index in
                            (speech, console, browser, reply)))


if __name__ == '__main__':
    unittest.main()
