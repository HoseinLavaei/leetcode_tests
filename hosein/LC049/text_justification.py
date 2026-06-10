from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        index = 0

        while index < len(words):
            line_words = []
            words_len = 0

            while (
                index < len(words)
                and words_len + len(words[index]) + len(line_words) <= maxWidth
            ):
                line_words.append(words[index])
                words_len += len(words[index])
                index += 1

            is_last_line = index == len(words)
            gaps = len(line_words) - 1

            if is_last_line or gaps == 0:
                line = " ".join(line_words)
                result.append(line + " " * (maxWidth - len(line)))
                continue

            total_spaces = maxWidth - words_len
            spaces_per_gap, extra_spaces = divmod(total_spaces, gaps)

            line_parts = []
            for gap_index, word in enumerate(line_words[:-1]):
                line_parts.append(word)
                spaces = spaces_per_gap
                if gap_index < extra_spaces:
                    spaces += 1
                line_parts.append(" " * spaces)

            line_parts.append(line_words[-1])
            result.append("".join(line_parts))

        return result
