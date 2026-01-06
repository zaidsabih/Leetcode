# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root):
        max_vals = []
        queue = deque([root])
        level = 1

        max_val = None
        max_level = None

        while(queue):

            total = 0
            n = len(queue)
            for _ in range(n):

                node = queue.popleft()
                total += node.val

                if(node.left != None):
                    queue.append(node.left)
                
                if(node.right != None):
                    queue.append(node.right)

            
            if(max_val == None):
                max_val = total
                max_level = level

            elif(total > max_val):
                max_val = total
                max_level = level

            level += 1

        return max_level