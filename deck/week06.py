"""SD5913 Week 6 interactive teaching lesson: sound as data, song APIs and interaction.

The calendar teaching date is deliberately absent until confirmed.
Reuses SD2112's sound figures and instruments, with original source attribution.
"""
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from deckgen import T
from deckgen.layouts import (title, end, agenda, section, content, statement,
                             two_col, figure_slide, code_panel, live)
import week05_figures as I
import week06_figures as F

S = []
EYE = 'SD5913 · WEEK 06'
FOOTER = 'SD5913 · Week 06 · Sound'
IMAGE_SOURCE = 'https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/deck/week05.py'
SOUND_SOURCE = 'https://github.com/venetanji/sd2112-teaching/blob/558d1d77ce6b0e42c2e9ec955ca191d40cb7976e/deck/week06.py'
PY_WAVE = 'https://docs.python.org/3.12/library/wave.html'
ANALYSIS_CODE = (HERE / 'week06_analysis.js').read_text()
SEQUENCER_CODE = (HERE / 'week06_sequencer.js').read_text()

S.append(title(EYE, 'Sound as data', 'Noise, waveforms, speech, songs and interaction.',
    notes='Two-hour lesson. Keep the Week 6 lesson numbering. The teaching date has not been confirmed. '
    'The class builds on Week 5 images and API requests, for designers learning to program with agents. '
    'Have the offline noise and tone files ready. Start with the device volume low. No sound autoplays.'))

S.append(agenda(EYE, [
    'Recall image values and positions', 'Make two seconds of noise',
    'Shape a tone with a rule', 'Explore songs and speech models',
    'Live-code four layers in Strudel', 'Edit with an agent and reflect',
], notes='The making and reflection blocks are part of the two-hour session. '
   'The standard-library examples work without accounts, external packages or a microphone. '
   'A live API generation is an optional instructor demonstration after preflight.'))

S.append(content('OPENING · LISTENING', 'What does a sound ask you to do?', [
    'Imagine a short sound when a file finishes saving.',
    'What would make it reassuring? What would make it distracting?',
    'Would you want to hear it on every save?',
], notes='Give pairs a minute, then take two contrasting answers. This is discussion, not an assessed quiz. '
    'A design judgment should name context and repetition. Students who prefer not to listen can work '
    'from waveform views and descriptions. No hearing test or loudness sweep.'))

S.append(figure_slide('RECALL · WEEK 5', 'An image gives values positions in space', I.pixel_grid(),
    notes='Recall pixel[y][x] and channel order. The exact image grid is reused from the Week 5 course source. '
    'An image array has spatial axes; a mono audio list will have a time axis. Source: ' + IMAGE_SOURCE))

S.append(two_col('01 · ORDERED VALUES', 'A sound gives values positions in time', [
    'A mono sound can use a one-dimensional array.',
    'Each number describes the signal at one instant.',
    'The index tells us which sample comes next.',
    'Zero is the centre of this signed signal.',
], [
    'samples = [', '    0.00, 0.04, 0.08,', '    0.04, 0.00, -0.04,', '    -0.08, -0.04', ']', '',
    'print(samples[2])  # 0.08',
], notes='This is a tiny illustrative sequence, not a playable sound file by itself. '
    'Positive and negative describe opposite directions of signal displacement. They do not mean louder and quieter. '
    'A Python list is enough for today. A typed array such as NumPy packages these values more compactly.'))

S.append(two_col('01 · RANDOM NOISE', 'Random values can become a signal', [
    'Week 5 used random RGB values for pixels.',
    'Here each random value becomes a sample.',
    'A seed lets us repeat this procedure.',
], [
    'import random', '', 'rng = random.Random(7)', 'samples = [',
    '    rng.uniform(-0.08, 0.08)', '    for _ in range(12)', ']', '', 'print(samples)',
], notes='Run the short expression before playing anything. These 12 values only expose the idea. '
    'The full example uses 44,100 samples. This continues pfad/week05/noise.py: explicit seed, ordered values, '
    'then a file writer. A fixed seed repeats this algorithm; it does not define musical meaning. '
    'Source: https://github.com/sd5913/pfad/blob/11252caa6ee6e34937fc3314b396e944be6bdf7d/week05/noise.py'))

