from searchProblem import SearchProblem
from searchAlgorithms import ids, ucs, a_start, ida_star

INPUT_F = "input.txt"
OUTPUT_F = "output.txt"
IDS_ALGO = "IDS"
UCS_ALGO = "UCS"
A_STAR_ALGO = "ASTAR"
IDA_STAR_ALGO = "IDASTAR"


def get_problem_parameters(f_name):
    """
    parse the input file and return the parameters for the problem
    :param f_name: name of the input file
    :return: all the parameters for solving the problem
    """
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


def write_sol_to_file(sol):
    """
    write the solution to a file
    :param sol: solution description
    """
    with open(OUTPUT_F, "w") as f:
        f.write(sol)


def main():
    """
    open an input file and the solution write to an output file
    """
    algo, s_start, s_goal, grid = get_problem_parameters(INPUT_F)
    sp = SearchProblem(grid, s_start, s_goal)

    sol = ""
    if algo == IDS_ALGO:
        sol = ids(sp)
    elif algo == UCS_ALGO:
        sol = ucs(sp)
    elif algo == A_STAR_ALGO:
        sol = a_start(sp)
    elif algo == IDA_STAR_ALGO:
        sol = ida_star(sp)

    write_sol_to_file(sol)


if __name__ == '__main__':
    main()
