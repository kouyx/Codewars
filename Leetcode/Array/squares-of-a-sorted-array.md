# 977. 有序数组的平方

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/squares-of-a-sorted-array)

## 题目描述

给定一个按非递减顺序排序的整数数组 `A`，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：

输入：`[-4,-1,0,3,10]`
输出：`[0,1,9,16,100]`

示例 2：

输入：`[-7,-3,2,3,11]`
输出：`[4,9,9,49,121]`

提示：

1. `1 <= A.length <= 10000`
1. `-10000 <= A[i] <= 10000`
1. `A` 已按非递减顺序排序。

## 题解

### 先平方后排序

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x ** 2 for x in A)
```

```java
class Solution {
    public int[] sortedSquares(int[] A) {
        for (int i = 0; i < A.length; i++) {
            A[i] = A[i] * A[i];
        }
        Arrays.sort(A);
        return A;
    }
}
```

- 时间复杂度：$O(NlogN)$
- 空间复杂度：$O(N)$

### 头尾双指针

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lft = 0
        n = rt = len(A) - 1
        res = [0] * len(A)
        aa, bb = A[lft] ** 2, A[rt] ** 2
        while lft < rt:
            if aa > bb:
                res[n] = aa
                lft += 1
                aa = A[lft] ** 2
            else:
                res[n] = bb
                rt -= 1
                bb = A[rt] ** 2
            n -= 1
        res[0] = A[lft] ** 2
        return res
```

```java
class Solution {
    public int[] sortedSquares(int[] A) {
        int lft = 0, n = A.length - 1, rt = A.length - 1;
        int[] res = new int[A.length];
        int aa = A[lft] * A[lft], bb = A[rt] * A[rt];
        while (lft < rt) {
            if (aa > bb) {
                res[n] = aa;
                lft++;
                aa = A[lft] * A[lft];
            } else {
                res[n] = bb;
                rt--;
                bb = A[rt] * A[rt];
            }
            n--;
        }
        res[0] = A[lft] * A[lft];
        return res;
    }
}```

- 时间复杂度：$O(N)$
- 空间复杂度：$O(N)$
