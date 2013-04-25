"""
  
  Answer by: jiweicao
  Copyright: 2013 Jiwei. All rights reserved.
  From: https://www.codeeval.com
  Challenge Description

  Write a program to determine the Mth to last element of a list.

  Input sample:

  The first argument will be a text file containing a series of space delimited characters followed by an integer representing a index into the list(1 based), one per line. e.g.

  a b c d 4
  e f g h 2
  Output sample:

  Print to stdout, the Mth element from the end of the list, one per line. If the index is larger than the list size, ignore that input.
  e.g.

 a
 g
  
"""
import sys
def mth_last_element(filename):
    f = open(filename, 'r')
    for line in f:
        line = line.strip().split(' ')
        if line:
            try:
                m = int(line[-1])
                if m < len(line):
                    yield line[len(line)-m-1]
            except ValueError:
                pass

def main():
    output = mth_last_element(sys.argv[1])
    for item in output:
        print item

if __name__ == "__main__":
    main()


