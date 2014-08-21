#include<iostream>
#include <vector>
using namespace std;

class Solution{
public:
    bool isValidSudoku(const vector<vector<char> > &board){
        if(!board.size()) return false;
        vector<bool> check;
        for(int i=0;i<9;i++){



        }
    }
    void print(const vector<vector<char> > &board){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                cout<<board[i][j]<<" ";
            }
            cout<<endl;
        }
    }
};

int main(){
    Solution S;
    vector<char> lines(9,'.');
    vector<vector<char> > board;
    while(1){
        board=vector<vector<char> >(9,vector<char>(9,'.'));
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                cin>>board[i][j];
            }
        }
        S.print(board);
        if(S.isValidSudoku(board)) cout<<"Yes"<<endl;
        else cout<<"No"<<endl;
    }
    return 0;
}
