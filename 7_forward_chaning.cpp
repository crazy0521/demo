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

// Check if all conditions of a rule are satisfied by known facts
bool conditionsSatisfied(const vector<string>& conditions, const map<string, bool>& facts) {
    for (auto& cond : conditions) {
        if (facts.find(cond) == facts.end() || facts.at(cond) == false)
            return false;
    }
    return true;
}

// Forward chaining algorithm
void forwardChaining(vector<Rule>& rules, map<string, bool>& facts) {
    bool newFactAdded = true;

    while (newFactAdded) {
        newFactAdded = false;

        for (auto& rule : rules) {
            if (conditionsSatisfied(rule.conditions, facts) && facts[rule.conclusion] == false) {
                cout << "Applying rule: IF ";
                for (size_t i = 0; i < rule.conditions.size(); i++) {
                    cout << rule.conditions[i];
                    if (i != rule.conditions.size() - 1) cout << " AND ";
                }
                cout << " THEN " << rule.conclusion << endl;

                facts[rule.conclusion] = true;
                newFactAdded = true;
            }
        }
    }
}

// Main function
int main() {
    // Initial facts
    map<string, bool> facts;
    facts["Has_Fever"] = true;
    facts["Has_Cough"] = true;
    facts["Flu"] = false;
    facts["Has_Rash"] = true;
    facts["Measles"] = false;

    // Rules
    vector<Rule> rules = {
        { {"Has_Fever", "Has_Cough"}, "Flu" },
        { {"Has_Fever", "Has_Rash"}, "Measles" }
    };

    cout << "Initial facts:\n";
    for (auto& f : facts)
        if (f.second) cout << "- " << f.first << endl;
    cout << "\n";

    // Run Forward Chaining
    forwardChaining(rules, facts);

    cout << "\nFinal inferred facts:\n";
    for (auto& f : facts)
        if (f.second) cout << "- " << f.first << endl;

    return 0;
}

//o/p
// PS E:\AI_LAB> g++ 7.forward_chaining.cpp -o forward_chaining
// >>
// PS E:\AI_LAB> ./forward_chaining
// >>
// Initial facts:
// - Has_Cough
// - Has_Fever
// - Has_Rash

// Applying rule: IF Has_Fever AND Has_Cough THEN Flu
// Applying rule: IF Has_Fever AND Has_Rash THEN Measles

// Final inferred facts:x 
// - Flu
// - Has_Cough
// - Has_Fever
// - Has_Rash
// - Measles
