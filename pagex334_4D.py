def checkSudoku(game):
    length = len(game)
    if length < 1:
        return False
    for i in range(length):
        row = []
        col = []
        for j in range(length):
            if game[j][i] in col:
                return False
            else:
                col.append(game[j][i])
            if game[i][j] in row:
                return False
            else:
                row.append(game[i][j])
    return True 
