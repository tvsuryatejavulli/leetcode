class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        
        for (int row = n - 2; row >= 0; row--) {
            for (int col = 0; col < triangle.get(row).size(); col++) {
                triangle.get(row).set(col, triangle.get(row).get(col) +
                    Math.min(triangle.get(row + 1).get(col), triangle.get(row + 1).get(col + 1)));
            }
        }
        
        return triangle.get(0).get(0);
    }
}
