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
    string str, new_str;
    int controle, size, new_size, score = 0;

    while (getline(myfile, str))
    {
        size = str.length();
        int j = size/2;
        controle = 0;
        do{
            for(int i=0; i<size/2; i++)
            {
                if(str[i] == str[j])
                {
                    cout << str[i] << " IS GELIJK AAN " << str[j] << endl;
                    new_str = new_str + str[i];
                    controle++;
                    break;
                }
            }
            if(controle == 1){break;}
            j++;
        }while(j<size+1);
    }

    new_size = new_str.length();

    for(int i=0; i<new_size; i++)
    {
        if(new_str[i] == 'a'){score += 1;}
        if(new_str[i] == 'b'){score += 2;}
        if(new_str[i] == 'c'){score += 3;}
        if(new_str[i] == 'd'){score += 4;}
        if(new_str[i] == 'e'){score += 5;}
        if(new_str[i] == 'f'){score += 6;}
        if(new_str[i] == 'g'){score += 7;}
        if(new_str[i] == 'h'){score += 8;}
        if(new_str[i] == 'i'){score += 9;}
        if(new_str[i] == 'j'){score += 10;}
        if(new_str[i] == 'k'){score += 11;}
        if(new_str[i] == 'l'){score += 12;}
        if(new_str[i] == 'm'){score += 13;}
        if(new_str[i] == 'n'){score += 14;}
        if(new_str[i] == 'o'){score += 15;}
        if(new_str[i] == 'p'){score += 16;}
        if(new_str[i] == 'q'){score += 17;}
        if(new_str[i] == 'r'){score += 18;}
        if(new_str[i] == 's'){score += 19;}
        if(new_str[i] == 't'){score += 20;}
        if(new_str[i] == 'u'){score += 21;}
        if(new_str[i] == 'v'){score += 22;}
        if(new_str[i] == 'w'){score += 23;}
        if(new_str[i] == 'x'){score += 24;}
        if(new_str[i] == 'y'){score += 25;}
        if(new_str[i] == 'z'){score += 26;}
        if(new_str[i] == 'A'){score += 27;}
        if(new_str[i] == 'B'){score += 28;}
        if(new_str[i] == 'C'){score += 29;}
        if(new_str[i] == 'D'){score += 30;}
        if(new_str[i] == 'E'){score += 31;}
        if(new_str[i] == 'F'){score += 32;}
        if(new_str[i] == 'G'){score += 33;}
        if(new_str[i] == 'H'){score += 34;}
        if(new_str[i] == 'I'){score += 35;}
        if(new_str[i] == 'J'){score += 36;}
        if(new_str[i] == 'K'){score += 37;}
        if(new_str[i] == 'L'){score += 38;}
        if(new_str[i] == 'M'){score += 39;}
        if(new_str[i] == 'N'){score += 40;}
        if(new_str[i] == 'O'){score += 41;}
        if(new_str[i] == 'P'){score += 42;}
        if(new_str[i] == 'Q'){score += 43;}
        if(new_str[i] == 'R'){score += 44;}
        if(new_str[i] == 'S'){score += 45;}
        if(new_str[i] == 'T'){score += 46;}
        if(new_str[i] == 'U'){score += 47;}
        if(new_str[i] == 'V'){score += 48;}
        if(new_str[i] == 'W'){score += 49;}
        if(new_str[i] == 'X'){score += 50;}
        if(new_str[i] == 'Y'){score += 51;}
        if(new_str[i] == 'Z'){score += 52;}

        cout << "score van -> " << str[i] << " -> " << score << endl;
    }

    cout << "EIND SCORE IS GELIJK AAN -> " << score << endl;
    cout << new_str << endl << new_size << endl;
}
void deel_2()
{
    string file  = "input.txt";
    ifstream myfile; myfile.open(file);
    string str, str_1, str_2, str_3, new_str, new_str_2, test;
    int size_str_1, size_str_2, size_str_3, new_size, score = 0;

    int i = 0;
    int j = 0;

    while (getline(myfile, str))
    {
        if(i == 0)
        {
            str_1 = str;
            cout << i << " " << str_1 << endl;
            size_str_1 = str_1.length();
            i = 1;
        }
        else if(i == 1)
        {
            str_2 = str;
            cout << i << " " << str_2 << endl;
            size_str_2 = str_2.length();
            i = 2;
        }
        else if(i == 2)
        {
            str_3 = str;
            cout << i << " " << str_3 << endl;
            size_str_3 = str_3.length();
            i = 3;
        }

        if(i == 3)
        {
            for(int m=0; m<size_str_1; m++)
            {
                for(int n=0; n<size_str_2; n++)
                {
                    for(int o=0; o<size_str_3; o++)
                    {
                        if(str_1[m] == str_2[n])
                        {
                            if(str_1[m] == str_3[o])
                            {
                                new_str = new_str + str_1[m];
                                j = 1;
                                break;
                            }
                        }
                    }
                    if(j == 1)
                    {
                        j = 2;
                        break;
                    }
                }
                if(j == 2)
                {
                    j = 0;
                    break;
                }
            }
            i = 0;
        }
    }

    cout << "**** " << new_str << " ****" << endl;

    new_size = new_str.length();

    for(int i=0; i<new_size; i++)
    {
        if(new_str[i] == 'a'){score += 1;}
        if(new_str[i] == 'b'){score += 2;}
        if(new_str[i] == 'c'){score += 3;}
        if(new_str[i] == 'd'){score += 4;}
        if(new_str[i] == 'e'){score += 5;}
        if(new_str[i] == 'f'){score += 6;}
        if(new_str[i] == 'g'){score += 7;}
        if(new_str[i] == 'h'){score += 8;}
        if(new_str[i] == 'i'){score += 9;}
        if(new_str[i] == 'j'){score += 10;}
        if(new_str[i] == 'k'){score += 11;}
        if(new_str[i] == 'l'){score += 12;}
        if(new_str[i] == 'm'){score += 13;}
        if(new_str[i] == 'n'){score += 14;}
        if(new_str[i] == 'o'){score += 15;}
        if(new_str[i] == 'p'){score += 16;}
        if(new_str[i] == 'q'){score += 17;}
        if(new_str[i] == 'r'){score += 18;}
        if(new_str[i] == 's'){score += 19;}
        if(new_str[i] == 't'){score += 20;}
        if(new_str[i] == 'u'){score += 21;}
        if(new_str[i] == 'v'){score += 22;}
        if(new_str[i] == 'w'){score += 23;}
        if(new_str[i] == 'x'){score += 24;}
        if(new_str[i] == 'y'){score += 25;}
        if(new_str[i] == 'z'){score += 26;}
        if(new_str[i] == 'A'){score += 27;}
        if(new_str[i] == 'B'){score += 28;}
        if(new_str[i] == 'C'){score += 29;}
        if(new_str[i] == 'D'){score += 30;}
        if(new_str[i] == 'E'){score += 31;}
        if(new_str[i] == 'F'){score += 32;}
        if(new_str[i] == 'G'){score += 33;}
        if(new_str[i] == 'H'){score += 34;}
        if(new_str[i] == 'I'){score += 35;}
        if(new_str[i] == 'J'){score += 36;}
        if(new_str[i] == 'K'){score += 37;}
        if(new_str[i] == 'L'){score += 38;}
        if(new_str[i] == 'M'){score += 39;}
        if(new_str[i] == 'N'){score += 40;}
        if(new_str[i] == 'O'){score += 41;}
        if(new_str[i] == 'P'){score += 42;}
        if(new_str[i] == 'Q'){score += 43;}
        if(new_str[i] == 'R'){score += 44;}
        if(new_str[i] == 'S'){score += 45;}
        if(new_str[i] == 'T'){score += 46;}
        if(new_str[i] == 'U'){score += 47;}
        if(new_str[i] == 'V'){score += 48;}
        if(new_str[i] == 'W'){score += 49;}
        if(new_str[i] == 'X'){score += 50;}
        if(new_str[i] == 'Y'){score += 51;}
        if(new_str[i] == 'Z'){score += 52;}
    }

    cout << "EIND SCORE IS GELIJK AAN -> " << score << endl;
}
