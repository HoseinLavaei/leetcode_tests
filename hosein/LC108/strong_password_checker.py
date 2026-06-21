import re

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        lower = any(c.islower() for c in password)
        upper = any(c.isupper() for c in password)
        digit = any(c.isdigit() for c in password)
        missing = 3 - (lower + upper + digit)
        runs = [m.end() - m.start() for m in re.finditer(r'(.)\1*', password) if m.end() - m.start() >= 3]
        if n < 6:
            return max(6 - n, missing)
        if n <= 20:
            replacements = sum(r // 3 for r in runs)
            return max(replacements, missing)
        deletions_needed = n - 20
        replacements = sum(r // 3 for r in runs)
        mod0, mod1, mod2 = [], [], []
        for r in runs:
            if r % 3 == 0:
                mod0.append(r)
            elif r % 3 == 1:
                mod1.append(r)
            else:
                mod2.append(r)
        for _ in mod0:
            if deletions_needed >= 1:
                deletions_needed -= 1
                replacements -= 1
            else:
                break
        for _ in mod1:
            if deletions_needed >= 2:
                deletions_needed -= 2
                replacements -= 1
            elif deletions_needed == 1:
                deletions_needed -= 1
                break
            else:
                break
        for _ in mod2:
            if deletions_needed >= 3:
                deletions_needed -= 3
                replacements -= 1
            else:
                break
        return (n - 20) + max(replacements, missing)