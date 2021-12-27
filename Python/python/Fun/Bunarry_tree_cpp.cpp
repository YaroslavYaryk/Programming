#include <iostream>
#include <locale>
#define N 5
using namespace std;
class tree {
public:
    int data;
    tree* left;
    tree* right;
    tree(int data) {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

int GetSumByLevel(tree* root, int s, int l)
{
    if (root != NULL)
    {
        s++;
        if (s < l)
        {
            int sum = 0;
            sum += GetSumByLevel(root->left, s, l);
            sum += GetSumByLevel(root->right, s, l);
            return sum;
        }
        else
            return 1;
    }
    else
        return 0;
}
void print(tree* root, int space = 0, int t = 0) {
    int COUNT = 3;

    if (root == NULL)
        return;
    space += COUNT;

    print(root->right, space, 1);

    for (int i = COUNT; i < space; i++) {
        cout << " ";
    }
    if (t == 1) { // Right 
        cout<< "/ "<< root->data<< endl;
    }
    else if (t == 2) { // Left 
        cout << "\\ " << root->data << endl;
    }
    else { // Root 
        cout << root->data << endl;
    }

    print(root->left, space, 2);
}

int main() {
    setlocale(LC_CTYPE, "ukr");
    int asum[N];
    int sum;
    int max;
    int maxl;
    tree* root = new tree(5);
    root->left = new tree(3);
    root->right = new tree(8);
    root->left->left = new tree(4);
    root->left->right = new tree(5);
    root->right->left = new tree(1);
    root->right->right = new tree(7);
    root->right->left->left = new tree(0);
    root->right->right->right = new tree(9);
    // print(root);
    for (int i = 0; i < N; i++) {
        sum = GetSumByLevel(root, -1, i);
        asum[i] = sum;
        cout <<"Сума елементiв на рiвнi ["<<i<<"] = "<<asum[i]<<endl;
    }
    max = asum[0];
    for (int j = 0; j < N; j++) {
        if (asum[j] > max) {
            max = asum[j];
            maxl = j;
        }
    }
    cout <<"Сума елементiв максимальна: = "<<max<<"на рiвнi ["<<maxl<<"]";
    cout << endl;
    system("pause");
    return 0;
}