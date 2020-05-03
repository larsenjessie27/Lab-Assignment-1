visited = []
map = []
rows = 0
cols = 0

def readDataFromFile():
    with open("sam_2.txt", "r") as infile:
        line = infile.readline()
        len_list = line.split(" ")

        global rows
        rows = int(len_list[0])
        global cols
        cols = int(len_list[1])
        for line in infile:
            line = line.replace("\n", "")
            line = list(line)
            map.append(line)
            # appending row of 0's that are the size of the line
            visited.append([0]*len(line))



def findLongestPathLength():
    length = []
    for y in range(len(map)):
        for x in range(len(map[0])):
            length.append(findPathLengthRecursive(x,y))

    return max(length)

def findPathLengthRecursive(i, j):
    if i < 0 or j < 0 or i >= rows or j >= cols:
        return 0
    if map[j][i] != "A":
        return 0
    if visited[j][i] == 1:
        return 0
    visited[j][i] = 1
    #
    path_length = 1 + find_max(findPathLengthRecursive(i + 1, j),
                      findPathLengthRecursive(i - 1, j),
                      findPathLengthRecursive(i, j - 1),
                      findPathLengthRecursive(i, j + 1))
    visited[j][i] = 0
    return path_length



def find_max(a, b, c, d):
    list1 = []

    list1.append(a)
    list1.append(b)
    list1.append(c)
    list1.append(d)
    return max(list1)


def main():
    readDataFromFile()
    length = findLongestPathLength()
    print("Map Dimensions:")
    print("Number of rows: ", rows)
    print("Number of columns: ", cols)
    print("Length of longest A path: ", length)

main()
