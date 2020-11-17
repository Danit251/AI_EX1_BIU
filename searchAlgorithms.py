from priorityQueue import PriorityQueueF
NO_PATH = "no path"
MAX_DEPTH = 30
A_STAR_MAX_DEPTH = 20


def bfs(problem, f):
    opened_nodes = 0
    frontier = PriorityQueueF(f)
    frontier.push(problem.get_start_node())
    closed_list = set()

    while not frontier.is_empty():

        node = frontier.pop()
        opened_nodes += 1

        if problem.is_goal(node.state):
            return "{} {}".format(node.solution(), opened_nodes)

        # prevents cycles
        closed_list.add(node.state)
        for child in problem.get_successors(node):

            if child.state not in closed_list and child not in frontier:
                frontier.push(child)
            elif child in frontier and f(child) < frontier.get_item_score(child):
                frontier.remove(child)
                frontier.push(child)

    return NO_PATH


def dfs_l(problem, limit, pre_opened_nodes):
    cur_opened_nodes = pre_opened_nodes
    frontier = [problem.get_start_node()]
    while frontier:
        node = frontier.pop()
        cur_opened_nodes += 1
        if problem.is_goal(node.state):
            return node.solution(), cur_opened_nodes

        # depth limit
        if node.depth < limit:
            frontier.extend(problem.get_successors(node)[::-1])

    return NO_PATH, cur_opened_nodes


def ids(problem):
    num_opened_nodes = 0
    for depth in range(1, MAX_DEPTH):
        res, num_opened_nodes = dfs_l(problem, depth, num_opened_nodes)
        if res != NO_PATH:
            return "{} {}".format(res, num_opened_nodes)

    return NO_PATH


def g(node):
    return node.cost


def ucs(problem):
    return bfs(problem, g)
