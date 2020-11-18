from priorityQueue import PriorityQueueF
NO_PATH = "no path"
MAX_DEPTH = 20


def bfs(problem, f):
    opened_nodes = 0
    frontier = PriorityQueueF(f)
    frontier.push(problem.get_start_node(), opened_nodes, 0)
    closed_list = set()

    while not frontier.is_empty():

        node = frontier.pop()

        if problem.is_goal(node.state):
            return "{} {}".format(node.solution(), opened_nodes)

        opened_nodes += 1

        # prevents cycles
        closed_list.add(node.state)
        for child in problem.get_successors(node):

            if child.state not in closed_list and child not in frontier:
                frontier.push(child, opened_nodes, child.get_move_priority())
            elif child in frontier and f(child) < frontier.get_item_score(child):
                frontier.remove(child)
                frontier.push(child, opened_nodes, child.get_move_priority())

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


def a_start(problem):
    def h(node):
        s_goal = problem.s_goal
        diff_row = abs(s_goal[0] - node.state[0])
        diff_col = abs(s_goal[1] - node.state[1])
        return min(diff_col, diff_row) + abs(diff_col - diff_row)
    return bfs(problem, f=lambda n: g(n) + h(n))


def ucs(problem):
    return bfs(problem, g)
