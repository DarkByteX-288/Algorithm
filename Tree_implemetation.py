from collections import deque
from typing import List, Optional, Any
class TreeNode:
    """Node class for a tree structure"""
    def __init__(self, value: Any):
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        """Add a child node to the current node"""
        self.children.append(child_node)
    
    def __str__(self):
        return f"Node({self.value})"

class Graph:
    """Graph class using adjacency list representation"""
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex: Any):
        """Add a vertex to the graph"""
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, vertex1: Any, vertex2: Any, directed: bool = False):
        """Add an edge between two vertices"""
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.adj_list[vertex1].append(vertex2)
        if not directed:
            self.adj_list[vertex2].append(vertex1)
    
    def get_neighbors(self, vertex: Any) -> List[Any]:
        """Get all neighbors of a vertex"""
        return self.adj_list.get(vertex, [])

class TreeTraversal:
    """Class containing BFS and DFS implementations for trees"""
    
    @staticmethod
    def bfs_tree(root: TreeNode) -> List[Any]:
        """BFS traversal for trees using queue"""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            current_node = queue.popleft()
            result.append(current_node.value)
            
            # Add all children to the queue
            for child in current_node.children:
                queue.append(child)
        
        return result
    
    @staticmethod
    def dfs_tree_recursive(root: TreeNode) -> List[Any]:
        """DFS traversal for trees using recursion (pre-order)"""
        result = []
        
        def dfs_helper(node):
            if not node:
                return
            result.append(node.value)
            for child in node.children:
                dfs_helper(child)
        
        dfs_helper(root)
        return result
    
    @staticmethod
    def dfs_tree_iterative(root: TreeNode) -> List[Any]:
        """DFS traversal for trees using stack (iterative)"""
        if not root:
            return []
        
        result = []
        stack = [root]
        
        while stack:
            current_node = stack.pop()
            result.append(current_node.value)
            
            # Add children in reverse order to maintain left-to-right traversal
            for child in reversed(current_node.children):
                stack.append(child)
        
        return result

class GraphTraversal:
    """Class containing BFS and DFS implementations for graphs"""
    
    @staticmethod
    def bfs_graph(graph: Graph, start_vertex: Any) -> List[Any]:
        """BFS traversal for graphs using queue"""
        if start_vertex not in graph.adj_list:
            return []
        
        result = []
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            current_vertex = queue.popleft()
            result.append(current_vertex)
            
            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    @staticmethod
    def dfs_graph_recursive(graph: Graph, start_vertex: Any) -> List[Any]:
        """DFS traversal for graphs using recursion"""
        result = []
        visited = set()
        
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start_vertex)
        return result
    
    @staticmethod
    def dfs_graph_iterative(graph: Graph, start_vertex: Any) -> List[Any]:
        """DFS traversal for graphs using stack"""
        if start_vertex not in graph.adj_list:
            return []
        
        result = []
        visited = set()
        stack = [start_vertex]
        visited.add(start_vertex)
        
        while stack:
            current_vertex = stack.pop()
            result.append(current_vertex)
            
            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        
        return result

# Example usage and demonstration
def main():
    print("=== TREE EXAMPLE ===")
    
    # Create a tree
    #        A
    #       / \
    #      B   C
    #     /|   |\
    #    D E   F G
    #     / \
    #    H   I
    
    root = TreeNode('A')
    node_b = TreeNode('B')
    node_c = TreeNode('C')
    node_d = TreeNode('D')
    node_e = TreeNode('E')
    node_f = TreeNode('F')
    node_g = TreeNode('G')
    node_h = TreeNode('H')
    node_i = TreeNode('I')
    
    root.add_child(node_b)
    root.add_child(node_c)
    node_b.add_child(node_d)
    node_b.add_child(node_e)
    node_c.add_child(node_f)
    node_c.add_child(node_g)
    node_e.add_child(node_h)
    node_e.add_child(node_i)
    
    # Tree traversals
    print("Tree BFS:", TreeTraversal.bfs_tree(root))
    print("Tree DFS Recursive:", TreeTraversal.dfs_tree_recursive(root))
    print("Tree DFS Iterative:", TreeTraversal.dfs_tree_iterative(root))
    
    print("\n=== GRAPH EXAMPLE ===")
    
    # Create a graph
    #    A --- B
    #    |     |
    #    C --- D
    #     \   /
    #       E
    
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('D', 'E')
    
    # Graph traversals
    print("Graph BFS starting from A:", GraphTraversal.bfs_graph(graph, 'A'))
    print("Graph DFS Recursive starting from A:", GraphTraversal.dfs_graph_recursive(graph, 'A'))
    print("Graph DFS Iterative starting from A:", GraphTraversal.dfs_graph_iterative(graph, 'A'))
    
    print("\n=== PATH FINDING EXAMPLE ===")
    
    # Find path using BFS
    def find_path_bfs(graph: Graph, start: Any, end: Any) -> Optional[List[Any]]:
        """Find shortest path using BFS"""
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])  # (current_vertex, path)
        visited.add(start)
        
        while queue:
            current_vertex, path = queue.popleft()
            
            for neighbor in graph.get_neighbors(current_vertex):
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        return None
    
    # Find path from A to E
    path = find_path_bfs(graph, 'A', 'E')
    print(f"Shortest path from A to E: {path}")

if __name__ == "__main__":
    main()
    
