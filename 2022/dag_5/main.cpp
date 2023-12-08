#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>

#define AANTAL 503
//#define AANTAL 4

using namespace std;

void deel_1();

int main()
{
    deel_1();

    return 0;
}

void deel_1()
{
    string file1 = "input.txt"; //Move
    int a, b, c = 0;
    ifstream myfile1; myfile1.open(file1); //Move
    string str;

    /*
    vector <string> rij_1 = {"Z", "N"};
    vector <string> rij_2 = {"M", "C", "D"};
    vector <string> rij_3 = {"P"};
    */

    vector <string> rij_1 = {"W", "R", "F"};
    vector <string> rij_2 = {"T", "H", "M", "C", "D", "V", "W", "P"};
    vector <string> rij_3 = {"P", "M", "Z", "N", "L"};
    vector <string> rij_4 = {"J", "C", "H", "R"};
    vector <string> rij_5 = {"C", "P", "G", "H", "Q", "T", "B"};
    vector <string> rij_6 = {"G", "C", "W", "L", "F", "Z"};
    vector <string> rij_7 = {"W", "V", "L", "Q", "Z", "J", "G", "C"};
    vector <string> rij_8 = {"P", "N", "R", "F", "W", "T", "V", "C"};
    vector <string> rij_9 = {"J", "W", "H", "G", "R", "S", "V"};


/*
8     [P]                 [C] [C]
7     [W]         [B]     [G] [V] [V]
6     [V]         [T] [Z] [J] [T] [S]
5     [D] [L]     [Q] [F] [Z] [W] [R]
4     [C] [N] [R] [H] [L] [Q] [F] [G]
3 [F] [M] [Z] [H] [G] [W] [L] [R] [H]
2 [R] [H] [M] [C] [P] [C] [V] [N] [W]
1 [W] [T] [P] [J] [C] [G] [W] [P] [J]
     1   2   3   4   5   6   7   8   9
*/

    vector <int> move;
    vector <int> van;
    vector <int> naar;

    vector <string> str_van;
    vector <string> str_naar;
    vector <string> tijdelijk;

    while (getline(myfile1, str))
    {
        sscanf_s(str.c_str(), "move %d from %d to %d", &a  , &b , &c);
        move.push_back(a);
        van.push_back(b);
        naar.push_back(c);
    }


    for(int i=0; i<AANTAL; i++)
    {
        if(van.at(i) == 1){str_van = rij_1;}
        else if(van.at(i) == 2){str_van = rij_2;}
        else if(van.at(i) == 3){str_van = rij_3;}
        else if(van.at(i) == 4){str_van = rij_4;}
        else if(van.at(i) == 5){str_van = rij_5;}
        else if(van.at(i) == 6){str_van = rij_6;}
        else if(van.at(i) == 7){str_van = rij_7;}
        else if(van.at(i) == 8){str_van = rij_8;}
        else if(van.at(i) == 9){str_van = rij_9;}

        if(naar.at(i) == 1){str_naar = rij_1;}
        else if(naar.at(i) == 2){str_naar = rij_2;}
        else if(naar.at(i) == 3){str_naar = rij_3;}
        else if(naar.at(i) == 4){str_naar = rij_4;}
        else if(naar.at(i) == 5){str_naar = rij_5;}
        else if(naar.at(i) == 6){str_naar = rij_6;}
        else if(naar.at(i) == 7){str_naar = rij_7;}
        else if(naar.at(i) == 8){str_naar = rij_8;}
        else if(naar.at(i) == 9){str_naar = rij_9;}

        for(int j=0; j<move.at(i); j++)
        {
            tijdelijk.push_back(str_van.back());
            str_van.pop_back();
        }

        for(int j=0; j<move.at(i); j++)
        {
            str_naar.push_back(tijdelijk.back());
            tijdelijk.pop_back();
        }

        if(van.at(i) == 1){rij_1 = str_van;}
        else if(van.at(i) == 2){rij_2 = str_van;}
        else if(van.at(i) == 3){rij_3 = str_van;}
        else if(van.at(i) == 4){rij_4 = str_van;}
        else if(van.at(i) == 5){rij_5 = str_van;}
        else if(van.at(i) == 6){rij_6 = str_van;}
        else if(van.at(i) == 7){rij_7 = str_van;}
        else if(van.at(i) == 8){rij_8 = str_van;}
        else if(van.at(i) == 9){rij_9 = str_van;}

        if(naar.at(i) == 1){rij_1 = str_naar;}
        else if(naar.at(i) == 2){rij_2 = str_naar;}
        else if(naar.at(i) == 3){rij_3 = str_naar;}
        else if(naar.at(i) == 4){rij_4 = str_naar;}
        else if(naar.at(i) == 5){rij_5 = str_naar;}
        else if(naar.at(i) == 6){rij_6 = str_naar;}
        else if(naar.at(i) == 7){rij_7 = str_naar;}
        else if(naar.at(i) == 8){rij_8 = str_naar;}
        else if(naar.at(i) == 9){rij_9 = str_naar;}
    }

    cout << rij_1.back() << rij_2.back() << rij_3.back() << rij_4.back() << rij_5.back() << rij_6.back() << rij_7.back() << rij_8.back() << rij_9.back() << endl;

}
