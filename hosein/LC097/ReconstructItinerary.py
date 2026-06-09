from collections import defaultdict
import heapq


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)
        for departure, arrival in tickets:
            heapq.heappush(graph[departure], arrival)

        route = []

        def depth_first_search(airport: str) -> None:
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                depth_first_search(next_airport)
            route.append(airport)

        depth_first_search("JFK")
        return route[::-1]