class Solution(object):
    def exist(self, board, word):
        if not board or not word:
            return False

        visited = [[False for i in range(len(board[0]))]for j in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board,word,visited,0,i,j):
                    return True
        return False

    def dfs(self,board,word,visited,current,row,col):
        if current == len(word):
            return True

        if (row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or
                visited[row][col] or word[current] != board[row][col]):
            return False

        visited[row][col] = True
        if self.dfs(board,word,visited,current+1,row+1,col): return True
        if self.dfs(board,word,visited,current+1,row-1,col): return True
        if self.dfs(board,word,visited,current+1,row,col+1): return True
        if self.dfs(board,word,visited,current+1,row,col-1): return True
        visited[row][col] = False
        return False


        