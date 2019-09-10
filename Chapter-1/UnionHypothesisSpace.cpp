//
//  main.cpp
//  VersionSpace
//
//  Created by Yifan Li on 2019/9/10.
//  Copyright © 2019 Yifan Li. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#define f(x, y, z) for (int x = y; x <= z; ++ x)
#define pb push_back
using namespace std;
int judge(string, string);
bool table[262150];
int total = 0, tok = 0;
vector<int> V1st, Vlast, V;
string hypo[] = {"111", "*11", "001", "101", "*01", "021", "121", "*21", "0*1", "1*1", "**1", "012", "112", "*12", "002", "102", "*02", "022", "122", "*22", "0*2", "1*2", "**2", "010", "110", "*10", "000", "100", "*00", "020", "120", "*20", "0*0", "1*0", "**0", "01*", "11*", "*1*", "00*", "10*", "*0*", "02*", "12*", "*2*", "0**", "1**", "***", "011", "---"};
string input[] = {"000", "001", "002", "010", "011", "012", "020", "021", "022", "100", "101", "102", "110", "111", "112", "120", "121", "122"};

int main(int argc, const char * argv[]) {
    // insert code here...
    f(i, 0, 48) {
        int code = 0;
        f(j, 0, 17) {
            code <<= 1;
            code |= judge(input[j], hypo[i]);
        }
        if (!table[code]) {
            table[code] = true;
            V.pb(code);
            V1st.pb(code);
            tok ++;
        }
    }
    printf("%d %d\n", 1, tok);
    f(k, 2, 18) {
        tok = 0;
        memset(table, false, sizeof table);
        Vlast = V;
        V.clear();
        for (auto i: Vlast) {
            for (auto j: V1st) {
                int rst = i | j;
                if (!table[rst]) {
                    table[rst] = true;
                    tok ++;
                    V.pb(rst);
                }
            }
        }
        printf("%d %d\n", k, tok);
    }
    return 0;
}

int judge(string melon, string hypo) {
    if (hypo == "---") return 0;
    if (hypo[0] != '*' && hypo[0] != melon[0])
        return 0;
    else if (hypo[1] != '*' && hypo[1] != melon[1])
        return 0;
    else if (hypo[2] != '*' && hypo[2] != melon[2])
        return 0;
    else
        return 1;
}
