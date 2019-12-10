# 1266. 访问所有点的最小时间

## 题目

平面上有 `n` 个点，点的位置用整数坐标表示 `points[i] = [xi, yi]`。请你计算访问所有这些点需要的最小时间（以秒为单位）。

你可以按照下面的规则在平面上移动：

每一秒沿水平或者竖直方向移动一个单位长度，或者跨过对角线（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
必须按照数组中出现的顺序来访问这些点。

## 解题

关键在于求切比雪夫距离，即两个点的横纵坐标距离的较大值。

## 实现

```python
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        x0, y0 = points[0]
        for [x, y] in points[1:]:
            res += max(abs(x-x0), abs(y-y0))
            x0, y0 = x, y
        return res
```

```java
class Solution {
    public int minTimeToVisitAllPoints(int[][] points) {
        int res = 0;
        for (int i = 1; i < points.length; i++) {
            res += distanceBetweenPoints(points[i - 1], points[i]);
        }
        return res;
    }

    private int distanceBetweenPoints(int[] point1, int[] point2) {
        return Math.max(Math.abs(point1[0] - point2[0]),
                Math.abs(point1[1] - point2[1]));
    }
}
```
