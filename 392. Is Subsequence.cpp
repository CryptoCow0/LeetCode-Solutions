#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {

        int left = 0;
        int right= t.size();

        // Hard code
        if(s.size() > right){
            return false;
        }
        else{

            for(int i = 0; i < right; i++){
                
                if(s[left] == t[i]){
                    left++;
                }


            }
        if (left == s.size()){
            return true;
        }



        }

    return false; // here for coding reasons



    }
};