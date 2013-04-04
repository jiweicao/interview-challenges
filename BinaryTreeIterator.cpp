struct TreeNode {
  int val;
  TreeNode * left, *right;
  TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

class TreeIterator {
private:
  stack<TreeNode*> stack_nodes;
  TreeNode *curr;

public:
  TreeIterator(TreeNode * root) {
    curr = root;
    while(curr != NULL) {
      stack_nodes.push(curr);
      cout << curr->val << endl;
      curr = curr->left;
    }
  }
  void showSize() const {cout << "stack size:" << stack_nodes.size() << endl;}
  TreeIterator* next() {
    showSize();
    while(stack_nodes.top() == NULL) {
      stack_nodes.pop();
    }
    curr = stack_nodes.top();
    cout << curr->val << endl; // questions herbe??? segmentation fault
    stack_nodes.pop();
    stack_nodes.push(curr->right);
    return this;
  }
};
