#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

map<string, vector<string>> family;


void addRelation(string parent, string child) {
    family[parent].push_back(child);
}

void showChildren(string parent) {
    if (family.find(parent) == family.end()) {
        cout << parent << " has no children.\n";
        return;
    }
    cout << "Children of " << parent << ": ";
    for (auto &c : family[parent]) cout << c << " ";
    cout << endl;
}

void isParent(string A, string B) {
    if (family.find(A) != family.end() &&
        find(family[A].begin(), family[A].end(), B) != family[A].end()) {
        cout << A << " is parent of " << B << endl;
    } else {
        cout << A << " is NOT parent of " << B << endl;
    }
}

void isSibling(string A, string B) {
    for (auto &p : family) {
        auto &kids = p.second;
        if (find(kids.begin(), kids.end(), A) != kids.end() &&
            find(kids.begin(), kids.end(), B) != kids.end() &&
            A != B) {
            cout << A << " and " << B << " are siblings\n";
            return;
        }
    }
    cout << A << " and " << B << " are NOT siblings\n";
}

int main() {

    addRelation("John", "Mary");
    addRelation("John", "Mark");
    addRelation("Alice", "John");
    addRelation("Alice", "Linda");
    addRelation("Linda", "Sam");

    showChildren("John");
    showChildren("Alice");

    isParent("John", "Mary");
    isParent("Alice", "Sam");

    isSibling("Mary", "Mark");
    isSibling("John", "Linda");

    return 0;
}
