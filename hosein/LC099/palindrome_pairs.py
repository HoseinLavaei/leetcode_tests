from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # Map each word to its index
        word_to_index = {word: idx for idx, word in enumerate(words)}
        result_pairs = []

        for current_index, current_word in enumerate(words):
            word_length = len(current_word)
            # Check all possible split points
            for split_position in range(word_length + 1):
                prefix_part = current_word[:split_position]
                suffix_part = current_word[split_position:]

                # If prefix is palindrome, then we look for reverse of suffix
                if prefix_part == prefix_part[::-1]:
                    reversed_suffix = suffix_part[::-1]
                    if reversed_suffix in word_to_index:
                        partner_index = word_to_index[reversed_suffix]
                        if partner_index != current_index:
                            result_pairs.append([partner_index, current_index])

                # If suffix is palindrome, then we look for reverse of prefix
                # Avoid duplicate when split_position == word_length (already handled above)
                if split_position != word_length and suffix_part == suffix_part[::-1]:
                    reversed_prefix = prefix_part[::-1]
                    if reversed_prefix in word_to_index:
                        partner_index = word_to_index[reversed_prefix]
                        if partner_index != current_index:
                            result_pairs.append([current_index, partner_index])

        return result_pairs