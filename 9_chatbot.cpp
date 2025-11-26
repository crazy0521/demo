#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Convert string to lowercase for easy comparison
string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    return s;
}

int main() {
    cout << "==============================\n";
    cout << "  Hospital Assistant Chatbot\n";
    cout << "==============================\n";
    cout << "Type 'bye' to exit.\n\n";

    string userInput;

    while (true) {
        cout << "You: ";
        getline(cin, userInput);
        string msg = toLower(userInput);

        if (msg == "bye" || msg == "exit") {
            cout << "Chatbot: Goodbye! Take care.\n";
            break;
        } 
        else if (msg.find("hello") != string::npos || msg.find("hi") != string::npos) {
            cout << "Chatbot: Hello! How can I help you today?\n";
        }
        else if (msg.find("appointment") != string::npos) {
            cout << "Chatbot: Sure! Please provide your preferred date and department.\n";
        }
        else if (msg.find("doctor") != string::npos) {
            cout << "Chatbot: We have doctors available in General Medicine, Pediatrics, and Dermatology.\n";
        }
        else if (msg.find("time") != string::npos || msg.find("hours") != string::npos) {
            cout << "Chatbot: Our hospital is open from 9 AM to 8 PM, Monday to Saturday.\n";
        }
        else if (msg.find("emergency") != string::npos) {
            cout << "Chatbot: In case of emergency, please dial 108 immediately!\n";
        }
        else if (msg.find("thank") != string::npos) {
            cout << "Chatbot: You're welcome! Anything else I can help you with?\n";
        }
        else {
            cout << "Chatbot: I'm sorry, I didn't understand that. Can you rephrase?\n";
        }
    }

    return 0;
}

//o/p
// PS E:\AI_LAB> g++ 9.chatbot.cpp -o chatbot
// >>
// PS E:\AI_LAB> ./chatbot
// >>
// ==============================
//   Hospital Assistant Chatbot
// ==============================
// Type 'bye' to exit.

// You: hello
// Chatbot: Hello! How can I help you today?
// You: I want to book an appointment
// Chatbot: Sure! Please provide your preferred date and department.
// You: what time do you open?
// Chatbot: Our hospital is open from 9 AM to 8 PM, Monday to Saturday.
// You: thanks
// Chatbot: You're welcome! Anything else I can help you with?
// You: bye
// Chatbot: Goodbye! Take care.
