import argparse


def main(documentsTxt):
    # Write the code to compute the One Hot Encodings for various "documents"
    # Make sure that your terminal output matches the terminal output of the example given on the instructions.
    wordDict = {}
    numOfLines = 0

    # make all the words in documentsTxt lowercase
    documentsTxt = documentsTxt.lower()

    # create a dictionary of all the words in the documents
    for line in documentsTxt.splitlines():
        string_list = line.split()
        numOfLines += 1
        for i in string_list:
            if i not in wordDict:
                wordDict[i.lower()] = string_list.count(i)

    # put the words in alphabetical order
    wordDict = dict(sorted(wordDict.items(), key=lambda item: item[0]))

    # create a matrix of numOfLines x len(wordDict)
    array = [[0 for x in range(len(wordDict))] for y in range(numOfLines)]

    # fill the matrix with the amount of times each word appears in each document
    for i in range(numOfLines):
        for j in range(len(wordDict)):
            if list(wordDict.keys())[j] in documentsTxt.splitlines()[i].split():
                array[i][j] = documentsTxt.splitlines()[i].split().count(list(wordDict.keys())[j].lower())

    # return the matrix
    return array


if __name__ == "__main__":
    parser = argparse.ArgumentParser("One Hot Encoder")
    parser.add_argument("--fpath", type=str, help="Name of the txt file to be read in")
    args = parser.parse_args()
    print('# Features:')
    matrix = main(open(args.fpath).read())
    for i in range(len(matrix)):
        print(matrix[i])
