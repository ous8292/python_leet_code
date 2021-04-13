class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # take index i of word 1 and add two third
        # take index i of word 2 and add two third, after index of word 1

        # loop through this process until reaching the end
        # if one of the inputs(word) is longer, use .append on final list to add remainding letters of the longer word

        word3 = ''

        '''  
        for i, letter in enumerate(word1):
            word3 += word1[i] + word2[i]
        return word3 
        '''

        i = 0

        while i <= len(word1) - 1 and i <= len(word2) - 1:
            word3 += word1[i] + word2[i]
            i += 1
        if i <= len(word1) - 1:
            word3 += word1[i:]
        elif i <= len(word2) - 1:
            word3 += word2[i:]
        return word3

        # word1              #word2
        # abc                #dfg

        # word3
        # word1[0] = a + word2[0] =d     =ad
        # loop   #word1[1] = b + word2[1] =f     =bf
        # loop   #word1[2] = c + word2[2] =g     =cg



        #i is place not value
        #lity[i] is the actual thing same as using word 'letter' or something