S.append(two_col('01 · THE AUDIO CLOCK', 'A sample rate gives the sequence a duration', [
    '22,050 samples per second.',
    'Two seconds need 44,100 mono samples.',
    'Duration = sample count / sample rate.',
], ['sample_rate = 22050', 'seconds = 2', '', 'count = sample_rate * seconds', 'print(count)  # 44100', '',
    '# one sample per time step', 'time = index / sample_rate'],
    notes='Here index stands for a sample index inside a loop. For mono, one frame contains one sample. '
    'For stereo, a frame contains a left and right sample. Do not confuse samples per second with cycles per second.'))

S.append(figure_slide('01 · WAVEFORM AND SAMPLES', 'The waveform shows signal amplitude over time', F.w06_waveform(),
    caption='This illustration uses 44,100 samples/s. The WAV demos use 22,050 samples/s.',
    notes='Reused SD2112 figure. This illustration uses 44,100 samples/s, while the runnable WAV examples use 22,050. '
    'Point out that distinction aloud. The left panel is a computed 220 Hz tone with harmonics over 40 ms, '
    'and the right panel is a 3 ms sampled view. Neither is the random-noise recording. '
    'The two vertical directions are signed amplitude, not more and less loudness. Source: ' + SOUND_SOURCE))

S.append(code_panel('01 · OFFLINE DEMO', 'Two seconds of noise', [
    'import random', 'from wav_support import fade_edges, save_wav',
    'rate, seconds, amplitude = 22050, 2, 0.08', 'rng = random.Random(7)',
    'samples = [rng.uniform(-amplitude, amplitude)', '           for _ in range(rate * seconds)]',
    'samples = fade_edges(samples, rate)', 'save_wav("out/noise.wav", samples, rate)',
], caption='Download from lesson resources, then run: python noise.py',
    notes='Use the supplied complete script, which adds input validation and an output folder option. '
    'It uses only the Python standard library and creates a finite WAV. It never plays automatically. '
    'Show the printed sample count, then open the result in a player at low device volume. '
    'The helper adds a 10 ms fade at each end to reduce sudden jumps. It does not smooth the whole noise signal.'))

S.append(code_panel('01 · VALUES TO A WAV FILE', 'Samples inside a WAV file', [
    'pcm = b"".join(struct.pack("<h", round(x * 32767))', '               for x in samples)',
    'with wave.open("out/noise.wav", "wb") as audio:', '    audio.setnchannels(1)   # mono',
    '    audio.setsampwidth(2)  # 2 bytes = 16 bits', '    audio.setframerate(22050)',
    '    audio.writeframes(pcm)',
], caption='The complete helper imports struct and wave, and checks the values first.',
    notes='This is an excerpt of wav_support.py, not a complete independent script. '
    'The < prefix specifies little-endian bytes and h a signed two-byte integer. '
    'The example maps normalized floats to signed 16-bit PCM. The header supplies channel count, sample width '
    'and sample rate. A WAV can contain different formats; this lesson deliberately writes uncompressed PCM. '
    'Sources: ' + PY_WAVE + ' and https://docs.python.org/3.12/library/struct.html'))

S.append(content('PAIR EXPERIMENT · 6 MINUTES', 'One change, one prediction', [
    'Keep the first noise.wav as a reference.',
    'Change SEED, SECONDS or AMPLITUDE in noise.py.',
    'Predict the difference, then run and compare.',
    'Which part of the result could you explain from the code?',
], notes='Pairs should change only one constant initially. Rename the first output before rerunning '
    'because the script replaces the same filename. Suggested changes: seed 8, duration 1 second, '
    'or amplitude 0.04. Lower amplitude still needs low device volume. Never ask students to increase '
    'volume to a limit or test hearing. Afterward ask which variables change file size and which do not. '
    'Expected: duration changes sample count, seed changes values, amplitude scales values.'))

