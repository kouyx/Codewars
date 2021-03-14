/**
 * 240. 搜索二维矩阵 II 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
 * 
 * 每行的元素从左到右升序排列。 每列的元素从上到下升序排列。
 * 
 * 
 * 示例 1：
 * 
 * 
 * 输入：matrix =
 * [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
 * target = 5 输出：true 示例 2：
 * 
 * 
 * 输入：matrix =
 * [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
 * target = 20 输出：false
 * 
 * 
 * 提示：
 * 
 * m == matrix.length n == matrix[i].length 1 <= n, m <= 300 -109 <= matix[i][j]
 * <= 109 每行的所有元素从左到右升序排列 每列的所有元素从上到下升序排列 -109 <= target <= 109
 */
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null) {
            return false;
        }
        for (int col = 0, row = matrix.length - 1; row >= 0 && col <= matrix[0].length - 1;) {
            if (matrix[row][col] > target) {
                row--;
            } else if (matrix[row][col] < target) {
                col++;
            } else {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solu = new Solution();
        int[][] matrix = { { 1, 4, 7, 11, 15 }, { 2, 5, 8, 12, 19 }, { 3, 6, 9, 16, 22 }, { 10, 13, 14, 17, 24 },
                { 18, 21, 23, 26, 30 } };
        System.out.println(solu.searchMatrix(matrix, 5));
        System.out.println(solu.searchMatrix(matrix, 20));
        matrix = null;
        System.out.println(solu.searchMatrix(matrix, 20));
        matrix = new int[0][0];
        System.out.println(solu.searchMatrix(matrix, 20));
    }
}

/**
 * 
 * 作者：LeetCode
 * 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
 * 来源：力扣（LeetCode） 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 */
class BinarySearchSolution {
    private boolean binarySearch(int[][] matrix, int target, int start, boolean vertical) {
        int lo = start;
        int hi = vertical ? matrix[0].length - 1 : matrix.length - 1;

        while (hi >= lo) {
            int mid = (lo + hi) / 2;
            if (vertical) { // searching a column
                if (matrix[start][mid] < target) {
                    lo = mid + 1;
                } else if (matrix[start][mid] > target) {
                    hi = mid - 1;
                } else {
                    return true;
                }
            } else { // searching a row
                if (matrix[mid][start] < target) {
                    lo = mid + 1;
                } else if (matrix[mid][start] > target) {
                    hi = mid - 1;
                } else {
                    return true;
                }
            }
        }

        return false;
    }

    public boolean searchMatrix(int[][] matrix, int target) {
        // an empty matrix obviously does not contain `target`
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        // iterate over matrix diagonals
        int shorterDim = Math.min(matrix.length, matrix[0].length);
        for (int i = 0; i < shorterDim; i++) {
            boolean verticalFound = binarySearch(matrix, target, i, true);
            boolean horizontalFound = binarySearch(matrix, target, i, false);
            if (verticalFound || horizontalFound) {
                return true;
            }
        }
        return false;
    }
}

/**
 * 
 * 作者：LeetCode
 * 链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/
 * 来源：力扣（LeetCode） 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 */
class Solution {
    private int[][] matrix;
    private int target;

    private boolean searchRec(int left, int up, int right, int down) {
        // this submatrix has no height or no width.
        if (left > right || up > down) {
            return false;
        } else if (target < matrix[up][left] || target > matrix[down][right]) {
            // `target` is already larger than the largest element or smaller
            // than the smallest element in this submatrix.
            return false;
        }

        int mid = left + (right - left) / 2;

        // Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
        int row = up;
        while (row <= down && matrix[row][mid] <= target) {
            if (matrix[row][mid] == target) {
                return true;
            }
            row++;
        }

        return searchRec(left, row, mid - 1, down) || searchRec(mid + 1, up, right, row - 1);
    }

    public boolean searchMatrix(int[][] mat, int targ) {
        // cache input values in object to avoid passing them unnecessarily
        // to `searchRec`
        matrix = mat;
        target = targ;

        // an empty matrix obviously does not contain `target`
        if (matrix == null || matrix.length == 0) {
            return false;
        }

        return searchRec(0, 0, matrix[0].length - 1, matrix.length - 1);
    }
}
