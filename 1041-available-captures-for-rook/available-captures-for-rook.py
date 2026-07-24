class Solution(object):

  def numRookCaptures(self, board):

    r_row, r_col = None, None
    for i in range(8):
      for j in range(8):
        if board[i][j] == 'R':
          r_row, r_col = i, j
          break

    captures = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
      r, c = r_row + dr, r_col + dc
      while 0 <= r < 8 and 0 <= c < 8:
        if board[r][c] == 'B':
          break
        if board[r][c] == 'p':
          captures += 1
          break
        r += dr
        c += dc

    return captures