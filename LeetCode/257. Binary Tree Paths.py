# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(node, path):
            path += '->'
            path += str(node.val) # 문자열로 붙이기
            
            # 1. 왼쪽 또는 오른쪽에 노드가 있는지 확인
            if not node.left and not node.right: # 4. 노드가 없다면
                return ans.append(path[2:]) # 맨 앞 화살표를 제거하고 반환

            # 2. 노드가 있다면
            if node.left:
                # 3. 그 노드를 루트로 설정하여 dfs를 재귀적으로 수행
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        
        ans = []
        dfs(root, "")
        return ans