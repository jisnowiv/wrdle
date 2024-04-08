# Wrdle
Wrdle is a Python clone of the New York Times word guessing game (Wordle). The project is mostly from the tutorial [Build a Wordle Clone With Python and Rich](https://realpython.com/python-wordle-clone/). I made a few changes, including:
* A replay option
* A set element to store previously used words (currently it only works during the game's run)
* A trie to efficiently check if a guess is in the word list (not necessary but interesting to implement) 

## Installation
Initialize a virtual environment and then install [Rich](https://realpython.com/python-rich-package/).
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
invalid characters you get another guess (the invalid guess won't be listed).
There are several attached images of gameplay, currently I'm procrastinating the task of putting them into the readme.

## Contributing
Pull requests are welcome. Known issues include:

* There is a minor issue with duplicate letters. If a letter appears twice in a word, the guess checker treats 
the second occurrence as the first letter. For example, if the word is **float** and the guess is **fluff**, the latter 
two *f*'s in the guess will be marked as misplaced, even though there's only one *f* in the correct word.
* Another improvement would be some way to store previously used words, in some kind of offline cache.
