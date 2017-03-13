#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;


class Character {
    private:
        vector<string> lines;
    public:
        void addLine(string line){
            lines.push_back(line);
        }

        string getLine(int index){
            return lines[index];
        }
};


int main()
{
    int L;
    cin >> L; cin.ignore();
    int H;
    cin >> H; cin.ignore();
    string T;
    getline(cin, T);

    transform(T.begin(),T.end(),T.begin(),ptr_fun<int,int>(toupper));

    map<char,Character> characters;

    for (int i = 0; i < H; i++) {
        string ROW;
        getline(cin, ROW);
        for(int j = 0; j < 27; j++){
            if(j == 26){
                characters[63].addLine(ROW.substr(L*j,L));
            } else {
                characters[j+65].addLine(ROW.substr(L*j,L));
            }
        } 
    }

    for(int i = 0; i < H; i++){
        for(int j = 0; j < T.length(); j++){
            if(T[j] < 65 || T[j] > 90){
                cout << characters[63].getLine(i);
            } else {
                cout << characters[T[j]].getLine(i);
            }
        }
        cout << endl;
    }
}