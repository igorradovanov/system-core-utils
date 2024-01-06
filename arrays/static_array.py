from typing import List

class StaticArray:
    def insertEnd(self, arr, n, length, capacity):
        """
        Inserts an element at the end of the array.

        Args:
            arr (list): The array to insert the element into.
            n: The element to be inserted.
            length (int): The current length of the array.
            capacity (int): The maximum capacity of the array.

        Returns:
            None
        """
        if length < capacity:
            arr[length] = n

    def removeEnd(self, arr, length):
        """
        Removes the element at the end of the array and updates the length.

        Args:
            arr (list): The array from which the element needs to be removed.
            length (int): The current length of the array.

        Returns:
            None
        """
        if length > 0:
            # Overwrite value and decrease the length
            arr[length - 1] = 0

    def insertMiddle(self, arr, i, n, length):
        """
        Inserts an element at the middle index of the array and shifts the remaining elements to the right.

        Args:
            arr (list): The input array.
            i (int): The index at which the element needs to be inserted.
            n: The element to be inserted.
            length (int): The length of the array.

        Returns:
            None
        """
        for index in range(length - 1, i - 1, -1):
            arr[index + 1] = arr[index]
        arr[i] = n

    def removeMiddle(self, arr, i, length):
        """
        Removes the element at the middle index of the array and shifts the remaining elements to the left.

        Args:
            arr (list): The input array.
            i (int): The index of the middle element to be removed.
            length (int): The length of the array.

        Returns:
            None
        """
        for index in range(i + 1, length):
            arr[index - 1] = arr[index]
            

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Removes duplicates from the given list of integers.

        Args:
            nums (List[int]): The list of integers.

        Returns:
            int: The length of the modified list without duplicates.
        """
        l = 1
        for r in range(1, len(nums)):
            if(nums[r] != nums[r-1]):
                nums[l] = nums[r]
                l = l + 1
        return l

    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of a specified value from the given list.

        Args:
            nums (List[int]): The list of integers.
            val (int): The value to be removed.

        Returns:
            int: The new length of the list after removing the specified value.
        """
        i, j = 0, 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        length = len(nums) // 2
        left = nums[:length]
        right = nums[length:]
        
        for x in range(len(left)):
            arr.append(left[x])
            arr.append(right[x])
        return arr