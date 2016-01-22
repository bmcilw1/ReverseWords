#!/usr/bin python

from __future__ import print_function, absolute_import
import sys

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    out = open("out.txt", 'w')
    cases = int(f.readline())

    for case in range(1, cases + 1):
        wordList = f.readline().split()

        print("Case #" + str(case) + ":", file=out, end="")

        for word in reversed(wordList):
            print(" " + word, file=out, end="")
        
        print("", file=out)

    out.close()
    f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
