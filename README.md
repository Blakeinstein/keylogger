# Python Keylogger

---

#### DISCLAIMER: THIS PROJECT WAS MADE PURELY FOR LEARNING PURPOSES. I SHALL NOT BE HELD RESPONSIBLE FOR ANYTHING THE PROJECT IS USED FOR. USE AT YOUR OWN RISK.

A simple keylogger proof of concept built with python for the course Information Security(CSL 466). The project uses:

- Dependency and Package Management: [`Poetry`](https://python-poetry.org/)

- Keyboard hooks: [`keyboard`](https://github.com/boppreh/keyboard)

Features:

- Cross-platform support

- Requires admin requirements on linux machines.

## Usage

---

### With Poetry

1. Install Poetry
   
   > Follow the instructions at https://python-poetry.org/docs/#installation

2. Clone this repository and cd into the project directory
   
   > `git clone https://github.com/blakeinstein/keylogger && cd keylogger`

3. Set up env using poetry
   
   > `poetry install`

4. Read the help document
   
   > `poetry run keylogger -h`

5. Run the keylogger with default arguments
   
   > `poetry run keylogger`

### Without Poetry

1. Install python 3.10

2. Clone this repository and cd into the project directory
   
   > `git clone https://github.com/blakeinstein/keylogger && cd keylogger`

3. (Optional) Setup a virtual env

4. Install dependencies
   
   > `pip install -r requirements.txt`

5. Read the help document
   
   > `python keylogger/main.py -h`

6. Run the keylogger with default arguments
   
   > `python keylogger/main.py`
