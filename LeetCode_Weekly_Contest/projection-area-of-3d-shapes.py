"""
weekly-contest-96 (4)

projection-area-of-3d-shapes

在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。

每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。

现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。

投影就像影子，将三维形体映射到一个二维平面上。

在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回所有三个投影的总面积。

提示：

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50

输入：[[2]]
输出：5

输入：[[1,2],[3,4]]
输出：17

输入：[[1,0],[0,2]]
输出：8

输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：14

输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：21

"""


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
