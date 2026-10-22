"""Count words, lines, and characters in a text file."""
import sys


def count(text):
    words = text.split(" ")
    lines = text.split("\n")
    return {"words": len(words), "lines": len(lines), "chars": len(text)}


def main():
    path = sys.argv[1]
    with open(path) as f:
        result = count(f.read())
    print(f"{result['lines']} lines, {result['words']} words, {result['chars']} characters")


if __name__ == "__main__":
    main()
