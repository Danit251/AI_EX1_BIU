from priorityQueue import PriorityQueueF
NO_PATH = "no path"
MAX_DEPTH = 20


# BFS algorithm
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


# DFS-L algorithm - part of IDS
def dfs_l(problem, limit, pre_opened_nodes):
    cur_opened_nodes = pre_opened_nodes
    frontier = [problem.get_start_node()]
    while frontier:
        node = frontier.pop()

        if problem.is_goal(node.state):
            return node.solution(), cur_opened_nodes

        cur_opened_nodes += 1

        # depth limit
        if node.depth < limit:
            frontier.extend(problem.get_successors(node)[::-1])

    return NO_PATH, cur_opened_nodes


# IDS algorithm
def ids(problem):
    num_opened_nodes = 0
    for depth in range(MAX_DEPTH):
        res, num_opened_nodes = dfs_l(problem, depth, num_opened_nodes)
        if res != NO_PATH:
            return "{} {}".format(res, num_opened_nodes)

    return NO_PATH


# g cost function - return the cost of all the nodes in the path until this node
def g(node):
    return node.cost


# my heuristic function
def h(node, s_goal):
    """
    logic: go on the diagonal as you can until you get the row/column og the goal state than go on row/column
    :param node: start node
    :param s_goal: goal state
    :return: number of minimal steps from node to goal
    """
    diff_row = abs(s_goal[0] - node.state[0])
    diff_col = abs(s_goal[1] - node.state[1])
    return min(diff_col, diff_row) + abs(diff_col - diff_row)


# A* algorithm
def a_start(problem):
    def h_helper(node):
        """
        wrapper for h for getting only node like g
        :param node: node to calculate for it the cost from heuristic
        :return: cost of heuristic
        """
        s_goal = problem.s_goal
        return h(node, s_goal)
    return bfs(problem, f=lambda n: g(n) + h_helper(n))


# ucs algorithm
def ucs(problem):
    return bfs(problem, g)


# IDA* algorithm
def ida_star(problem):
    s_start = problem.get_start_node()
    s_goal = problem.s_goal
    new_limit = h(s_start, s_goal)
    f_limit = 0
    nodes_count = 0

    # dfs-f algorithm - recursive DFS with f function helper function for IDA*
    def dfs_f(node, cost):
        nonlocal new_limit
        nonlocal nodes_count
        nodes_count += 1
        new_f = cost + h(node, s_goal)

        if new_f > f_limit:
            new_limit = min(new_limit, new_f)
            return None

        if problem.is_goal(node.state):
            return node.solution()

        if node.depth < MAX_DEPTH:
            for s in problem.get_successors(node):
                sol = dfs_f(s, cost + g(s))
                if sol:
                    return sol

        return None

    # while find new bigger limit in the limited depth
    while f_limit != new_limit:
        f_limit = new_limit
        new_limit = float('inf')
        res = dfs_f(s_start, 0)
        if res:
            return "{} {}".format(res, nodes_count)

    return NO_PATH


