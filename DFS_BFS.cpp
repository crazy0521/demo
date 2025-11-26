#include<iostream>
#include<queue>
using namespace std;

class Node{
public:
    int data;
    Node* left;
    Node* right;

    Node(int data){
        this->data=data;
        this->right=NULL;
        this->left =NULL;
    }
};

Node* build (Node* root){
    int data;
    cout<<"Enter the data:"<<endl;
    cin>>data;
    root = new Node(data);
    if(data == -1){
        return NULL;
    }

    cout<<"Enter data for left child of "<<data<<" : "<<endl;
    root->left = build(root->left);
    cout<<"Enter data for right child of "<<data<<" : "<<endl;
    root->right = build(root->right);

    return root;

}

void DFS(Node* root){
    if(root==NULL){
        return;
    }
    DFS(root->left);
    cout<<root->data<<" ";
    DFS(root->right);
}

void BFS(Node * root){
    if(root==NULL){
        return;
    }
    queue<Node*> q;
    q.push(root);
    q.push(NULL);
    while(!q.empty()){
        Node* temp = q.front();
        q.pop();
        if(temp==NULL){
            cout<<endl;
            if(!q.empty()){
                q.push(NULL);
            }
        }
        else{
            cout<<temp->data<<" ";
            if(temp->left)
            {
                q.push(temp->left);
            }
            if(temp->right){
                q.push(temp->right);
            }
        }
    }
    
}

int main(int argc, char const *argv[])
{
    Node* root=NULL;
    root=build(root);

    DFS(root);
    cout<<endl;
    BFS(root);
    return 0;
    // 1 2 4 -1 -1 5 -1 -1 3 6 -1 -1 7 -1 -1
}

