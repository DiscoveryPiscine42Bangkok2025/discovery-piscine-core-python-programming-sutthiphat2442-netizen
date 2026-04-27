#!/usr/bin/env python3

def greetings(name='noble stranger'):
    if not isinstance(name, str):
        print("Error! it was not name.")
    else:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    greetings()
    greetings("Alice")
    greetings(42)