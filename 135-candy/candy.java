import java.util.Arrays;
class Solution {
    public int candy(int[] ratings) {
        int n=ratings.length;
        int allocation[]=new int[n];
        Arrays.fill(allocation,1);

        for(int i=1;i<n;i++){
            if(ratings[i]>ratings[i-1])
                allocation[i]=allocation[i-1]+1;
        }
        for(int i=n-2;i>=0;i--){
            if(ratings[i]>ratings[i+1])
                allocation[i]=Math.max(allocation[i],allocation[i+1]+1);
        }
        int ans=0;
        for(int i=0;i<n;i++){
            ans+=allocation[i];
        }
        return ans;
    }
}