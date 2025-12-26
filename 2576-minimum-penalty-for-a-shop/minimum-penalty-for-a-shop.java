class Solution {
    public int bestClosingTime(String customers) {
        int totalHours = customers.length();
      
        // Create prefix sum array to count 'Y' customers up to each position
        // prefixYCount[i] represents the count of 'Y' customers from index 0 to i-1
        int[] prefixYCount = new int[totalHours + 1];
        for (int i = 0; i < totalHours; ++i) {
            prefixYCount[i + 1] = prefixYCount[i] + (customers.charAt(i) == 'Y' ? 1 : 0);
        }
      
        // Initialize variables to track the best closing hour and minimum penalty
        int bestClosingHour = 0;
        int minimumPenalty = Integer.MAX_VALUE;
      
        // Try each possible closing hour from 0 to totalHours
        for (int closingHour = 0; closingHour <= totalHours; ++closingHour) {
            // Calculate penalty for closing at this hour:
            // - Penalty for 'N' hours when shop is open: closingHour - prefixYCount[closingHour]
            // - Penalty for 'Y' customers after closing: prefixYCount[totalHours] - prefixYCount[closingHour]
            int penaltyForNBeforeClosing = closingHour - prefixYCount[closingHour];
            int penaltyForYAfterClosing = prefixYCount[totalHours] - prefixYCount[closingHour];
            int totalPenalty = penaltyForNBeforeClosing + penaltyForYAfterClosing;
          
            // Update best closing hour if we found a lower penalty
            if (minimumPenalty > totalPenalty) {
                bestClosingHour = closingHour;
                minimumPenalty = totalPenalty;
            }
        }
      
        return bestClosingHour;
    }
}