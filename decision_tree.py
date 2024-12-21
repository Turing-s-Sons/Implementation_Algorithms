from math import log2
from typing import List, Tuple

class Node:
    def __init__(self, axis: int, val: float, l: 'Node' = None, r: 'Node' = None, ans: int = None) -> None:
        self.axis = axis
        self.val = val
        self.l = l
        self.r = r
        self.ans = ans
    
    def __str__(self):
        return f"""Node({self.axis=}, {self.val=}, {str(self.l)=}, {str(self.r)=}, {self.ans=})"""

class MazgasTree:
    def __init__(self):
        self.main_node: Node = None

    def entropy(self, data: List[tuple]) -> float:
        if not data:
            return 0.0
        total = len(data)
        counts = [0, 0]
        for _, _, label in data:
            counts[int(label)] += 1
        probs = [x / total for x in counts if x > 0]
        return -sum(p * log2(p) for p in probs)
    
    def build_tree(self, points: List[Tuple[float, float, int]], depth: int = 0) -> Node:
        if len(set([p[2] for p in points])) == 1:
            return Node(axis=-1, val=None, ans=points[0][2])

        best_entropy = float('inf')
        best_val = None
        best_axis = None
        best_left = None
        best_right = None

        for axis in range(2):
            points_sorted = sorted(points, key=lambda x: x[axis])
            for i in range(1, len(points)):
                left = points_sorted[:i]
                right = points_sorted[i:]
                e_left = self.entropy(left)
                e_right = self.entropy(right)
                total_entropy = (len(left) / len(points)) * e_left + (len(right) / len(points)) * e_right

                if total_entropy < best_entropy:
                    best_entropy = total_entropy
                    best_val = (points_sorted[i-1][axis] + points_sorted[i][axis]) / 2
                    best_axis = axis
                    best_left = left
                    best_right = right

        if best_axis is None:
            return Node(axis=-1, val=None, ans=points[0][2])

        left_node = self.build_tree(best_left, depth + 1)
        right_node = self.build_tree(best_right, depth + 1)
        return Node(axis=best_axis, val=best_val, l=left_node, r=right_node)
    
    def classify(self, point: Tuple[float], node: Node = None):
        if node is None:
            node = self.main_node

        while node.ans is None:
          if point[node.axis] <= node.val:
                node = node.l
          else:
                node = node.r
        
        return node.ans

tree = MazgasTree()

n = int(input())
points = [tuple(map(float, input().split())) for _ in range(n)]

tree.main_node = tree.build_tree(points)

m = int(input())
for _ in range(m):
    point = tuple(map(float, input().split()))
    print(int(tree.classify(point)))
