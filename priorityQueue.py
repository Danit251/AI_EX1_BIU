import heapq


class PriorityQueueF:
    """
      Implements a priority queue with function data structure. Each inserted item
      has a priority associated with it: from f value then time of insertion (according to father node) then
      priority between directions when right is the most important.
    """
    ITEM_IND = 3

    def __init__(self, priority_f):
        self.queue = []
        self.priority_f = priority_f

    def push(self, item, time, direction_priority):
        """
        :param item: node to insert
        :param time: time of insertion according to father
        :param direction_priority: direction's priority
        :return:
        """
        pair = (self.priority_f(item), time, direction_priority, item)
        heapq.heappush(self.queue, pair)

    def pop(self):
        """
        :return: remove and return from the queue the most preferred node
        """
        return heapq.heappop(self.queue)[self.ITEM_IND]

    def remove(self, item):
        """
        :param item: item to remove
        """
        for tp in self.queue:
            if tp[self.ITEM_IND] == item:
                self.queue.remove(tp)
                break

    def is_empty(self):
        """
        check if the queue is empty
        :return: True if the queue is empty, otherwise False
        """
        return len(self.queue) == 0

    def get_item_score(self, item):
        """
        :param item: item to get score of it
        :return: the score of the item from the priority function
        """
        for f_score, _, _, cur_item in self.queue:
            if cur_item == item:
                return f_score

    def __contains__(self, item):
        """
        check if an item is in the queue
        """
        for _, _, _, cur_item in self.queue:
            if cur_item == item:
                return True
        return False
