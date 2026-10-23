# herdr-demo-word-count

A tiny word and line counter used in a Starry Hope video about Herdr. It has two known bugs on purpose.

## Usage

Run `wordcount.py` with Python 3, passing the path to a text file:

```sh
python3 wordcount.py sample.txt
```

It prints the line, word, and character counts on one line:

```
<lines> lines, <words> words, <chars> characters
```

Run the tests with:

```sh
python3 -m pytest test_wordcount.py
```
