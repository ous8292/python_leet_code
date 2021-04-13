class Solution:
    def restoreString(self, word_list: str, number_list: List[int]) -> str:
        # create unscrambled list
        unscrambled = [None] * len(word_list)

        for i, word in enumerate(word_list):  # for i and word enumerate word list
            unscrambled[number_list[i]] = word  # unscrambled of number list of i is word,
        return ''.join(unscrambled)

        # word_list = asd               number_list = [2,1,0]

        # unscambled = [1 ,2 ,3]


