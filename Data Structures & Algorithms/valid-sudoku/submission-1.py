class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check rows
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Check columns
        for i in range(n):
            seen = set()
            for j in range(n):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in seen:
                    return False
                else:
                    seen.add(board[j][i])

        # Box 1: top left
        seen = set()
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 2: top middle
        seen = set()
        for i in range(0, 3):
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 3: top right
        seen = set()
        for i in range(0, 3):
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 4: middle left
        seen = set()
        for i in range(3, 6):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 5: center
        seen = set()
        for i in range(3, 6):
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 6: middle right
        seen = set()
        for i in range(3, 6):
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 7: bottom left
        seen = set()
        for i in range(6, 9):
            for j in range(0, 3):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 8: bottom middle
        seen = set()
        for i in range(6, 9):
            for j in range(3, 6):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        # Box 9: bottom right
        seen = set()
        for i in range(6, 9):
            for j in range(6, 9):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])

        return True