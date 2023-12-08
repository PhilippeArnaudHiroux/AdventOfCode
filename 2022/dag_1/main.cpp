#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    string filename  = "input.txt";
    ifstream myfile; myfile.open(filename);
    vector<int> lijst;

    string line;   // To read each line from code

    while (getline(myfile, line))
    {
        int a{};

        while (!line.empty())
        {
            int value;
            value = stoi(line);
            a = a + value;

            if (!getline(myfile, line))
            {
                break;
            }
        }

        lijst.push_back(a);
    }

    cout << "Maximum element = " << *max_element(lijst.begin(), lijst.end()) << endl;

    sort(lijst.begin(), lijst.end(), greater<int>());
    cout<<"uitkomst "<< lijst.at(0) + lijst.at(1) + lijst.at(2) << endl;

    return 0;
}
