from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points):
        point_count = len(points)

        if point_count <= 2:
            return point_count

        max_points_on_line = 2

        for anchor_index in range(point_count):
            slope_counts = defaultdict(int)

            anchor_x, anchor_y = points[anchor_index]

            for other_index in range(anchor_index + 1, point_count):
                other_x, other_y = points[other_index]

                delta_x = other_x - anchor_x
                delta_y = other_y - anchor_y

                if delta_x == 0:
                    normalized_slope = ("vertical",)
                elif delta_y == 0:
                    normalized_slope = ("horizontal",)
                else:
                    common_divisor = gcd(delta_x, delta_y)

                    delta_x //= common_divisor
                    delta_y //= common_divisor

                    if delta_x < 0:
                        delta_x *= -1
                        delta_y *= -1

                    normalized_slope = (delta_y, delta_x)

                slope_counts[normalized_slope] += 1

            if slope_counts:
                max_points_on_line = max(
                    max_points_on_line,
                    max(slope_counts.values()) + 1
                )

        return max_points_on_line