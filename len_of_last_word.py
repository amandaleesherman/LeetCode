class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split() #.split() splits on default on whitespace (spaces, tabs, and newlines)
        return len(arr[-1])
    #beats 100% of solns, 100% accuracy

'''class Solution:
    def checkIfSubsetOfArrayIsEmpty(self, i, arr):
        if arr[i] != "": #if last index has some content in it
            return len(arr[i])
        return self.checkIfSubsetOfArrayIsEmpty(i - 1, arr) #traverse backward thru array and recursively call helper fcn upon last n indexes until find non empty index 

    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(" ") #.split() splits on default on whitespace (spaces, tabs, and newlines)
        return self.checkIfSubsetOfArrayIsEmpty(len(arr) - 1, arr) #check upon last index
        #beats 100% of solns, 100% accuracy'''