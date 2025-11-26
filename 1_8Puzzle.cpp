#include <bits/stdc++.h>
using namespace std;

const int N = 3;

struct State {
    vector<vector<int>> board;
    int x, y;   
    string path; 
};

vector<vector<int>> goal = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 0}
};


int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};
char dir[] = {'D', 'L', 'U', 'R'};

bool isValid(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < N);
}

bool isGoal(vector<vector<int>>& b) {
    return b == goal;
}

void printBoard(vector<vector<int>>& b) {
    for (auto &row : b) {
        for (int val : row) {
            cout << val << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

void solvePuzzle(vector<vector<int>> initial, int x, int y) {
    queue<State> q;
    set<vector<vector<int>>> visited;

    State start = {initial, x, y, ""};
    q.push(start);
    visited.insert(initial);

    while (!q.empty()) {
        State cur = q.front();
        q.pop();

        if (isGoal(cur.board)) {
            cout << "Solution found in " << cur.path.size() << " moves.\n\n";
            
            vector<vector<int>> tmp = initial;
            int blankX = x, blankY = y;
            printBoard(tmp);

            for (char move : cur.path) {
                int dirIndex = string("DLUR").find(move);
                int newX = blankX + dx[dirIndex];
                int newY = blankY + dy[dirIndex];
                swap(tmp[blankX][blankY], tmp[newX][newY]);
                blankX = newX;
                blankY = newY;
                printBoard(tmp);
            }
            return;
        }

       
        for (int i = 0; i < 4; i++) {
            int newX = cur.x + dx[i];
            int newY = cur.y + dy[i];

            if (isValid(newX, newY)) {
                vector<vector<int>> newBoard = cur.board;
                swap(newBoard[cur.x][cur.y], newBoard[newX][newY]);

                if (visited.find(newBoard) == visited.end()) {
                    visited.insert(newBoard);
                    q.push({newBoard, newX, newY, cur.path + dir[i]});
                }
            }
        }
    }

    cout << "No solution exists.\n";
}

int main() {
    vector<vector<int>> initial = {
        {1, 2, 3},
        {5, 6, 0},
        {7, 8, 4}
    };

    int x = 1, y = 2;

    cout << "Initial State:\n";
    printBoard(initial);

    cout << "Goal State:\n";
    printBoard(goal);

    cout << "\nSolving using BFS...\n\n";
    solvePuzzle(initial, x, y);

    return 0;
}
