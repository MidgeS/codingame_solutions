#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;


class Defibrillator {

    private:
        string name;
        float longitude;
        float latitude;
        int id;
    public:
        string address;
        string phone;
        static const float earthRadius;

    Defibrillator(int id,string name,float longitude,float latitude){
        this->name = name;
        this->longitude = longitude;
        this->latitude = latitude;
        this->id = id;
    }

    float distanceTo(float longitude, float latitude){
        float x = (this->longitude - longitude) * cos((latitude + this->latitude) / 2);
        float y = this->latitude - latitude;
        return sqrt(x*x + y*y) * earthRadius;
    }

    string getName(){
        return name;
    }
};

const float Defibrillator::earthRadius = 6371.0f;


class Converter {
    public:
        static float stringToFloat(string str){
            while(str.find(",") != string::npos){
                int pos = str.find(",");
                str.replace(pos,1,".");
            }
            return stof(str);
        }

        static Defibrillator lineToDefibrillator(string line){
            vector<string> elements;
            stringstream stream;
            stream.str(line);
            string item;
            while(getline(stream,item,';')){
                elements.push_back(item);
            }
            Defibrillator defi(stoi(elements[0]),elements[1],Converter::stringToFloat(elements[4]),Converter::stringToFloat(elements[5]));
            defi.address = elements[2];
            defi.phone = elements[3];

            return defi;
        }
};


int main()
{
    string LON;
    cin >> LON; cin.ignore();
    float userLongitude = Converter::stringToFloat(LON);
    cerr << "userLongitude: " << userLongitude << endl;

    string LAT;
    cin >> LAT; cin.ignore();
    float userLatitude = Converter::stringToFloat(LAT);
    cerr << "userLatitude: " << userLatitude << endl;

    int N;
    cin >> N; cin.ignore();
    vector<Defibrillator> defis;
    for (int i = 0; i < N; i++) {
        string DEFIB;
        getline(cin, DEFIB);
        defis.push_back(Converter::lineToDefibrillator(DEFIB));
    }

    float distance = numeric_limits<float>::max();
    int index = 0;
    for(int i = 0; i < defis.size(); i++){
        float dist = defis[i].distanceTo(userLongitude,userLatitude);
        if(distance > dist){
            distance = dist;
            index = i;
        }
    }

    cerr << index << ": " << distance << endl;
    cout << defis[index].getName() << endl;
}