

class Node:
    """
    Class that represents a Node in problem search
    """
    # for BFS queue priority
    moves_priority = {"R": 0, "RD": 1, "D": 2, "LD": 3, "L": 4, "LU": 5, "U": 6, "RU": 7}

    def __init__(self, state, path, depth, cost):
        self.state = state
        self.path = path
        self.depth = depth
        # cost summed by this path
        self.cost = cost

    def solution(self):
        """
        :return: string that represent the path until this node and the cost
        """
        return '{} {}'.format("-".join(self.path), self.cost)

    def get_move_priority(self):
        return self.moves_priority[self.path[-1]]

    # define how to compare nodes
    def __eq__(self, other):
        return self.state == other.state


class SearchProblem:
    """
    Class that represent a search problem on grid.
    The class define also the possible movement on the grid and it's start and goal states
    """
    def __init__(self, grid, start_state, goal_state):
        self.grid = grid
        self.s_start = start_state
        self.s_goal = goal_state

    def is_goal(self, state):
        """
        :param state: state to check if it the goal
        :return: True if the state is the goal, otherwise False
        """
        if state[0] == self.s_goal[0] and state[1] == self.s_goal[1]:
            return True
        return False

    def get_start_node(self):
        """
        :return: start node
        """
        return Node(self.s_start, [], 0, 0)

    def get_successors(self, node):
        """
        :param node: node to get successors from
        :return: all the valid nodes that are possible to go
        """
        all_legal_successors = []
        row = node.state[0]
        col = node.state[1]
        grid_size = len(self.grid)
        cur_path = node.path
        new_depth = node.depth + 1
        cur_cost = node.cost

        # right = R
        if col != grid_size - 1 and self.grid[row][col+1] != -1:
            all_legal_successors.append(Node((row, col+1), cur_path + ["R"], new_depth, cur_cost + self.grid[row][col+1]))

        # right down = RD
        if col != grid_size - 1 and row != grid_size - 1 and self.grid[row+1][col+1] != -1 \
                and self.grid[row][col+1] != -1 and self.grid[row+1][col] != -1:
            all_legal_successors.append(Node((row+1, col+1), cur_path + ["RD"], new_depth, cur_cost + self.grid[row+1][col+1]))

        # down = D
        if row != grid_size - 1 and self.grid[row+1][col] != -1:
            all_legal_successors.append(Node((row+1, col), cur_path + ["D"], new_depth, cur_cost + self.grid[row+1][col]))

        # left down = LD
        if col != 0 and row != grid_size - 1 and self.grid[row+1][col-1] != -1 \
                and self.grid[row+1][col] != -1 and self.grid[row][col-1] != -1:
            all_legal_successors.append(Node((row+1, col-1), cur_path + ["LD"], new_depth, cur_cost + self.grid[row+1][col-1]))

        # left = L
        if col != 0 and self.grid[row][col-1] != -1:
            all_legal_successors.append(Node((row, col-1), cur_path + ["L"], new_depth, cur_cost + self.grid[row][col-1]))

        # left up = LU
        if col != 0 and row != 0 and self.grid[row-1][col-1] != -1 \
                and self.grid[row-1][col] != -1 and self.grid[row][col-1] != -1:
            all_legal_successors.append(Node((row-1, col-1), cur_path + ["LU"], new_depth, cur_cost + self.grid[row-1][col-1]))

        # up = U
        if row != 0 and self.grid[row-1][col] != -1:
            all_legal_successors.append(Node((row-1, col), cur_path + ["U"], new_depth, cur_cost + self.grid[row-1][col]))

        # right up = RU
        if col != grid_size - 1 and row != 0 and self.grid[row-1][col+1] != -1 \
                and self.grid[row-1][col] != -1 and self.grid[row][col+1] != -1:
            all_legal_successors.append(Node((row-1, col+1), cur_path + ["RU"], new_depth, cur_cost + self.grid[row-1][col+1]))

        return all_legal_successors
