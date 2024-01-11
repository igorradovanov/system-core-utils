class DynamicArray:
    """
    A dynamic array implementation that allows for resizing as needed.
    """

    def __init__(self, capacity: int):
        """
        Initializes a new instance of the DynamicArray class.

        Args:
            capacity (int): The initial capacity of the array.
        """
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        """
        Retrieves the element at the specified index.

        Args:
            i (int): The index of the element to retrieve.

        Returns:
            int: The element at the specified index, or -1 if the index is out of range.
        """
        # Reject if i is greater than arr size
        if i >= self.size:
            return -1
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        """
        Sets the value at index i in the dynamic array.

        Args:
            i (int): The index at which to set the value.
            n (int): The value to set.

        Returns:
            None
        """
        # Reject if asking for i out of bound
        if self.size == 0:
            return -1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        """
        Adds an element to the end of the dynamic array.

        Args:
            n (int): The element to be added.

        Returns:
            None
        """
        if self.size == self.capacity:
            self.resize()

        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """
        Removes and returns the last element from the dynamic array.

        Returns:
            int: The value of the last element that was removed.

        Raises:
            IndexError: If the dynamic array is empty.
        """
        # Soft deletion
        self.size -= 1
        return self.arr[self.size]
