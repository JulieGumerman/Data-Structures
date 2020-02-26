class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        pass

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def __swap(self, i, j):
            self.heap[i], self.heap[j] == self.heap[j], self.heap[i]

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
        pass
