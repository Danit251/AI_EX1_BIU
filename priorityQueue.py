import heapq

class PriorityQueueF:
    """
      Implements a priority queue with function data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue.
    """

    def __init__(self, priority_f):
        self.queue = []
        self.priority_f = priority_f

    def push(self, item):
        pair = (self.priority_f(item), item)
        heapq.heappush(self.queue, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.queue)
        return item

    def remove(self, item):
        for pair in self.queue:
            if pair[1] == item:
                self.queue.remove(pair)
                break

    def is_empty(self):
        return len(self.queue)

    def get_item_score(self, item):
        for score, cur_item in self.queue:
            if cur_item == item:
                return score

    def __contains__(self, item):
        return item in self.queue
