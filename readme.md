# Wrdle
Wrdle is a Python clone of the New York Times word guessing game (Wordle).

## Installation
```
python -v venv venv
source venv/bin/activate
python -m pip install rich
```

## Usage
```python wrdle.py <d>```

Optional *d* flag is for debug mode (extra print statements).

## Gameplay
Each round gives you six guesses, each guess must contain five letters. If a word is not in the word list, or contains
invalid characters, you get a another guess.


## Contributing
Pull requests are welcome.

Currently, there is a minor issue with duplicate letters. If a letter appears twice in a word, the guess checker treats 
the second occurrence as the first letter. For example, if the word is **float** and the guess is **fluff**, the latter 
two *f*'s in the guess will be marked as misplaced, even though there's only one *f* in the correct word.