class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(self.get_size())

    def delete(self):
        pass

    def get_max(self):
        return self.storage[-1]

    def get_size(self):
        return len(self.storage) -1

    def __swap(self, i, j):
        self.storage[i], self.storage[j] == self.storage[j], self.storage[i]

    def _bubble_up(self, index):
        parent = index // 2
        if index <= 1:
            return
        elif self.storage[index] > self.storage[parent]:
            #swap parent and index
            self.__swap(index, parent)
            #call _bubble_up on the parent
            self._bubble_up(parent)
        

    def _sift_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.storage) > left and self.storage[largest] < self.storage[left]:
            largest = left
        if len(self.storage) > right and self.storage[largest] < self.storage[right]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self._sift_down(largest)


