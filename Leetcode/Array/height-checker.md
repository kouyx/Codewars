# 1051. 高度检查器

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/height-checker)

## 题目描述

学校在拍年度纪念照时，一般要求学生按照 **非递减** 的高度顺序排列。

请你返回至少有多少个学生没有站在正确位置数量。该人数指的是：能让所有学生以 **非递减** 高度排列的必要移动人数。

示例：

输入：`[1,1,4,2,1,3]`
输出：`3`
解释：
高度为 `4`、`3` 和最后一个 `1` 的学生，没有站在正确的位置。

提示：

1. `1 <= heights.length <= 100`
2. `1 <= heights[i] <= 100`

## 题解

### 排序比较

比较排序前后的数组，站错位置的人数即排序前后的不相同的人数。

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a,b in zip(sorted(heights), heights))
```

```java
import java.util.Arrays;

class Solution {
    public int heightChecker(int[] heights) {
        int[] org = heights.clone();
        Arrays.sort(heights);
        int res = 0;
        for (int i = 0; i < heights.length; i++) {
            if (org[i] != heights[i]) {
                res++;
            }
        }
        return res;
    }
}
```

- 时间复杂度：$O(NlogN)$ 快速排序；
- 空间复杂度：$O(N)$

### 计数

启发于 [holy-sword 的题解](https://leetcode-cn.com/problems/height-checker/solution/onjie-fa-yong-shi-yu-nei-cun-ji-bai-100-javayong-h/)

其实排序后得到的结果并不重要，只需要知道在该位置上与最小的值是否一致。所以仅仅需要计数而已。

```java
class Solution {
    public int heightChecker(int[] heights) {
        int[] arr = new int[101]; // heights[i] 取值范围 [1, 100]
        for (int ht : heights) {
            arr[ht]++;
        }
        int res = 0, i = 0, j = 0;
        while (i < heights.length) {
            while (arr[j] == 0 && j <= 100) {
                j++;
            }
            if (j != heights[i]) {
                res++;
            }
            i++;
            arr[j]--;
        }
        return res;
    }
}
```

```python
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = [0] * 101
        for ht in heights:
            arr[ht] += 1
        res = i = j = 0
        while i < len(heights):
            while arr[j] == 0 and j <= 100:
                j += 1
            if j != heights[i]:
                res += 1
            i += 1
            arr[j] -= 1
        return res
```

- 时间复杂度：$O(N)$；
- 空间复杂度：$O(1)$
