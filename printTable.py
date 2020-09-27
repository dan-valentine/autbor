#! python3

def printTable(table):
    
    longestList = []

    for i in range(len(table)) :
        longest = len(table[i][0])

        for j in range(len(table[i])) :
            length = len(table[i][j])
            if length > longest :
                longest = length

        longestList.append(longest)

    print(longestList)

    for i in range(len(table[0])) :
        for j in range(len(table)) :
            print(table[j][i].rjust(longestList[j]+1), end='')

        print('')


table = [['apples', 'oranges', 'cherries', 'bananas'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

printTable(table)
