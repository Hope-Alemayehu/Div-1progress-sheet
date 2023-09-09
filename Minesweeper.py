class Solution(object):
    def updateBoard(self, board, click):
        def dfs(r, c):
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or board[r][c] != 'E':
                return

            # Count mines in adjacent cells
            mines = sum(1 for dr in [-1, 0, 1] for dc in [-1, 0, 1] if (0 <= r + dr < len(board)) and (0 <= c + dc < len(board[0])) and board[r + dr][c + dc] == 'M')

            if mines == 0:
                board[r][c] = 'B'
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        dfs(r + dr, c + dc)
            else:
                board[r][c] = str(mines)

        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)

        return board
