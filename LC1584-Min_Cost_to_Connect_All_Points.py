'''
Difficulty: Medium
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.


'''
from typing import List
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)        
        min_heap = [(0, 0)]  # (cost, point_index)
        visited = set()
        total_cost = 0

        def manhattan(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            # print(f"Cost: {cost}, i: {i}, n: {n}")
            if i in visited:
                continue
            visited.add(i)
            total_cost += cost
            for j in range(n):
                if j not in visited:
                    dist = manhattan(points[i], points[j])
                    heapq.heappush(min_heap, (dist, j))
        return total_cost