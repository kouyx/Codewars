/**
 * 169. 多数元素 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
 * 
 * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 * 
 * 示例 1：
 * 
 * 输入：[3,2,3] 输出：3 示例 2：
 * 
 * 输入：[2,2,1,1,1,2,2] 输出：2
 * 
 * 进阶：
 * 
 * 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
 */
class Solution1 {
    public int majorityElement(int[] nums) {
        return majorityElement(nums, 0, nums.length - 1);
    }

    private int majorityElement(int[] nums, int lo, int hi) {
        if (hi == lo) {
            return nums[lo];
        }
        int mid = (lo >> 1) + (hi >> 1);
        int left = majorityElement(nums, lo, mid);
        int right = majorityElement(nums, mid + 1, hi);
        if (left == right) {
            return left;
        }
        int leftCnt = countInRange(nums, lo, mid, left);
        int rightCnt = countInRange(nums, mid + 1, hi, right);
        return leftCnt > rightCnt ? left : right;
    }

    private int countInRange(int[] nums, int lo, int hi, int target) {
        int cnt = 0;
        for (int i = lo; i < hi; i++) {
            if (nums[i] == target) {
                cnt++;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        BoyerMooreSolution solu = new BoyerMooreSolution();
        int[] nums = { 3, 2, 3 };
        System.out.println(solu.majorityElement(nums));
        nums = new int[] { 2, 2, 1, 1, 1, 2, 2 };
        System.out.println(solu.majorityElement(nums));
    }
}

class BoyerMooreSolution {
    public int majorityElement(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int count = 0;
        int candidate = 0;
        for (int x : nums) {
            if (count == 0) {
                candidate = x;
            }
            count += x == candidate ? 1 : -1;
        }
        return candidate;
    }
}