from .ReconstructItinerary import Solution

def test_reconstruct_itinerary():
    assert Solution().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]) == ["JFK","MUC","LHR","SFO","SJC"]