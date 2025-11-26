#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
using namespace std;

class MapColor
{
public:
    vector<string> REGIONS = {"WA", "NT", "SA", "Q", "NSW", "V", "T"};
    vector<string> COLORS = {"RED", "GREEN", "BLUE"};
    map<string, vector<string>> NEIGHBORS = {
        {"WA", {"NT", "SA"}},
        {"NT", {"WA", "SA", "Q"}},
        {"SA", {"WA", "NT", "Q", "NSW", "V"}},
        {"Q", {"NT", "SA", "NSW"}},
        {"NSW", {"Q", "SA", "V"}},
        {"V", {"SA", "NSW"}},
        {"T", {}}};
    map<string, string> assignment;
    bool backtrack()
    {

        if (assignment.size() == REGIONS.size())
            return true;
        string var;
        for (auto &r : REGIONS)
        {
            if (assignment.find(r) == assignment.end())
            {
                var = r;
                break;
            }
        }
        for (auto &color : COLORS)
        {
            if (isConsistent(var, color))
            {
                assignment[var] = color;
                if (backtrack())
                    return true;
                assignment.erase(var);
            }
        }
        return false;
    }
    bool isConsistent(const string &var, const string &color)
    {
        for (auto &nb : NEIGHBORS[var])
        {
            if (assignment.find(nb) != assignment.end() && assignment[nb] == color)
                return false;
        }
        return true;
    }
    void printSolution()
    {
        cout << "Solution:\n";
        for (auto &r : REGIONS)
        {
            cout << r << " = " << assignment[r];
            if (!NEIGHBORS[r].empty())
            {
                cout << " | Neighbors: ";
                for (auto &nb : NEIGHBORS[r])
                {
                    cout << nb << "(";
                    if (assignment.find(nb) != assignment.end())
                        cout << assignment[nb];
                    else
                        cout << "Not Assigned";
                    cout << ") ";
                }
            }
            cout << "\n";
        }
    }
};

int main()
{
    MapColor csp;
    if (csp.backtrack())
    {
        csp.printSolution();
    }
    else
    {
        cout << "No solution found.\n";
    }
    return 0;
}
