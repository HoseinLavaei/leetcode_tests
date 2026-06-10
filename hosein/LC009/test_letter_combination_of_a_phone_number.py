from .letter_combination_of_a_phone_number import Solution

def test_combination_of_a_phone_number():
    assert Solution().letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert Solution().letterCombinations("") == []
