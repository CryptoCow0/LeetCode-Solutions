class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int counter = 0;
        if (n == 0){
            return true;
        }
        for (int i = 0; i < flowerbed.size(); ++i) {
            // Check if the current position is empty and if its neighbors (if any) are also empty
            if (flowerbed[i] == 0 && 
                (i == 0 || flowerbed[i - 1] == 0) && 
                (i == flowerbed.size() - 1 || flowerbed[i + 1] == 0)) {
                
                flowerbed[i] = 1;// for the next time we check
                counter++;
                // Early exit if we have placed enough flowers
                if (counter >= n) {
                    return true;
                }
            
            }
           
        }
        return false;

    }
};