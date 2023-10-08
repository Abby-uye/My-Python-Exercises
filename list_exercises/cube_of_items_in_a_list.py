def list_of_numbers_to_cube(numbers):
    cube_of_numbers = []
    for index in range(len(numbers)):
        cube_of_numbers.append(numbers[index] ** 3)
    return cube_of_numbers

cube = [3,7,2,6,5]
print(list_of_numbers_to_cube(cube))
