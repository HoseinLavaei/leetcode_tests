class Solution:
    def shortestPalindrome(self, input_string: str) -> str:
        if not input_string:
            return ""

        reversed_string = input_string[::-1]
        combined_string = input_string + "#" + reversed_string

        lps_array = [0] * len(combined_string)

        prefix_length = 0

        for i in range(1, len(combined_string)):
            while prefix_length > 0 and combined_string[i] != combined_string[prefix_length]:
                prefix_length = lps_array[prefix_length - 1]

            if combined_string[i] == combined_string[prefix_length]:
                prefix_length += 1

            lps_array[i] = prefix_length

        longest_palindromic_prefix_length = lps_array[-1]

        suffix_to_add = input_string[longest_palindromic_prefix_length:]
        reversed_suffix = suffix_to_add[::-1]

        return reversed_suffix + input_string