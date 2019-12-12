# 1252. 奇数值单元格的数目

来源：[力扣（LeetCode）](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix)

## 题目

给你一个 `n` 行 `m` 列的矩阵，最开始的时候，每个单元格中的值都是 `0`。

另有一个索引数组 `indices`，`indices[i] = [ri, ci]` 中的 `ri` 和 `ci` 分别表示指定的行和列（从 `0` 开始编号）。

你需要将每对 `[ri, ci]` 指定的行和列上的所有单元格的值加 `1`。

请你在执行完所有 `indices` 指定的增量操作后，返回矩阵中 「奇数值单元格」 的数目。

## 解题

启发于 [Shuxin Chen 的题解](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix/solution/ti-jie-1252-qi-shu-zhi-dan-yuan-ge-de-shu-mu-by-ze/)

### 模拟

```java
class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int[][] mtx = new int[n][m];
        for (int[] idx : indices) {
            int ri = idx[0], ci = idx[1];
            for (int i = 0; i < n; i++) {
                mtx[i][ci] += 1;
            }
            for (int i = 0; i < m; i++) {
                mtx[ri][i] += 1;
            }
        }

        int res = 0;
        for (int[] rs : mtx) {
            for (int x : rs) {
                res += x % 2;
            }
        }
        return res;
    }
}
```

```python
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mtx = [[0] * m for _ in range(n)]
        for (x, y) in indices:
            for i in range(m):
                mtx[x][i] += 1

            for i in range(n):
                mtx[i][y] += 1
        return sum(ele % 2 for r in mtx for ele in r)

```

- 时间复杂度：$O(L(M+N)+MN)$，其中 $L$ 是 `indices` 数组的长度。
- 空间复杂度：$O(MN)$。

### 模拟 + 空间优化

使用一个行数组 `rows` 和列数组 `cols` 分别记录每一行和每一列被增加的次数。对于 `indices` 中的每一对 `[ri, ci]`，将 `rows[ri]` 和 `cols[ci]` 的值分别增加 `1`。

在所有操作模拟完毕后，矩阵中位于 `(x, y)` 位置的数即为 `rows[x] + cols[y]`。遍历矩阵，对 2 取余求和得到奇数的数目。

```java
class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int[] rows = new int[n];
        int[] cols = new int[m];
        for (int[] idx : indices) {
            rows[idx[0]] += 1;
            cols[idx[1]] += 1;
        }

        int res = 0;
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < m; c++) {
                res += (rows[r] + cols[c]) % 2;
            }
        }
        return res;
    }
}
```

```python
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for (x, y) in indices:
            rows[x] += 1
            cols[y] += 1

        return sum((x + y) % 2 for x in rows for y in cols)
```

- 时间复杂度：$O(L+MN)$，其中 $L$ 是 `indices` 数组的长度。
- 空间复杂度：$O(M + N)$。

### 计数

继续对方法二进行优化。可以发现，矩阵中位于 `(x, y)` 位置的数为奇数，当且仅当 `rows[x]` 和 `cols[y]` 中恰好有一个为奇数。因此

- 对于 `rows[x]` 为偶数，那么在矩阵第 `x` 行有 `count_odd(cols)` 个奇数
- 对于 `rows[x]` 为奇数，那么在矩阵第 `x` 行有 `m - count_odd(cols)` 个偶数

其中 `count_odd(cols)` 表示数组 `cols` 中奇数的个数。将所有的行进行求和，可以得到奇数的数目为 `count_odd(rows) * (m - count_odd(cols)) + (n - count_odd(rows)) * count_odd(cols)`。

```java
class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int[] rows = new int[n];
        int[] cols = new int[m];
        for (int[] idx : indices) {
            rows[idx[0]] += 1;
            cols[idx[1]] += 1;
        }

        int ro = 0, co = 0;
        for (int r: rows) {
            ro += r % 2;
        }
        for (int c: cols) {
            co += c % 2;
        }
        return ro * (m - co) + (n - ro) * co;
    }
}
```

```python
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [0] * n
        cols = [0] * m
        for (x, y) in indices:
            rows[x] += 1
            cols[y] += 1

        ro = sum(x % 2 for x in rows)
        co = sum(x % 2 for x in cols)

        return ro * (m - co) + (n - ro) * co
```

- 时间复杂度：$O(L+M+N)$，其中 $L$ 是 `indices` 数组的长度。
- 空间复杂度：$O(M + N)$。
