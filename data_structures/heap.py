class Heap:
    """
        mapping an array to a heap
    """

    def __init__(self, array=None):
        self.array = []
        self.max_index = -1
        if array is not None:
            self.array = array
            self.max_index = len(array) - 1

    def append(self, value):
        self.array.append(value)
        self.max_index += 1

    def swap(self, i, j):
        tmp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = tmp

    @staticmethod
    def get_parent_index(index):
        return index // 2

    @staticmethod
    def get_left_index(index):
        return 2 * index

    @staticmethod
    def get_right_index(index):
        return 2 * index + 1

    def get_parent_value(self, index):
        return self.array[self.get_parent_index(index)]

    def get_left_value(self, index):
        return self.array[self.get_left_index(index)]

    def get_right_value(self, index):
        return self.array[self.get_right_index(index)]

    def max_heapify(self, index):
        # do the max_heapify start from the index-th node
        # if index is the largest within [index, left, right] then done
        # else choose the largest as the root of the subtree and
        # do this procedure recursively
        l = self.get_left_index(index)
        r = self.get_right_index(index)
        largest = index
        if l <= self.max_index and self.array[l] > self.array[index]:
            largest = l
        if r <= self.max_index and self.array[r] > self.array[largest]:
            largest = r
        if largest != index:
            self.swap(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self, array=None):
        if array is not None:
            self.array = array
            self.max_index = len(array) - 1
        for i in reversed(range(1 + self.max_index // 2)):
            self.max_heapify(i)

    def descending_sort(self):
        sorted_array = []
        self.build_max_heap()
        tmp = self.max_index
        for i in reversed(range(0, self.max_index + 1)):
            sorted_array.append(self.array[0])
            self.swap(0, i)
            self.max_index -= 1
            self.max_heapify(0)
        self.max_index = tmp
        return sorted_array

    def min_heapify(self, index):
        l = self.get_left_index(index)
        r = self.get_right_index(index)
        smallest = index
        if l <= self.max_index and self.array[l] < self.array[index]:
            smallest = l
        if r <= self.max_index and self.array[r] < self.array[smallest]:
            smallest = r
        if smallest != index:
            self.swap(index, smallest)
            self.min_heapify(smallest)

    def build_min_heap(self, array=None):
        if array is not None:
            self.array = array
            self.max_index = len(array) - 1
        for i in reversed(range(1 + self.max_index // 2)):
            self.min_heapify(i)

    def ascending_sort(self):
        sorted_array = []
        self.build_min_heap()
        tmp = self.max_index
        for i in reversed(range(0, self.max_index + 1)):
            sorted_array.append(self.array[0])
            self.swap(0, i)
            self.max_index -= 1
            self.min_heapify(0)
        self.max_index = tmp
        return sorted_array


if __name__ == '__main__':
    heap = Heap()
    heap.build_max_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
    print(heap.descending_sort())
    print(heap.ascending_sort())
