# def right_angled(n):
#     for i in range(1,n+1):
#         print("*"*i)

# right_angled(5)

# def right_angle_continous_numbers(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j, end=" ")
#         print()
# right_angle_continous_numbers(5)

# def right_angle_with_numbers(n):
#     for i in range(1,n+1):
#         print(f"{i} "*i)

# right_angle_with_numbers(5)

# def star_rectangle(n):
#     for i in range(n):
#         print("*"*n)

# star_rectangle(5)


# def inverted_right_angle_triangle(n):
#     for i in range(n,0,-1):
#         print("*"*i)

# inverted_right_angle_triangle(5)

# def inverted_right_angle_triangle_numbered(n):
#     s = "".join(str(i) for i in range(1,n+1))
#     for i in range(n):
#         print(s[:n-i])

# inverted_right_angle_triangle_numbered(5)


# def pyramid(n):
#     for i in range(1,n+1):
#         print(" "*(n-i) + "*"*(2*i-1) + " "*(n-i))

# pyramid(5)

# def inverted_pyramid(n):
#     for i in range(n):
#         print(" "*i + "*"*(2*(n-i)-1) + " "*i)
    
# inverted_pyramid(5)

# def increasing_number_triangle(n):
#     num = 1
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(num, end=" ")
#             num += 1
#         print()
# increasing_number_triangle(3)

# def increasing_letter_triangle(n):
#     final_letter = 65 + n
#     for i in range(65, final_letter):
#         for j in range(65,i+1):
#             print(chr(j), end=" ")
#         print()
# increasing_letter_triangle(5)

def decreasing_letter_triangle(n):
    final_letter = 65 + n
    for i in range(final_letter, 65, -1):
        print()
decreasing_letter_triangle(5)