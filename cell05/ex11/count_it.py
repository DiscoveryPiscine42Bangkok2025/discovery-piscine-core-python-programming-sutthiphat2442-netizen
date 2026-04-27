#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for item in args:
        print(f"{item}: {len(item)}")
