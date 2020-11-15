def chessboard(n):
    chessboard = np.full((n, n), 0, dtype = int)
    chessboard[1::2,::2] = 1
    chessboard[::2,1::2] = 1
    return chessboard

#chessboard(8)