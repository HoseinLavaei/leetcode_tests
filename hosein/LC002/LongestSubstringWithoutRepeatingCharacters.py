class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        times = (0,0) # times, length
        for first_counter in range(0,len(s)):
            for second_counter in range(first_counter+1,len(s)):
                the_string = s[first_counter:second_counter]
                if is_repeated(the_string):
                    break
                new_times = (repeat_times(s, the_string),len(the_string))
                if new_times[1] > times[1]:
                    times = new_times
                elif new_times[1] == times[1] and new_times[0] > times[0]:
                    times = new_times
        return times[1]

def is_repeated(s: str) -> bool:
    for char in s:
        if len(s.replace(char,"")) + 1 != len(s):
            return True
    return False


def repeat_times(s: str, the_string: str) -> int:
        times = 0
        for counter in range(0,len(s)):
            try:
                if s[counter:counter+len(the_string)] == the_string:
                    times += 1
            except IndexError:
                break
        return times