class Solution:
    def int_to_array(self, num): #helper fcn to convert int to array
        #every time add new fcn, have got to add self as parameter
        if num == 0:
            return [] #gotta ret an array
        else:
            return self.int_to_array(num // 10) + [num % 10] #if call another method besides the main one, have got to use self.

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False #neg #'s are NOT palindromes
        arr = self.int_to_array(x)
        #reverse = arr.reverse()
        #reverse modifies original list in place, it does NOT create a copy
        reverse = arr[::-1] #this is how you reverse the list using python slicing
        if arr == reverse: 
            return True
        return False
    #beats 5% of solns, 100% accuracy
