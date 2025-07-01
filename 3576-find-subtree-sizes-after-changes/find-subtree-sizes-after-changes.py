from typing import List
from collections import defaultdict

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(node: int, parent_node: int):
            # Initialize the subtree size for the current node to 1
            subtree_sizes[node] = 1
            # Append the current node index to the list of nodes for character s[node]
            character_dict[s[node]].append(node)
            # Recursively traverse the children of the current node
            for child in graph[node]:
                dfs(child, node)
            # Determine the last visited ancestor with the same character
            ancestor = parent_node
            if len(character_dict[s[node]]) > 1:
                ancestor = character_dict[s[node]][-2]
            # If a valid ancestor is found, update its subtree size
            if ancestor != -1:
                subtree_sizes[ancestor] += subtree_sizes[node]
            # Remove the current node from the character's list (backtracking)
            character_dict[s[node]].pop()

        n = len(s)
        # Create an adjacency list representation of the tree
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[parent[i]].append(i)
        # Dictionary to keep track of nodes with the same character
        character_dict = defaultdict(list)
        # List to store the size of the subtree rooted at each node
        subtree_sizes = [0] * n
        # Start DFS traversal from the root node (0) with no parent (-1)
        dfs(0, -1)
        return subtree_sizes
