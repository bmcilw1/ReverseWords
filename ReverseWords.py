#!/usr/bin python

from __future__ import print_function
import sys

def main():
    filename = sys.argv[1]
    f = open(filename, 'rU')
    out = open("out.txt", 'w')
    cases = int(f.readline())

    for case in range(1, cases + 1):
        wordList = f.readline().split()

        out.write("Case #" + str(case) + ":")

        for word in reversed(wordList):
            out.write(" " + word)
        
        out.write("\n")

    out.close()
    f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
