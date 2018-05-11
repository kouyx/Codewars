class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:  # Ordered linked list; modify add() and search() for ascending or descending
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        previous = None
        current = self.head
        while current is not None and current.getData() < item:  # Ascending
            previous = current
            current = current.getNext()
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.getData() == item:
                return True
            elif current.getData() > item:
                return False
            else:
                current = current.getNext()
        return False

    def remove(self, item):
        previous = None
        current = self.head
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == "__main__":
    pass
