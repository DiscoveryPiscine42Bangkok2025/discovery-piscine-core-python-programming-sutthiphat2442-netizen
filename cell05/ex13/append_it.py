#!/usr/bin/env python3
import sys

def main():
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("none")
        return
    for word in arguments:
        if not word.endswith("ism"):
            print(word + "ism")

if __name__ == "__main__":
    main()
