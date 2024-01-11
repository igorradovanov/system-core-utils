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

