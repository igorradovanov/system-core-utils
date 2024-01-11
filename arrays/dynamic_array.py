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
