import argparse
import numpy as np


def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    wordDict = {}
    numOfLines = 0
    for line in documentsTxt.splitlines():
        string_list = line.split()
        numOfLines += 1
        for i in string_list:
            if i not in wordDict:
                wordDict[i.lower()] = string_list.count(i)

    array = np.empty(numOfLines, len(wordDict))

    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    main(open(args.fpath).read())
