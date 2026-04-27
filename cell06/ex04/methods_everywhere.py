#!/usr/bin/env python3

import sys
def shrink(s):
    print(s[:8])
def enlarge(s):
    padding = 'z' * (8 - len(s))
    print(s + padding)
def main():
    if len(sys.argv) < 2:
        print("none")
        return
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)
if __name__ == "__main__":    
    main()