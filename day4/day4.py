def find_xmas(matrix):
    result = 0

    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    
    # Define directions: up, down, left, right, and diagonals
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'X':
                # Check all adjacent positions for 'M'
                for dir_row, dir_col in directions:
                    # Check the next positions (M, A, S) in the same direction
                    new_pos_row, new_pos_col = r + dir_row, c + dir_col
                    if 0 <= new_pos_row < rows and 0 <= new_pos_col < cols and matrix[new_pos_row][new_pos_col] == 'M':
                        new_pos_row_2, new_pos_col_2 = new_pos_row + dir_row, new_pos_col + dir_col
                        if 0 <= new_pos_row_2 < rows and 0 <= new_pos_col_2 < cols and matrix[new_pos_row_2][new_pos_col_2] == 'A':
                            new_pos_row_3, new_pos_col_3 = new_pos_row_2 + dir_row, new_pos_col_2 + dir_col
                            if 0 <= new_pos_row_3 < rows and 0 <= new_pos_col_3 < cols and matrix[new_pos_row_3][new_pos_col_3] == 'S':
                                result += 1
    return result

def find_x_mas(matrix):
    result = 0

    rows, cols = len(matrix), len(matrix[0]) if matrix else 0
    
    # Define directions for diagonals (top-left ↔ bottom-right and top-right ↔ bottom-left)
    directions = [(-1, -1), (-1, 1)]
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'A':  # Find 'A'
                mas_found = 0
                for dir_row, dir_col in directions:
                    # Calculate positions for 'M' and 'S' based on direction
                    first_diag_r, first_diag_c = r + dir_row, c + dir_col  # Check top-left or top-right diagonal
                    second_diag_r, second_diag_c = r - dir_row, c - dir_col  # Opposite diagonal (bottom-right or bottom-left)
                    
                    # Check if we found 'M' or 'S' in the first diagonal
                    if 0 <= first_diag_r < rows and 0 <= first_diag_c < cols and matrix[first_diag_r][first_diag_c] in ['M', 'S']:
                        # Check for the opposite symbol in the second diagonal
                        expected_symbol = 'S' if matrix[first_diag_r][first_diag_c] == 'M' else 'M'
                        
                        if 0 <= second_diag_r < rows and 0 <= second_diag_c < cols and matrix[second_diag_r][second_diag_c] == expected_symbol:
                            mas_found += 1  # We encountered one diagonal 'MAS'

                if mas_found == 2:  # If there is a cross (two diagonal 'MAS')
                    result += 1
    return result

def main() -> None:
    with open('input.txt', 'r') as f:
        matrix = [list(line.strip()) for line in f.readlines()]

        print(f"Answer 1: {find_xmas(matrix)}")
        print(f"Answer 2: {find_x_mas(matrix)}")


if __name__ == "__main__":
    main()