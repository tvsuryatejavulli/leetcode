class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def is_valid_unit(unit):
            unit = [x for x in unit if x != '.']
            return len(unit) == len(set(unit))
        
        def get_box(board, box_index):
            box = []
            row_start = (box_index // 3) * 3
            col_start = (box_index % 3) * 3
            for i in range(3):
                for j in range(3):
                    box.append(board[row_start + i][col_start + j])
            return box
        
        # Check rows
        for row in board:
            if not is_valid_unit(row):
                return False
        
        # Check columns
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        
        # Check 3x3 sub-boxes
        for i in range(9):
            if not is_valid_unit(get_box(board, i)):
                return False
        
        return True
