#include <iostream>
#include <vector>
#include <limits>
using namespace std;

const char PLAYER = 'X'; // Human
const char AI = 'O';     // Computer

// Print the board
void printBoard(vector<vector<char>> &board)
{
    cout << "\n";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == ' ')
            {
                cout << "." << " "; // empty cell shown as dot
            }
            else
            {
                cout << board[i][j] << " "; // print X or O
            }
        }
        cout << "\n";
    }
    cout << "\n";
}

// Check if moves are left
bool movesLeft(vector<vector<char>> &board)
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (board[i][j] == ' ')
                return true;
    return false;
}

// Evaluate board: +10 if AI wins, -10 if player wins, 0 otherwise
int evaluate(vector<vector<char>> &b)
{
    // Rows
    for (int row = 0; row < 3; row++)
    {
        if (b[row][0] == b[row][1] && b[row][1] == b[row][2] && b[row][0] != ' ')
        {
            return (b[row][0] == AI) ? 10 : -10;
        }
    }
    // Cols
    for (int col = 0; col < 3; col++)
    {
        if (b[0][col] == b[1][col] && b[1][col] == b[2][col] && b[0][col] != ' ')
        {
            return (b[0][col] == AI) ? 10 : -10;
        }
    }
    // Diagonals
    if (b[0][0] == b[1][1] && b[1][1] == b[2][2] && b[0][0] != ' ')
        return (b[0][0] == AI) ? 10 : -10;
    if (b[0][2] == b[1][1] && b[1][1] == b[2][0] && b[0][2] != ' ')
        return (b[0][2] == AI) ? 10 : -10;

    return 0;
}

// Minimax function
int minimax(vector<vector<char>> &board, int depth, bool isMax)
{
    int score = evaluate(board);

    if (score == 10)
        return score - depth; // AI wins
    if (score == -10)
        return score + depth; // Human wins
    if (!movesLeft(board))
        return 0; // Draw

    if (isMax)
    {
        int best = numeric_limits<int>::min();
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (board[i][j] == ' ')
                {
                    board[i][j] = AI;
                    best = max(best, minimax(board, depth + 1, false));
                    board[i][j] = ' ';
                }
            }
        }
        return best;
    }
    else
    {
        int best = numeric_limits<int>::max();
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (board[i][j] == ' ')
                {
                    board[i][j] = PLAYER;
                    best = min(best, minimax(board, depth + 1, true));
                    board[i][j] = ' ';
                }
            }
        }
        return best;
    }
}

// Find the best move for AI
pair<int, int> findBestMove(vector<vector<char>> &board)
{
    int bestVal = numeric_limits<int>::min();
    pair<int, int> bestMove = {-1, -1};

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            if (board[i][j] == ' ')
            {
                board[i][j] = AI;
                int moveVal = minimax(board, 0, false);
                board[i][j] = ' ';
                if (moveVal > bestVal)
                {
                    bestMove = {i, j};
                    bestVal = moveVal;
                }
            }
        }
    }
    return bestMove;
}

// -------------------- MAIN --------------------
int main()
{
    vector<vector<char>> board(3, vector<char>(3, ' '));
    int x, y;
    cout << "Tic-Tac-Toe (You = X, Computer = O)\n";

    for (int turn = 0; turn < 9; turn++)
    {
        printBoard(board);
        if (turn % 2 == 0)
        {
            cout << "Enter your move (row col): ";
            cin >> x >> y;
            if (x >= 0 && x < 3 && y >= 0 && y < 3 && board[x][y] == ' ')
            {
                board[x][y] = PLAYER;
            }
            else
            {
                cout << "Invalid move! Try again.\n";
                turn--;
            }
        }
        else
        {
            cout << "Computer's move...\n";
            pair<int, int> bestMove = findBestMove(board);
            board[bestMove.first][bestMove.second] = AI;
        }

        int score = evaluate(board);
        if (score == 10)
        {
            printBoard(board);
            cout << "Computer Wins!\n";
            break;
        }
        if (score == -10)
        {
            printBoard(board);
            cout << "You Win!\n";
            break;
        }
        if (!movesLeft(board))
        {
            printBoard(board);
            cout << "It's a Draw!\n";
            break;
        }
    }
    return 0;
}

// o/p
//  PS E:\AI_LAB> g++ "5.minmax algorithm.cpp" -o minimax_game
//  >>
//  PS E:\AI_LAB> ./minimax_game
//  >>
//  Tic-Tac-Toe (You = X, Computer = O)

// . . .
// . . .
// . . .

// Enter your move (row col): 0 0

// X . .
// . . .
// . . .

// Computer's move...

// X . .
// . O .
// . . .

// Enter your move (row col): 2 0

// X . .
// . O .
// X . .

// Computer's move...

// X . .
// O O .
// X . .

// Enter your move (row col): 1 2

// X . .
// O O X
// X . .

// Computer's move...

// X O .
// O O X
// X . .

// Enter your move (row col): 2 1

// X O .
// O O X
// X X .

// Computer's move...

// X O .
// O O X
// X X O

// Enter your move (row col): 0 2

// X O X
// O O X
// X X O

// It's a Draw!