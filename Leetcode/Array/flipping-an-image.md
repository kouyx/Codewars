# 832. 翻转图像

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/flipping-an-image)

## 题目描述

给定一个二进制矩阵 `A`，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 `[1, 1, 0]` 的结果是 `[0, 1, 1]`。

反转图片的意思是图片中的 `0` 全部被 `1` 替换， `1` 全部被 `0` 替换。例如，反转 `[0, 1, 1]` 的结果是 `[1, 0, 0]`。

## 题解

### 模拟

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i].reverse()

        return [[0 if x == 1 else 1 for x in r] for r in A]
```

```java
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int ln = A.length;
        for (int i = 0; i < ln; i++) {
            for (int lft = 0, rt = ln - 1;lft < rt; lft++, rt--) {
                int tmp = A[i][rt];
                A[i][rt] = A[i][lft];
                A[i][lft] = tmp;
            }
        }

        for (int i = 0; i < ln; i++) {
            for (int j = 0; j < ln; j++) {
                A[i][j] = A[i][j] == 1 ? 0 : 1;
            }
        }
        return A;
    }
}
```

- 时间复杂度：$O(N^2)$
- 空间复杂度：原矩阵直接修改则 $O(1)$，返回新矩阵则 $O(N^2)$. Python3 测试列表生成表达式与原矩阵修改在内存消耗上无区别。
