#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = right = nullptr;
    }
};

// Insertion
Node* insert(Node* root, int val) {
    if (root == nullptr)
        return new Node(val);

    if (val < root->data)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);

    return root;
}

// Search
bool search(Node* root, int val) {
    if (root == nullptr) return false;
    if (root->data == val) return true;
    if (val < root->data)
        return search(root->left, val);
    else
        return search(root->right, val);
}

// Minimum Value
int findMin(Node* root) {
    if (root == nullptr) {
        cout << "Tree is empty.\n";
        return -1;
    }
    while (root->left != nullptr)
        root = root->left;
    return root->data;
}

// Longest Path (height)
int longestPath(Node* root) {
    if (root == nullptr)
        return 0;
    int left = longestPath(root->left);
    int right = longestPath(root->right);
    return max(left, right) + 1;
}

// Inorder Traversal (for visualization)
void inorder(Node* root) {
    if (root == nullptr) return;
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int main() {
    Node* root = nullptr;

    // Insert values
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    insert(root, 60);
    insert(root, 80);

    cout << "Inorder traversal of BST: ";
    inorder(root);
    cout << "\n";

    cout << "Minimum value in BST: " << findMin(root) << "\n";
    cout << "Longest path length (height of tree): " << longestPath(root) << "\n";

    int key = 40;
    if (search(root, key))
        cout << key << " found in BST.\n";
    else
        cout << key << " not found in BST.\n";

    return 0;
}