S.append(two_col('02 · A REPEATING RULE', 'A sine wave repeats smoothly', [
    'Frequency sets cycles per second.',
    'Amplitude scales the signal values.',
    'The sample rate sets how often we take a value.',
], ['import math', '', 'time = i / sample_rate', 'value = amplitude * math.sin(',
    '    2 * math.pi * frequency * time', ')'],
    notes='Read the expression as a recipe, not a trigonometry examination. i advances one sample at a time. '
    'Time gives seconds; frequency counts cycles; 2*pi expresses one cycle in radians; sine returns a repeating '
    'value from -1 to 1; amplitude scales it. Students can inspect and change the recipe with an agent. '
    'The variables shown are supplied by the complete tone.py example.'))

S.append(code_panel('02 · OFFLINE DEMO', 'A two-second tone', [
    'import math', 'from wav_support import fade_edges, save_wav',
    'rate, seconds, amplitude, frequency = 22050, 2, 0.08, 220',
    'samples = [amplitude * math.sin(2 * math.pi * frequency * i / rate)',
    '           for i in range(rate * seconds)]', 'samples = fade_edges(samples, rate)',
    'save_wav("out/tone.wav", samples, rate)',
], caption='Download from lesson resources, then run: python tone.py',
    notes='The complete script performs the same validation as noise.py plus the frequency check. '
    'The file contains 44,100 mono samples, 22,050 samples/s and a 220 Hz sine with short edge fades. '
    'Ask students to identify the one line that replaced the random values.'))

S.append(two_col('02 · TWO DIFFERENT RATES', 'Frequency and sample rate', [
    'Keep SAMPLE_RATE at 22050.',
    'Change FREQUENCY from 220 to 440.',
    'Predict what changes and what stays the same.',
], ['# sample clock', 'SAMPLE_RATE = 22050', '', '# repeating waveform', 'FREQUENCY = 440', '',
    '# unchanged duration', 'SECONDS = 2'],
    notes='The tone has twice as many cycles per second while retaining duration and sample count. '
    'For these sine tones, doubling frequency raises pitch by an octave. Keep the sample rate fixed for this '
    'comparison. Changing the sample-rate label on already generated samples changes playback speed and pitch, '
    'which is a separate experiment.'))

S.append(content('02 · AMPLITUDE AND LISTENING', 'The same numbers can feel different', [
    'Lower AMPLITUDE from 0.08 to 0.04 and compare.',
    'Then imagine the same cue in a quiet room and a busy studio.',
    'What would you need to know about the listener and device?',
], notes='Signal amplitude is measurable. Perceived loudness also depends on frequency, device, listening level '
    'and the listener. Avoid saying half amplitude means half perceived loudness. Use the user-controlled '
    'device volume as an additional precaution. This is a design discussion rather than a hearing test.'))

S.append(figure_slide('02 · SOUND IN THE BROWSER', 'One sound, three views', F.w06_analysis_still(),
    sketch=live('week06-analysis', ANALYSIS_CODE, 1200, 700,
                hint='Click Play · change frequency or waveform · Stop / Escape'),
    caption='HTML has a live instrument. PDF and PowerPoint show the illustrated still.',
    notes='Reused course instrument. Start only with a click. Change sine to triangle and sawtooth and observe '
    'additional frequency components. This uses Web Audio in JavaScript, not the Python WAV writer. '
    'The FFT display measures the browser oscillator output, not a microphone. Stop closes the AudioContext; '
    'Escape and slide navigation also stop. This still is illustrative, not a captured FFT. '
    'Source: ' + SOUND_SOURCE + ' and https://webaudio.github.io/web-audio-api/#AnalyserNode'))

