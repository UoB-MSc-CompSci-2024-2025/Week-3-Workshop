def sum_rows(matrix, row):
    if row == 0:
        row_sum = sum(matrix[row])
        print(row_sum)
    elif row == 1:
        print(sum(matrix[row]))
    elif row == 2:
        print(sum(matrix[row]))
        

def sum_column(matrix, column):
    col = []
    for value in matrix:
        col.append(value[column])
    print(sum(col))
            

def change_value(matrix, row_num, col_num, value):
    matrix[row_num][col_num] = value
    matrix[row_num][col_num] = value
    return matrix


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    decision = int(input("Would you like to 1. Find the sum of a row; 2. Find the sum of a column; 3. Change a value in the matrix? "))
    match decision:
        case 1:
            row = int(input("Which row would you like to find the sum of? "))
            sum_rows(matrix, row)
        case 2:
            column = int(input("Which column would you like to find the sum of? "))
            sum_column(matrix, column)
        case 3:
            row_num = int(input("Which row would you like to change? "))
            col_num = int(input("Which column would you like to change? "))
            value = int(input("What number would you like to insert into the matrix? "))
            change_value(matrix, row_num, col_num, value)
            print(matrix)

if __name__ == "__main__":
    main()