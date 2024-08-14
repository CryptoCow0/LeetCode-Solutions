class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        //okay so we want to make a set and compare if the number in the set is greater or smaller?
    vector<bool> Answers;
    size_t max = candies.at(0);

    for(size_t i = 0; i < candies.size(); i++){
        if (candies.at(i) > max){
            max = candies.at(i);
        }
    }


    for(size_t i = 0; i < candies.size(); i++){

        if(max <= (candies.at(i) + extraCandies)){
            //max = candies.at(i) + extraCandies;
            Answers.push_back(true);
        }
        else{
            Answers.push_back(false);
        }
    }

    return Answers;

    }
};