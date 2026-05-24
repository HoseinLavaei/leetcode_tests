from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[str, List[str]] = {}

        for string in strs:
            key = "".join(sorted(string))

            if key not in groups:
                groups[key] = []

            groups[key].append(string)

        return list(groups.values())