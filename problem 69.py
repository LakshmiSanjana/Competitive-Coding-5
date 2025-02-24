# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO


# Your code here along with comments explaining your approach

############## BFS  ###################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        q = deque()
        q.append(root)
        res = []
        #level = 0

        while q:
            len_q = len(q)
            ans = float(-inf)

            for _ in range(len_q):
                curr = q.popleft()
                ans = max(ans,curr.val)

                if curr.left != None:
                    q.append(curr.left)

                if curr.right != None:
                    q.append(curr.right)
            
            res.append(ans)
            #level += 1
        
        return res

############# DFS ###################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        self.res = []
        self.dfs(root, 0)
        
        return self.res

    def dfs(self, root: Optional[TreeNode],depth):
        # base
        if root == None:
            return

        # logic
        if depth == len(self.res):
            self.res.append(root.val)
        else:
            self.res[depth] = max(self.res[depth],root.val)


        self.dfs(root.left,depth+1)
        self.dfs(root.right,depth+1)

        