S.append(figure_slide('OPTIONAL BRIDGE · SOUND AS AN IMAGE', 'A spectrogram shows frequency over time', F.w06_spectrogram_how(),
    caption='Time across, frequency up. Shade represents magnitude in this illustration.',
    notes='Optional if students need a link back to Week 5 images. The three panels are illustrative examples, '
    'not one measured signal transformed numerically. A magnitude spectrogram omits phase. '
    'Making an image of sound playable requires more than treating it as ordinary pixels. '
    'Keep the mathematics light and move on if time is short. Source: ' + SOUND_SOURCE))

S.append(section('10 MINUTES', 'Break', 'Save the files you want to compare',
    notes='Stop any browser audio before the break. Preserve at least one before/after pair.'))

S.append(content('03 · PROGRAMS AND MODELS', 'Where do the sound choices come from?', [
    'Our Python rule specifies every sample value.',
    'A song model uses learned patterns to interpret a request.',
    'An agent can help prepare either program and inspect its result.',
    'You still decide whether the sound serves the experience.',
], notes='Avoid treating random/procedural as uncreative or model output as inherently expressive. '
    'The distinction here is how the values are produced. A model prompt describes qualities; it does not '
    'guarantee each note, exact duration or interaction behavior. The agent is a collaborator coordinating '
    'tools; students need evidence of the result.'))

S.append(two_col('03 · WEEK 5 API PARALLEL', 'The request changes. The habit stays useful.', [
    'Prepare a request you can read.',
    'Check the response before using it.',
    'Save the output and its settings.',
], ['# Week 5', 'POST /v1/images/generations', 'image response', '', '# Week 6',
    'POST /v1/audio/generations', 'attempt status, then tracks'], lang=None,
    notes='The image example uses the verified Easel image route and a base64 response. '
    'Audio generation is an Easel extension with an asynchronous Suno-backed flow, not a claim that every '
    'OpenAI-compatible API supports songs. A successful submission is not a completed audio file. '
    'Exact current API provenance is included in site/week06/examples/TEACHER_NOTES.md.'))

# The API contract slides are a small separately reviewed source module.
from week06_api_slides import api_slides
S.extend(api_slides())

from week06_speech_slides import speech_slides
S.extend(speech_slides())

from week06_livecoding_slides import livecoding_slides
S.extend(livecoding_slides())

S.append(content('PAIR REVIEW · FINAL 4 MINUTES', 'What does the other person notice?', [
    'Let your partner try it before you explain.',
    'What action did they expect to make?',
    'Could they tell what changed, and stop it?',
    'What would become tiring after the twentieth use?',
], notes='Listen for claims supported by a concrete observation. Offer waveform/visual feedback review for '
    'anyone who does not want to listen. Ask for one change after the test, rather than broad aesthetic ratings.'))

S.append(content('REFLECTION', 'Which choice can you explain?', [
    'Name one input and the data it changes.',
    'Name one choice you left to a rule, an agent or a model.',
    'What evidence would make you revise the sound?',
], notes='Take a few spoken answers or a short private note. No answer bank, ClassPoint response collection '
    'or publication is configured. The aim is to connect a programming decision to a design consequence.'))

S.append(content('PRACTICE · 10 MINUTES', 'Try the existing mock', [
    'The instructor opens the mock practice already supplied.',
    'Try a short selection with your course notes beside you.',
    'For one answer, trace the code and explain your reasoning.',
    'Note one concept to revisit before 22 October.',
], notes='Reuse the existing mock package; do not create or publish assessed questions or an answer bank. '
    'No verified course Canvas URL was supplied, so the instructor opens the existing resource directly. '
    'Suggested split: six minutes individual practice, four minutes explain and compare reasoning. '
    'This classroom slot does not establish the actual quiz duration or permitted tools.'))

