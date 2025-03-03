class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        modified_arr = [] #create list to store modified array
        for i in range(len(arr)): #iterate through array
#             if element is 0 append twice
            if arr[i] == 0: 
                modified_arr.append(0)
                modified_arr.append(0)
#                 otherwise append the element
            else:
                modified_arr.append(arr[i])
#         copy the modified array back into original array
        for i in range(len(arr)):
            arr[i] = modified_arr[i]