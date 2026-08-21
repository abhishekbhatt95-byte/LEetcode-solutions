class Solution {
public:
    int k;
    vector<int> sizes;

    // Returns {isPerfect, height}
    pair<bool, int> dfs(TreeNode* root) {
        if (!root)
            return {true, 0};

        auto left = dfs(root->left);
        auto right = dfs(root->right);

        bool perfect = left.first && right.first &&
                       left.second == right.second;

        int height = max(left.second, right.second) + 1;

        if (perfect) {
            int size = (1 << height) - 1;
            sizes.push_back(size);
        }

        return {perfect, height};
    }

    int kthLargestPerfectSubtree(TreeNode* root, int k) {
        this->k = k;

        dfs(root);

        sort(sizes.rbegin(), sizes.rend());

        if (sizes.size() < k)
            return -1;

        return sizes[k - 1];
    }
};