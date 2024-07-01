#include <string>
#include <iostream>
using namespace std;

 string mergeAlternately(string word1, string word2)
    {
       std::string word3 = "";
       int larger = max(word1.length(), word2.length());

        for(int i = 0; i < larger; i++){

            if(i < word1.length()){
                word3 +=word1[i];
            }
            if(i < word2.length()){
                word3 += word2[i];
            }


        }
        return word3;


    };


int main() {
    cout << mergeAlternately("abc","qr");
   
    return 0;
};


