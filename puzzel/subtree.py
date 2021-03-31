# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isMatch(s, t): return True
        if not s or not t: return False
        return self.isSubtree(s.left, t.left) or self.isSubtree(s.right, t.right)

    def isMatch(self, s, t) -> bool:
        if not (s and t):
            return s is t
        print(type(s))
        print(type(t))
        return (s.val == t.val
                and self.isMatch(s.left, t.left)
                and self.isMatch(s.right, t.right))


sol = Solution()

t = TreeNode(3, TreeNode(4, TreeNode())
tl = TreeNode(4, 1, 2)
tll = TreeNode(1, 0, None)
tl.left = tll
t.left = tl


s = TreeNode(4, 1, 2)

print(sol.isSubtree(s, t))

'''
public class Solution {
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if (s == null) return false;
        if (isSame(s, t)) return true;
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
    
    private boolean isSame(TreeNode s, TreeNode t) {
        if (s == null && t == null) return true;
        if (s == null || t == null) return false;
        
        if (s.val != t.val) return false;
        
        return isSame(s.left, t.left) && isSame(s.right, t.right);
    }
}
'''



'''
public boolean isSubtree(TreeNode s, TreeNode t) {
    Queue<TreeNode> nodes = new ArrayDeque<>();
    nodes.offer(s);
    while (!nodes.isEmpty()) {
        TreeNode node = nodes.poll();
        if (isSameTree(node, t)) {
            return true;
        }
        if (node.left != null) {
            nodes.offer(node.left);
        }
        if (node.right != null) {
            nodes.offer(node.right);
        }
    }
    return false;
}

public boolean isSameTree(TreeNode s, TreeNode t) {
    if (s == null && t == null) {
        return true;
    }
    if (s == null || t == null) {
        return false;
    }
    if (s.val != t.val) {
        return false;
    } else {
        return isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
    }
}
'''