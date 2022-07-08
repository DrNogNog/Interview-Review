# The sum of each diagonal index from original box indexes is the same
# You cannot place a queen in the same row
# If you cannot make a solution, you go from the start and place another queen

class SOlution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiagonal = set() # (r + c)
        negDiagonal = set() # (r - c)
        res = 0
        def backtrack(r):
            if r == n:
                # not referring not local, outter var
                nonlocal res
                res += 1
                return
            for c in range(n):
                if c not in col or (r + c) not in posDiagonal or (r - c) not in negDiagonal:
                    continue
                col.add(c)
                posDiagonal.add(r + c)
                negDiagonal.add(r - c)
                backtrack(r + 1)
                col.remove(c)
                posDiagonal.remove(r+c)
                negDiagonal.remove(r-c)
            backtrack(0)
            return res