S.append(content('LINKED RESOURCES', 'Keep the code, not just the sound', [
    '[Open the lesson resources](resources.html)',
    'Four cumulative Strudel scores and links to the editor.',
    'Python WAV, local speech models and the song-request preview.',
    'Tutorial video: pending the instructor’s selection.',
], notes='The resources page and examples travel with the HTML preview. '
    'The requested tutorial video has not been identified. Keep its status explicit; add the exact link '
    'on this same branch when supplied rather than guessing a video.'))

S.append(content('ASSESSMENT · 22 OCTOBER 2026', 'Quiz · Thursday 22 October', [
    'Open-book, timed, multiple choice.',
    'Practise tracing the course examples and explaining the output.',
    'Question count and duration will be announced.',
], notes='Keep the confirmed date and format. The question count, duration and permitted tools beyond '
    'open-book are not confirmed. Do not imply that AI use is authorized. This lesson does not replace '
    'or recreate the previously supplied mock quiz. Date: current Week 5 deck. Format: instructor briefing.'))

S.append(content('ASSIGNMENT 3 · 15 POINTS', 'An interactive experience', [
    'A user input and program response should form a loop.',
    'A website, survey or command-line program can work.',
    'Due Sunday 1 November, 23:59 Hong Kong time.',
    'Detailed rubric and submission instructions are separate.',
], notes='The current Week 5 instructor lesson plan confirms 1 November 2026 at 23:59 '
    'Hong Kong time. The instructor briefing supplies 15 points. Rubric component weights remain unconfirmed. Audio and AI generation '
    'are possibilities, not required features. Source: '
    'https://github.com/sd5913/teaching/blob/dd8e30ed640af73008f283fd6cbcca9167fc3735/lessons/week05-lesson-plan.md'))

S.append(end('What should the listener notice?',
    'A sound is data, a design choice and part of an interaction.',
    'sd5913.github.io/teaching',
    notes='Close with one concrete choice from the room.'))

# Optional worked interaction, after the main lesson close.
S.append(figure_slide('OPTIONAL · SOUND IN THE BROWSER', 'A click changes the score', F.w06_written_score(),
    sketch=live('week06-score', SEQUENCER_CODE, 1000, 600,
                hint='Click Play · change one cell · Stop / Escape'),
    caption='Four sine voices, eight steps. Each cell chooses whether a note plays.',
    notes='Use the original course-owned sequencer as a worked example. Click an empty cell, observe the '
    'changed grid value and then listen when the playhead reaches that step. This is JavaScript Web Audio, '
    'not Python or the API. A visible playhead is feedback. Stop, Escape, navigation and page hiding close '
    'the audio context. No microphone, account or external sample pack is involved. Source: ' + SOUND_SOURCE))

S.append(two_col('OPTIONAL · READING THE INTERACTION', 'A small state change has an audible result', [
    'The grid stores the score.',
    'A click toggles one value between 0 and 1.',
    'The player reads the current grid at each step.',
], ['// excerpt from the browser instrument', 'grid[r][c] = 1 - grid[r][c];', '',
    '// the scheduler checks a cell', 'if (grid[r][step]) {', '  // schedule a short note', '}'], lang='js', right_size=28,
    notes='This is a shortened excerpt explaining state, not a complete sequencer. The full script ships with '
    'the deck. Row maps to pitch and column to a time step. A click changes the data immediately; sound '
    'changes when the scheduler next reaches that step. Ask students where they would put a mute control.'))

for index, slide in enumerate(S, 1):
    slide.els.append(T(1400, 1000, 400, 32, f'{index:02d}', 'monomed', 22,
        '#CCDADD' if slide.bg not in ('#FFFFFF', '#F4F4F2') else '#5C6470', lh=1.2, align='r',
        valign='b', spc=0.14, name='week06-slide-number'))

DECK = {'title': 'SD5913 · Week 6 · Sound as data', 'pdf': 'SD5913-week06.pdf', 'slides': S}
