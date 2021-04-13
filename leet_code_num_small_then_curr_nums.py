
"""
1365. How Many Numbers Are Smaller Than the Current Number


Given the array nums,
for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        # create a new list
        listy = [None] * len(nums)  # creating an empty list with the amount of things in numbs (this is similar to the idea of hard copy)
        # has to loop through the beginning of the list also up to the point where your at
        for i in range(len(nums)):
            # create loop counter
            loopy_counter = 0
            # nested loop that starts over at the begining of the loop
            for j in range(len(nums)):
                # condininal
                if j != i and nums[j] < nums[i]:
                    loopy_counter += 1  # compares the two index values
            listy[i] = loopy_counter
        return listy   # return list that is the same size as original list


