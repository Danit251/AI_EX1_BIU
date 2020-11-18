import heapq


class PriorityQueueF:
    """
      Implements a priority queue with function data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue.
    """
    ITEM_IND = 3

    def __init__(self, priority_f):
        self.queue = []
        self.priority_f = priority_f

    def push(self, item, time, priority):
        pair = (self.priority_f(item), time, priority, item)
        heapq.heappush(self.queue, pair)

    def pop(self):
        return heapq.heappop(self.queue)[self.ITEM_IND]

    def remove(self, item):
        for tp in self.queue:
            if tp[self.ITEM_IND] == item:
                self.queue.remove(tp)
                break

    def is_empty(self):
        return len(self.queue) == 0

    def get_item_score(self, item):
        for f_score, _, _, cur_item in self.queue:
            if cur_item == item:
                return f_score

    def __contains__(self, item):
        for _, _, _, cur_item in self.queue:
            if cur_item == item:
                return True
        return False
