class Solution {
    public static int search1(int[] arr, int start, int end, int target) {
        int mid = (start + end)/2;
        if (start > end) 
            return -1; 
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] > target) {
            return search1(arr, start, mid - 1, target);
        } else {
            return search1(arr, mid + 1, end, target);
        }
    
    }

    public static int search(int[] nums, int search) { 
        return search1(nums, 0, nums.length - 1, search);
    }
}