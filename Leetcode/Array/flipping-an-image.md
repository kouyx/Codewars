# 832. 翻转图像

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/flipping-an-image)

## 题目描述

给定一个二进制矩阵 `A`，我们想先水平翻转图像，然后反转图像并返回结果。

水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 `[1, 1, 0]` 的结果是 `[0, 1, 1]`。

反转图片的意思是图片中的 `0` 全部被 `1` 替换， `1` 全部被 `0` 替换。例如，反转 `[0, 1, 1]` 的结果是 `[1, 0, 0]`。

## 题解

### 模拟

Python 一行列表生成式：

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if x == 1 else 1 for x in r[::-1]] for r in A]
```

- 时间复杂度：$O(MN)$
- 空间复杂度：$O(N)$，数组切片新建数组；$O(1)$，一般循环解法

$M$, $N$ 分别表示矩阵 `A` 的行数和列数。

```java
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            for (int lft = 0, rt = A[i].length - 1;lft < rt; lft++, rt--) {
                int tmp = A[i][rt];
                A[i][rt] = A[i][lft];
                A[i][lft] = tmp;
            }
        }

        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < A[i].length; j++) {
                A[i][j] = A[i][j] == 1 ? 0 : 1;
            }
        }
        return A;
    }
}
```

### 反转同时翻转

类似双指针从左右同时遍历每一行可以发现：

- 若左右两边的数不同，交换再翻转后与原来相同；
- 若左右两边的数相同，则同时翻转即可。

翻转的方法可以用 `1-` 或者 `1^`，即减法或者**异或**。

Python 语法中从 list 右侧取索引可以用 `A[~i]`，等价于 `A[-1-i] = A[len(A)-1-i]`。注意 `i` 值循环的上限。

```python
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            # 注意以下循环的 range 范围
            for j in range((len(A[i]) + 1) // 2):
                if A[i][j] == A[i][~j]:
                    A[i][j] = A[i][~j] = A[i][j] ^ 1
        return A
```

```java
class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            int lft, rt;
            for (lft = 0, rt = A[i].length - 1;lft < rt; lft++, rt--) {
                if (A[i][rt] == A[i][lft]) {
                    A[i][lft] ^= 1;
                    A[i][rt] ^= 1;
                }
            }
            if (lft == rt) {
                A[i][lft] ^= 1;
            }
        }
        return A;
    }
}
```
