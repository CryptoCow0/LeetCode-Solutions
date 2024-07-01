#include <iostream>
#include <regex>
#include <algorithm>

using namespace std;


string gcdOfString(string str1, string str2){
string final = "";
string pattern_str = "";
for(char c:str1){

 pattern_str += c;

regex pattern(pattern_str);

if (regex_search(str2, pattern)){
    
    final = pattern_str;
        std::string result = gcdOfString(str1, str2);


}

}

//check if this 



return final;


}

int main(){
cout << gcdOfString("ABABAB","ABAB");
    return 0;
}