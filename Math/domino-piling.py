def domino(row, col):
    return (row // 2) * col + ((row % 2) * col) // 2

if __name__ == "__main__":
    row, col = map(int, input().split(" "))
    print(domino(row, col))