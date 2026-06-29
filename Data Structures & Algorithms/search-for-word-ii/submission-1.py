class TrieNode:
    def __init__(self):
        self.child = {}
        self.isword = False

    def addword(self, word):
        cur = self
        for c in word:
            if c not in cur.child:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.isword = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addword(w)

        rows = len(board)
        col = len(board[0])
        res, vist = set(), set()

        def dfs(r, c, node, w):

            if (
                r < 0
                or c < 0
                or r == rows
                or c == col
                or board[r][c] not in node.child
                or (r, c) in vist
            ):
                return False

            vist.add((r, c))

            node = node.child[board[r][c]]
            w += board[r][c]
            if node.isword:
                res.add(w)

            dfs(r + 1, c, node, w)
            dfs(r, c + 1, node, w)
            dfs(r - 1, c, node, w)
            dfs(r, c - 1, node, w)

            vist.remove((r, c))
            return res

        for r in range(rows):
            for c in range(col):
                dfs(r, c, root, "")

        return list(res)
