#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;

// Rule structure
struct Rule {
    vector<string> conditions;  // IF conditions
    string conclusion;          // THEN conclusion
};

// Recursive function for backward chaining
bool backwardChaining(string goal, vector<Rule>& rules, map<string, bool>& facts) {
    // If already known fact
    if (facts.find(goal) != facts.end()) {
        return facts[goal];
    }

    // Try to prove using rules
    for (auto& rule : rules) {
        if (rule.conclusion == goal) {
            bool allTrue = true;
            for (auto& cond : rule.conditions) {
                if (!backwardChaining(cond, rules, facts)) {
                    allTrue = false;
                    break;
                }
            }
            if (allTrue) {
                facts[goal] = true;
                cout << "Proved: " << goal << " using rule -> IF ";
                for (size_t i = 0; i < rule.conditions.size(); i++) {
                    cout << rule.conditions[i];
                    if (i != rule.conditions.size() - 1) cout << " AND ";
                }
                cout << " THEN " << goal << endl;
                return true;
            }
        }
    }
    facts[goal] = false;
    return false;
}

// ---------------- MAIN ----------------
int main() {
    // Initial facts
    map<string, bool> facts;
    facts["Has_Fever"] = true;
    facts["Has_Cough"] = true;
    facts["Has_Rash"] = false;

    // Rules
    vector<Rule> rules = {
        { {"Has_Fever", "Has_Cough"}, "Flu" },
        { {"Has_Fever", "Has_Rash"}, "Measles" }
    };

    cout << "Known facts:\n";
    for (auto& f : facts)
        if (f.second) cout << "- " << f.first << endl;
    cout << "\n";

    // Ask user for goal
    string goal;
    cout << "Enter the goal to prove (e.g., Flu, Measles): ";
    cin >> goal;

    if (backwardChaining(goal, rules, facts))
        cout << "\nConclusion: " << goal << " is TRUE\n";
    else
        cout << "\nConclusion: " << goal << " cannot be proved.\n";

    return 0;
}

//o/p
// PS E:\AI_LAB> g++ 8.backward_chaining.cpp -o backward_chaining
// >>
// PS E:\AI_LAB> ./backward_chaining
// >>
// Known facts:
// - Has_Cough
// - Has_Fever

// Enter the goal to prove (e.g., Flu, Measles): Measles

// Conclusion: Measles cannot be proved.
