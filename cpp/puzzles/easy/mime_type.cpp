#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;


int main()
{
    int N; // Number of elements which make up the association table.
    cin >> N; cin.ignore();
    int Q; // Number Q of file names to be analyzed.
    cin >> Q; cin.ignore();

    map<string, string> mimes;

    for (int i = 0; i < N; i++) {
        string EXT; // file extension
        string MT; // MIME type.
        cin >> EXT >> MT; cin.ignore();
        transform(EXT.begin(),EXT.end(),EXT.begin(),ptr_fun<int,int>(toupper));
        mimes[EXT] = MT;
    }
    for (int i = 0; i < Q; i++) {
        string FNAME; // One file name per line.
        getline(cin, FNAME);
        int index = FNAME.find_last_of('.');
        if(index > -1){
            string ext = FNAME.substr(index+1,FNAME.length());
            transform(ext.begin(),ext.end(),ext.begin(),ptr_fun<int,int>(toupper));
            if(mimes.find(ext) == mimes.end()){
                cout << "UNKNOWN" << endl;
            } else {
                cout << mimes[ext] << endl;
            }
        } else {
            cout << "UNKNOWN" << endl;
        }
    }
}