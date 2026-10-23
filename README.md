# herdr-demo-word-count

A tiny word and line counter used in a Starry Hope video about Herdr. It has two known bugs on purpose.

## Usage

Requires Python 3. Pass the path of a text file to count:

```sh
python3 wordcount.py sample.txt
```

The script prints a single summary line in this form:

```
<lines> lines, <words> words, <characters> characters
```

Run the tests with:

```sh
python3 -m unittest test_wordcount.py
```

Some tests fail until the two intentional bugs are fixed.
