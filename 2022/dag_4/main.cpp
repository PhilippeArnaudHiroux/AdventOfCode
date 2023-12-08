#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

using namespace std;
void deel_1();
void deel_2();

int main()
{
    //deel_1();
    deel_2();

    return 0;
}

void deel_1()
{
    string file  = "input.txt";
    ifstream myfile; myfile.open(file);
    string str, str1, str2, str11, str12, str21, str22;
    int size_str, size_str1, size_str2 = 0;
    int z, j, score = 0;
    int getal11, getal12, getal21, getal22 = 0;

    for(int j=0; j<1000; j++)
    {
        getline(myfile, str);
        cout << str << endl;
        size_str = str.length();

        for(int i=0; i<size_str; i++) //str opsplitsen in linker (str1) en rechter (str2) kant
        {
            if(str[i] != ',' and z == 0)
            {
                str1 = str1 + str[i];
            }
            else
            {
                z = 1;
                if(str[i] != ',')
                {

                    str2 = str2 + str[i];
                }
            }
        }
        z = 0;

        size_str1 = str1.length();
        size_str2 = str2.length();

        for(int i=0; i<size_str1; i++) //str opsplitsen in linker (str11) en rechter (str12) kant
        {
            if(str1[i] != '-' and z == 0)
            {
                str11 = str11 + str1[i];
            }
            else
            {
                z = 1;
                str12 = str12 + str1[i+1];
            }
        }
        z = 0;

        for(int i=0; i<size_str2; i++) //str opsplitsen in linker (str21) en rechter (str22) kant
        {
            if(str2[i] != '-' and z == 0)
            {
                str21 = str21 + str2[i];
            }
            else
            {
                z = 1;
                str22 = str22 + str2[i+1];
            }
        }
        z = 0;

        cout << "str1 -> " << str1 << " en str2 -> " << str2 << endl;

        cout << "str11 -> " << str11  << " en str12 -> " << str12 << endl;
        cout << "str21 -> " << str21 << " en str22 -> " << str22 << endl;

        getal11 = stoi(str11);
        getal12 = stoi(str12);
        getal21 = stoi(str21);
        getal22 = stoi(str22);

        if(getal11 >= getal21 and getal12 <= getal22) //str1 in str2
        {
            score++;
            cout << "***** SCORE 1 ***** " << score << endl;
        }
        /*else if(str21 >= str11 and str22 <= str12)
        {
            score++;
            cout << "***** SCORE 2 ***** " << score << endl;
        }*/
        else if(getal11 <= getal21 and getal12 >= getal22) //str2 in str1
        {
            score++;
            cout << "***** SCORE 2 ***** " << score << endl;
        }
        /*else
        {
            cout << "***** NIET *****" << endl;
        }*/

        str1.clear();
        str2.clear();
        str11.clear();
        str12.clear();
        str21.clear();
        str22.clear();
    }

    cout << "SCOREN -> " << score << endl;
}

void deel_2()
{
    string file  = "input.txt";
    ifstream myfile; myfile.open(file);
    string str, str1, str2, str11, str12, str21, str22;
    int size_str, size_str1, size_str2 = 0;
    int z, j, score, eind_score = 0;
    int a = 0;
    int getal11, getal12, getal21, getal22 = 0;

    for(int j=0; j<1000; j++)
    {
        getline(myfile, str);
        cout << str << endl;
        size_str = str.length();

        for(int i=0; i<size_str; i++) //str opsplitsen in linker (str1) en rechter (str2) kant
        {
            if(str[i] != ',' and z == 0)
            {
                str1 = str1 + str[i];
            }
            else
            {
                z = 1;
                if(str[i] != ',')
                {

                    str2 = str2 + str[i];
                }
            }
        }
        z = 0;

        size_str1 = str1.length();
        size_str2 = str2.length();

        for(int i=0; i<size_str1; i++) //str opsplitsen in linker (str11) en rechter (str12) kant
        {
            if(str1[i] != '-' and z == 0)
            {
                str11 = str11 + str1[i];
            }
            else
            {
                z = 1;
                str12 = str12 + str1[i+1];
            }
        }
        z = 0;

        for(int i=0; i<size_str2; i++) //str opsplitsen in linker (str21) en rechter (str22) kant
        {
            if(str2[i] != '-' and z == 0)
            {
                str21 = str21 + str2[i];
            }
            else
            {
                z = 1;
                str22 = str22 + str2[i+1];
            }
        }
        z = 0;

        cout << "str1 -> " << str1 << " en str2 -> " << str2 << endl;

        cout << "str11 -> " << str11  << " en str12 -> " << str12 << endl;
        cout << "str21 -> " << str21 << " en str22 -> " << str22 << endl;

        getal11 = stoi(str11);
        getal12 = stoi(str12);
        getal21 = stoi(str21);
        getal22 = stoi(str22);

        //------------------------------------------------------------------------------------------

        if(getal11 < getal21 and getal12 < getal22 and getal12 < getal21)
        {
            score++;
            cout << "**** SCORE 1 ****" << endl;
        }
        else if(getal11 > getal21 and getal12 > getal22 and getal11 > getal22)
        {
            score++;
            cout << "**** SCORE 2 ****" << endl;
        }


        //--------------------------------------------------------------------------------------------------
        str1.clear();
        str2.clear();
        str11.clear();
        str12.clear();
        str21.clear();
        str22.clear();
    }

    eind_score = 1000 - score;
    cout << "SCOREN -> " << eind_score << endl;
}
