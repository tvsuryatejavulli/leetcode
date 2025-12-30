class Solution {
    // Grid dimensions
    private int rows;
    private int cols;
    private int[][] grid;

    /**
     * Counts the number of 3x3 magic squares in the grid.
     * A magic square is a 3x3 grid containing distinct numbers from 1 to 9
     * where all rows, columns, and diagonals sum to the same value (15).
     * 
     * @param grid The input 2D grid
     * @return The count of valid 3x3 magic squares
     */
    public int numMagicSquaresInside(int[][] grid) {
        this.rows = grid.length;
        this.cols = grid[0].length;
        this.grid = grid;
      
        int count = 0;
      
        // Check every possible 3x3 subgrid starting position
        for (int row = 0; row < rows; ++row) {
            for (int col = 0; col < cols; ++col) {
                count += checkMagicSquare(row, col);
            }
        }
      
        return count;
    }

    /**
     * Checks if a 3x3 subgrid starting at position (startRow, startCol) is a magic square.
     * 
     * @param startRow The starting row index of the 3x3 subgrid
     * @param startCol The starting column index of the 3x3 subgrid
     * @return 1 if the subgrid is a magic square, 0 otherwise
     */
    private int checkMagicSquare(int startRow, int startCol) {
        // Check if 3x3 subgrid fits within bounds
        if (startRow + 3 > rows || startCol + 3 > cols) {
            return 0;
        }
      
        // Track frequency of numbers (index 1-9 used, others ignored)
        int[] frequency = new int[16];
      
        // Store sum of each row and column
        int[] rowSums = new int[3];
        int[] colSums = new int[3];
      
        // Store diagonal sums
        int mainDiagonalSum = 0;  // Top-left to bottom-right
        int antiDiagonalSum = 0;  // Top-right to bottom-left
      
        // Process each cell in the 3x3 subgrid
        for (int row = startRow; row < startRow + 3; ++row) {
            for (int col = startCol; col < startCol + 3; ++col) {
                int value = grid[row][col];
              
                // Validate: number must be 1-9 and appear exactly once
                if (value < 1 || value > 9 || ++frequency[value] > 1) {
                    return 0;
                }
              
                // Calculate relative position within 3x3 subgrid
                int relativeRow = row - startRow;
                int relativeCol = col - startCol;
              
                // Add to row and column sums
                rowSums[relativeRow] += value;
                colSums[relativeCol] += value;
              
                // Check if on main diagonal (top-left to bottom-right)
                if (relativeRow == relativeCol) {
                    mainDiagonalSum += value;
                }
              
                // Check if on anti-diagonal (top-right to bottom-left)
                if (relativeRow + relativeCol == 2) {
                    antiDiagonalSum += value;
                }
            }
        }
      
        // Both diagonals must have equal sums
        if (mainDiagonalSum != antiDiagonalSum) {
            return 0;
        }
      
        // All rows and columns must have the same sum as the diagonals
        for (int i = 0; i < 3; ++i) {
            if (rowSums[i] != mainDiagonalSum || colSums[i] != mainDiagonalSum) {
                return 0;
            }
        }
      
        // All conditions satisfied - this is a magic square
        return 1;
    }
}