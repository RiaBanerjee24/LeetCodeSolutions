'''
Difficulty: Medium
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.
'''
from typing import List
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #Straigh up Djsiktra implementation
        
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2],time[1])) #dist,node
        dist = {}
        for i in range(1,n+1):
            dist[i] = float('inf')
        dist[k] = 0
        queue = []
        heapq.heapify(queue)
        heapq.heappush(queue,(0,k))
        visited = set()

        while queue:
            current_dist,node = heapq.heappop(queue)

            if node in visited:
                continue
            visited.add(node)

            for neighbor_dist,neighbor in graph[node]:
                if neighbor not in visited:
                    new_dist = current_dist+neighbor_dist
                    if new_dist<dist[neighbor]:
                        dist[neighbor] = new_dist
                    heapq.heappush(queue,(new_dist,neighbor))
        if max(dist.values()) == float('inf'):
            return -1
        return max(dist.values())

