"""All functions to implement for the technical test: Python skills."""
# pylint: disable=unused-import, fixme

# No other import is allowed.
# You don't have to necessary use them all to complete the test.
import math
from functools import reduce
import re
from typing import List


def unique_strings(strings_1: List[str], strings_2: List[str]) -> List[str]:
    """Returns a list of unique strings sorted by alphabetic order.
        ## Arguments
        - `strings_1`: a list of strings 
        - `strings_2`: an other list of strings
        
        ## Returns
        - A list of unique strings
        
        ## Example
            >>> alpha, beta = ["a","b","c","d"], ["a","d","e","f"]
            >>> unique_strings(alpha, beta)
            # ['a', 'b', 'c', 'd', 'e', 'f']
    """
    result = []
    joined_lists = strings_1 + strings_2
    for i in joined_lists:
        if i not in result:
            result.append(i)
    return sorted(result)



def unique_multiple_strings(*args: List[str]) -> List[str]:
    """Returns a list of unique strings sorted by alphabetic order with unlimited arguments.
        ## Example
            >>> unique_multiple_strings(
                ["a","b","c","d"],
                ["a","b","c","d"],
                ["a","d","e","f",
            )
        
        ## Returns
        - A list of unique strings
        
        ## Bonus if you have some spare time
        - one elegant line
    """
    result = []
    for arg in args:
        for str in arg:
            if str not in result:
                result.append(str)
    return sorted(result)



class Word():
    """Word class
        This class can give us some information about a word.
        We will create two methods that can be used on any instance:
            - is_palindrome
            - is_kalindrome
        
        All details are available in the corresponding documentation
    """
    #Do not modify
    def __init__(self, word: str) -> None:
        """Creates an instance of the Word class.
            ## Arguments
            -`word`: The word of the instance to be created. 
        """
        self._word = word # we use an underscore '_' to specify a private variable 
    
    
    #Do not modify
    def get_word(self) -> str:
        """Returns the word of the instance"""
        return self._word
    
    
    def is_palindrome(self) -> bool:
        """ Returns True if the Word instance is a palindrome
            ## What is a palindrome
                - A word, phrase, or sequence that reads the same backwards as forwards. 
                - An empty string is also a palindrome.
            
            ## Examples
                >>> is_palindrome("anna") # True
                >>> is_palindrome("yolo") # False
                >>> is_palindrome("olo") # True
                >>> is_palindrome("alo") # False
        """
        rev = self._word[::-1]
        return rev == self._word
    
    
    def is_kalindrome(self) -> bool:
        """ Returns True if the Word instance is a kalindrome
            ## What is a kalindrome
                - It's possible to select some letter `x` and delete all letters equal to `x`, 
                    so that the remaining word is a palindrome.
            
            ## Examples
                >>> is_kalindrome("anna") # True, nothing to remove, or a or n
                >>> is_kalindrome("yolo") # True, y to remove
                >>> is_kalindrome("aoloc") # False
                >>> is_kalindrome("oaloa") # True, o or a to remove
        """
        unique = []
        word = self._word
        for i in word :
            if i not in unique:
                unique.append(i)
        if word == reversed(word):
            return True

        for letter in unique:
            new_word = word.replace(letter, "")
            if new_word[::-1] == new_word:
                break
            else:
                continue
        return new_word[::-1] == new_word
            
        
        
        
            


if __name__ == "__main__":
    # Here is some material to test your code:
    
    strings_test_1 = ["a","b","c","d"]
    strings_test_2 = ["a","d","e","f"]
    simple = unique_strings(strings_test_1, strings_test_2)
    print(simple)
    assert simple == ["a","b","c","d","e","f"], "unique_strings function failed."
    
    
    strings_test_3 = ["b","d","f","g","h","i"]
    strings_test_4 = ["i","j","k","l","e"]
    multiples = unique_multiple_strings(
        strings_test_1,
        strings_test_2,
        strings_test_3,
        strings_test_4,
    )
    print(multiples)
    assert multiples == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
    
    
    anna = Word("anna")
    melvil = Word("melvil")
    racecar = Word("racecar")
    boby = Word("boby")
    yolo = Word("yolo")
    radars = Word("radar")
    aaaaaaaaabcb = Word("aaaaaaaaabcb")
    aaaaaaabcba = Word("aaaaaaaaabcba")
    
    
    assert anna.is_palindrome() is True, "is_palindrome function is not working properly"
    assert melvil.is_palindrome() is False, "is_palindrome function is not working properly"
    assert racecar.is_palindrome() is True, "is_palindrome function is not working properly"
    assert boby.is_palindrome() is False, "is_palindrome function is not working properly"
    assert yolo.is_palindrome() is False, "is_palindrome function is not working properly"
    
    
    assert melvil.is_kalindrome() is False, "is_kalindrome function is not working properly"
    assert boby.is_kalindrome() is True, "is_kalindrome function is not working properly"
    assert yolo.is_kalindrome() is True, "is_kalindrome function is not working properly"
    assert radars.is_kalindrome() is True, "is_kalindrome function is not working properly"
    assert aaaaaaaaabcb.is_kalindrome() is True, "is_kalindrome function is not working properly"
    assert aaaaaaabcba.is_kalindrome() is True, "is_kalindrome function is not working properly"
    
    
    print("Nice, your code seems to be working.")