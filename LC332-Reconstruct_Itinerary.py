'''
Difficulty: Hard
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.
'''
from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])
        for k in graph:
            graph[k] = sorted(graph[k])
        
        path = []
        def heirholzer(node):
            while graph[node]:
                next_stop = graph[node].pop(0)
                heirholzer(next_stop)
            path.append(node)
        heirholzer('JFK')
        return path[::-1]