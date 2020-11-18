from searchProblem import SearchProblem
from searchAlgorithms import ids, ucs, a_start

IDS_ALGO = "IDS"
UCS_ALGO = "UCS"
A_STAR_ALGO = "ASTAR"
IDA_ALGO = "IDASTAR"


def get_problem_parameters(f_name):
    with open(f_name) as f:
        lines = [l.rstrip() for l in f.readlines()]
        algo = lines[0]
        s_start = tuple([int(x) for x in lines[1].split(",")])
        s_goal = tuple([int(x) for x in lines[2].split(",")])
        grid_size = int(lines[3])
        grid = []
        for g in range(4, 4 + grid_size):
            grid.append([int(x) for x in lines[g].split(",")])

        return algo, s_start, s_goal, grid


def main():
    # TODO: write to file!!!
    algo, s_start, s_goal, grid = get_problem_parameters("input2.txt")
    sp = SearchProblem(grid, s_start, s_goal)
    if algo == IDS_ALGO:
        print(ids(sp))
    elif algo == UCS_ALGO:
        print(ucs(sp))
    elif algo == A_STAR_ALGO:
        print(a_start(sp))


if __name__ == '__main__':
    main()
