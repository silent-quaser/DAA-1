# ---------------- Check if Queen Placement is Safe ----------------
def is_safe(board, row, col):
    for prev_row in range(row):
        placed_col = board[prev_row]

        # Same column
        if placed_col == col:
            return False

        # Same diagonal
        if abs(prev_row - row) == abs(placed_col - col):
            return False

    return True


# ---------------- Solve N-Queens using Backtracking ----------------
def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):

        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row] = col

                backtrack(row + 1)

                # Backtrack
                board[row] = -1
                backtrack_count[0] += 1

    backtrack(0)

    return solutions, backtrack_count[0]


# ---------------- Display Chess Board ----------------
def display_board(solution, n):

    print(" +" + "---+" * n)

    for row in range(n):

        print(" |", end="")

        for col in range(n):

            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")

        print()
        print(" +" + "---+" * n)


# ---------------- Main ----------------
def main():

    for n in [4, 6, 8]:

        solutions, backtracks = solve_n_queens(n)

        print(f"N = {n}")
        print(f"Number of Solutions : {len(solutions)}")
        print(f"Backtracks          : {backtracks}")
        print()

        # Display only 4-Queen solutions
        if n == 4:

            print("All Solutions for 4-Queens\n")

            for i, solution in enumerate(solutions, start=1):

                print(f"Solution {i}: {solution}")
                display_board(solution, n)
                print()


if __name__ == "__main__":
    main()