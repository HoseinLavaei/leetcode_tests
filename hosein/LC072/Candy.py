from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        smallest = 1
        current_candy_given = 1
        candies = []
        for index, rating in enumerate(ratings):
            if index == 0:
                candies.append(current_candy_given)
                continue
            if rating > ratings[index - 1]:
                current_candy_given += 1
                candies.append(current_candy_given)
            elif rating == ratings[index - 1]:
                candies.append(current_candy_given)
            else:
                current_candy_given -= 1
                candies.append(current_candy_given)
            smallest = min(smallest, current_candy_given)

        return (1-smallest) * len(candies) + sum(candies)