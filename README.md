# wordle-helper

Determine remaining set of Wordle answers after guesses

# Usage

## Prompts

The script will take input of each of your guesses in order. 
1. Enter the first 5 letter guess
2. You'll be prompted for the position of yellow characters for the inputted guess. Enter the position (1-5) of each yellow character. If there are multiple yellow characters, then put in both numbers with no delimiiter. Example: If the second and fifth positions were yellow, then enter `25`. If there are no yellow characters, just press `enter` with no input.
3. You'll be prompted for the position of green characters for the inputted guess

## Help
```console
Usage: wordle-helper.py [OPTIONS]

  Show remaining wordle possibilities

Options:
  -f, --filename TEXT  File path to possible word answers
  -b, --batch INTEGER  Number of possible answers per output row
  -q, --quiet          Suppress the final word list
  --help               Show this message and exit.
```

## Example

Wordle 246
```console
$ python3 wordle-helper.py
Guessed word (word 1) (empty to stop): outer
Yellow positions (word 1): 3
Green positions (word 1): 
Guessed word (word 2) (empty to stop): banks
Yellow positions (word 2): 
Green positions (word 2): 2
Guessed word (word 3) (empty to stop): 

Possible answers after guess 1: 98
Possible answers after guess 2: 7
Final set size: 7 words
cacti faith tacit taffy tally waltz yacht
```

Wordle 249 (quiet mode)
```console
$ python3 wordle-helper.py --quiet
Guessed word (word 1) (empty to stop): crane
Yellow positions (word 1):   
Green positions (word 1): 25
Guessed word (word 2) (empty to stop): grime
Yellow positions (word 2): 
Green positions (word 2): 25
Guessed word (word 3) (empty to stop): broke
Yellow positions (word 3): 
Green positions (word 3): 235
Guessed word (word 4) (empty to stop): prove
Yellow positions (word 4): 
Green positions (word 4): 2345
Guessed word (word 5) (empty to stop): 

Possible answers after guess 1: 26
Possible answers after guess 2: 12
Possible answers after guess 3: 8
Possible answers after guess 4: 2
```
