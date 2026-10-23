"""Count words, lines, and characters in a text file."""
import argparse
import json


def count(text):
    words = text.split(" ")
    lines = text.split("\n")
    return {"words": len(words), "lines": len(lines), "chars": len(text)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="text file to count")
    parser.add_argument("--json", action="store_true", help="print the counts as JSON")
    args = parser.parse_args()
    with open(args.path) as f:
        result = count(f.read())
    if args.json:
        print(json.dumps(result))
    else:
        print(f"{result['lines']} lines, {result['words']} words, {result['chars']} characters")


if __name__ == "__main__":
    main()
