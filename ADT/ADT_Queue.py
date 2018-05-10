class Queue:
    def __init__(self, init_queue=None):
        if init_queue and isinstance(init_queue, list):
            self.items = init_queue[::-1]
        else:
            self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def hotPotato(namelist, num):
    simqueue = Queue(namelist)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


if __name__ == "__main__":
    print(hotPotato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
