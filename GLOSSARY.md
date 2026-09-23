# Words we use

Plain meanings for the words that come up in the slides and the tutorials. If a word on
a slide is not here, ask — it will be added.

## Files and GitHub

| Word | What it means |
|---|---|
| **repository** (repo) | A folder that git is watching. Your assignment is one; the course material is one. |
| **commit** | A saved version of the folder, with a short message saying what changed. |
| **push** | Send your commits to GitHub. **Pull** brings down what changed there. |
| **clone** | Download a whole repo, with its history, to your machine. |
| **branch** | A parallel version of the same repo. The course repo has `2026` (this year) and `2025` (last year). |
| **fork** | Your own copy of somebody else's repo, under your account. |
| **pull request** (PR) | "I changed something in my copy — please take it into yours." |
| **issue** | A note on a repo: a bug, a question, something unclear. |
| **README.md** | The file GitHub shows on a repo's front page. `.md` is markdown: text with a little formatting. |
| **organisation** (org) | A shared GitHub account for a group. Ours is `sd5913`. Being a member is not the same as being allowed to write to a repo. |
| **the registry** | pfad.ait4x.org — where your GitHub account is matched to your student ID. |

## Running code

| Word | What it means |
|---|---|
| **terminal** | The window where you type commands instead of clicking. In VS Code: `Ctrl+`` ` (the key top-left, under Esc). |
| **script** | A file of Python. `schotter.py` is a script. |
| **run** | Make the computer carry out a script, top to bottom. `uv run schotter.py`. |
| **uv** | The tool that runs Python scripts and fetches what they need. The only Python command we type. |
| **library** (package) | Code somebody else wrote, that your script `import`s. `pygame` is one. |
| **dependency** | A library your script needs. A script should say what it needs at the top. |
| **environment** | The Python and the libraries a script runs with. If it is not written down, the script only works on your machine. |
| **console** (REPL) | A place to type one line of Python at a time and see the answer. On the slides: press the `` ` `` key. |
| **output** | What a program prints or draws when it runs. |
| **error** (traceback) | Python's report of what went wrong and on which line. Read it from the bottom. |

## Reading Python

| Word | What it means |
|---|---|
| **syntax** | The spelling and grammar of code. Wrong syntax: the program does not start. |
| **variable** | A name for a value. `size = 24` makes a variable called `size`. |
| **type** | What kind of value something is: a whole number (`int`), a number with a decimal point (`float`), text (`str`), yes/no (`bool`), a list, a dict. |
| **string** (`str`) | Text. The quotes are what make it text: `"3"` is text, `3` is a number. |
| **list** | Several things in order: `[3, 1, 4]`. Positions count from 0. |
| **dict** (dictionary) | Values you look up by name: `{"name": "Ada"}`. |
| **boolean** (`bool`) | `True` or `False`. What a comparison like `a > b` gives you. |
| **loop** | Do something once for each item: `for w in range(size):`. |
| **condition** | A yes/no test that decides what happens: `if bar or cap:`. |
| **function** | A named piece of code you can call: `print(...)`, `abs(...)`, or one you define with `def`. |
| **return** | What a function hands back. A function with no `return` gives back `None`. |
| **None** | Python's word for "nothing here". |
| **indentation** | The spaces at the start of a line. In Python they say what belongs inside a loop, a condition, a function. Four spaces. |
| **state** | Something a program remembers from one step to the next. `last_square_empty` is state. |
| **random** | A number the program picks by chance. The same **seed** gives the same random numbers again. |
| **tuple** | A short list you do not change, written with round brackets: `(hour, height)`. A coordinate is one. |
| **enumerate** | Loop over a list and get the position as well as the value: `for hour, height in enumerate(heights, start=1):`. |
| **comprehension** | A loop written on one line that collects the answers: `[move(p, 10, 20) for p in shape]`. |

## Data and pictures

| Word | What it means |
|---|---|
| **data** | Numbers somebody measured and published. The tide at Quarry Bay, every earthquake of the last month. |
| **JSON** | A common file format for data: lists and dicts, written out as text. Every number in it is text until you say `float()`. |
| **CSV** | A file of rows and columns, separated by commas. Opens in Excel, reads in three lines of Python. |
| **API** (endpoint) | An address you fetch data from instead of a web page. `data.weather.gov.hk/...?station=QUB` is one. |
| **parse** | Turn a file of text into lists and numbers your program can use. |
| **cache** | Fetch once, save the raw reply into `data/`, then read the saved file. Your script then runs with no internet, and the repo still works when the address moves. |
| **scrape** | Take numbers off a web page that was not meant to be read by a program. A page is a tree; BeautifulSoup walks it. |
| **User-Agent** | The line your script uses to say who it is when it fetches something. Say who you are, and do not fetch in a loop. |
| **plot** | Draw numbers as a picture. **matplotlib** is the library we use for it. |
| **axis** | One direction of a picture, and what it means: hour across, metres up. An unlabelled axis is a picture nobody can read. |
| **vector** | A list of numbers where each position means something: `(hour, height)`, `(lng, lat)`, `(knot, deg)`. Swap them and the picture is nonsense. |
| **transformation** | A rule that turns one vector into another: `move`, `scale`, `rotate`, or hour-and-height into angle-and-radius. A chart type is a transformation. |
| **matrix** | A small table of numbers that *is* a transformation. Matplotlib, CSS and p5.js all call it `transform`. |
| **polar** | Saying where a point is with an angle and a distance instead of x and y. `to_xy` converts one to the other. |
| **projection** | The transformation that puts a round world on a flat page. Longitude across, latitude up is the cheapest one. |
| **frame** | One picture of an animation. An animation is a function of which frame it is: `def frame(i)`. |

## Interfaces and web apps

| Word | What it means |
|---|---|
| **interface** | The part of a program a person can see and use. |
| **input** | Information or an action a person gives the program. |
| **state** | Something a program remembers between actions, such as a selected month or current count. |
| **event** | Something that happens, such as a click, key press, or completed request. |
| **callback** | A function the program runs when an event happens. |
| **client** | A program that asks a service for information or an action. A browser can be a client. |
| **server** | A program that receives requests and sends responses. |
| **request** | A message a client sends to a server, asking for data or an action. |
| **response** | The reply a server sends to a request, often with a status and data. |
| **endpoint** | An address and method a web service responds to, such as `GET /tides`. |
| **JSON** (web response) | A text format commonly used to send structured data between a service and a client. |
| **Streamlit** | A Python library for building small web apps; changing a widget reruns the script. |
| **FastAPI** | A Python library for building web services with endpoints. |
| **session state** | Values Streamlit keeps available across reruns in one browser session. |
| **test** | A repeatable check of whether code meets one stated expectation. |
| **fixture** | Small, known input used by a test so the result is predictable. |
| **unit test** | A test of one small piece of code, separated from the network and other outside systems. |
| **test-driven development** (TDD) | Write a test for the expected behavior, see it fail, implement the rule, then keep the test passing. |
| **GitHub Actions** | GitHub's service for running a workflow when an event such as a push happens. |
| **workflow** | A YAML file that tells GitHub Actions what event starts a job and which steps to run. |
| **workflow_dispatch** | A GitHub Actions event that lets someone start a workflow manually. |

## Checking work

| Word | What it means |
|---|---|
| **spec** (specification) | A sentence about what the program must do, that is either true or false. "A cap never sits under a drawn cell." |
| **bug** (fault) | Code that runs but does the wrong thing. |
| **predict** | Say what the output will be before you run it. |
| **diff** | The lines that differ between two versions of a file. GitHub shows one on every commit. |
| **check** (a workflow) | A program GitHub runs on your repo every time you push, that ends in a green tick or a red cross. |
| **SVG** | A picture described as text — lines, shapes, coordinates. A script can write one. |
