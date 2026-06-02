class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Use the shorter word as columns to save memory.
        if len(word1) < len(word2):
            longer_word = word2
            shorter_word = word1
        else:
            longer_word = word1
            shorter_word = word2

        previous_row_distances = list(range(len(shorter_word) + 1))

        for longer_index, longer_char in enumerate(longer_word, start=1):
            current_row_distances = [longer_index] + [0] * len(shorter_word)

            for shorter_index, shorter_char in enumerate(shorter_word, start=1):
                if longer_char == shorter_char:
                    current_row_distances[shorter_index] = previous_row_distances[shorter_index - 1]
                    continue

                delete_cost = previous_row_distances[shorter_index]
                insert_cost = current_row_distances[shorter_index - 1]
                replace_cost = previous_row_distances[shorter_index - 1]

                current_row_distances[shorter_index] = 1 + min(
                    delete_cost,
                    insert_cost,
                    replace_cost,
                )

            previous_row_distances = current_row_distances

        return previous_row_distances[-1]
