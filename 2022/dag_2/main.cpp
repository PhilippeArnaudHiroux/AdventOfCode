#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>

#define X 1 //ROCK
#define Y 2 //PAPER
#define Z 3 //SCISSORS

using namespace std;

int main()
{
    string file  = "input.txt";
    ifstream myfile; myfile.open(file);
    string str;

    char a = 0;
    char b = 0;

    int score_ik = 0;
/*
    while (getline(myfile, str))
    {
        if(!str.empty())
        {
            a = str[0];
            b = str[2];

            if(b == 'X')
            {
                score_ik += X;
            }
            else if(b == 'Y')
            {
                score_ik += Y;
            }
            else
            {
                score_ik += Z;
            }

            if(a == 'A' and b == 'X') //ROCK - ROCK
            {
                score_ik += 3;
            }
            else if(a == 'A' and b == 'Y') //ROCK - PAPER
            {
                score_ik += 6;
            }
            else if(a == 'A' and b == 'Z') //ROCK - SCISSORS
            {
                score_ik += 0;
            }

            if(a == 'B' and b == 'X') //PAPER - ROCK
            {
                score_ik += 0;
            }
            else if(a == 'B' and b == 'Y') //PAPER - PAPER
            {
                score_ik += 3;
            }
            else if(a == 'B' and b == 'Z') //PAPER - SCISSORS
            {
                score_ik += 6;
            }

            if(a == 'C' and b == 'X') //SCISSORS - ROCK
            {
                score_ik += 6;
            }
            else if(a == 'C' and b == 'Y') //SCISSORS - PAPER
            {
                score_ik += 0;
            }
            else if(a == 'C' and b == 'Z') //SCISSORS - SCISSORS
            {
                score_ik += 3;
            }
        }
    }
    cout << score_ik << endl;*/
    int score = 0;

    //X -> Verliezen
    //Y -> Gelijk
    //Z -> Winnen

    while (getline(myfile, str))
    {
        if(!str.empty())
        {
            a = str[0];
            b = str[2];

            if(a == 'A' and b == 'X') //ROCK - VERLIEZEN -> SICCORS
            {
                score = score + 0 + 3;
            }
            else if(a == 'A' and b == 'Y') //ROCK - GELIJK -> ROCK
            {
                score = score + 3 + 1;
            }
            else if(a == 'A' and b == 'Z') //ROCK - WINNEN -> PAPER
            {
                score = score + 6 + 2;
            }

            if(a == 'B' and b == 'X') //PAPER - VERLIEZEN -> ROCK
            {
                score = score + 0 + 1;
            }
            else if(a == 'B' and b == 'Y') //PAPER - GELIJK -> PAPER
            {
                score = score + 3 + 2;
            }
            else if(a == 'B' and b == 'Z') //PAPER - WINNEN -> SICCORS
            {
                score = score + 6 + 3;
            }

            if(a == 'C' and b == 'X') //SICCORS - VERLIEZEN -> PAPER
            {
                score = score + 0 + 2;
            }
            else if(a == 'C' and b == 'Y') //SICCORS - GELIJK -> SICCORS
            {
                score = score + 3 + 3;
            }
            else if(a == 'C' and b == 'Z') //SICCORS - WINNEN -> ROCK
            {
                score = score + 6 + 1;
            }
        }
    }

    cout << score << endl;

    return 0;
}



