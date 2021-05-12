import random

from pprint import pprint

def init_matrix():
    N = 10
    matrix = []
    for i in range(N):
        matrix.append([])
        for j in range(N):
            matrix[i].append(random.randint(0, 100))
    return matrix

def first_coordinates():
    print("Enter first coordinates")
    i1 = int(input())
    j1 = int(input())
    return i1,j1

def coordinates():
    print("Enter coordinates")
    i_x = int(input())
    j_y= int(input())
    return i_x,j_y

def rel_coordinates(i1,j1,i_x,j_y):
    j_result = i1 - i_x
    i_result = j_y - j1
    print(i_result, j_result)
    return i_result,j_result

def show_el(matrix,i1,j1,i_x,j_y,i_result,j_result):
    print("Matrix:\n")
    pprint(matrix)
    print("\nFirst and second coordinates:\n")
    print(f'{i1} {j1} \n{i_x} {j_y}')
    print("\n Data of first coordinates:\n")
    print(matrix[i1-1][j1-1])
    print("\n Data of second coordinates:\n")
    print(matrix[i_x-1][j_y-1])
    print("\n Rel coordinates:\n")
    print(i_result,j_result)
    
    
def main():
    matrix = init_matrix()
    i1, j1 = first_coordinates()
    i_x, j_y = coordinates()
    i_result, j_result = rel_coordinates(i1,j1,i_x,j_y)
    show_el(matrix,i1,j1,i_x,j_y,i_result,j_result)

if __name__ == '__main__':
    main()