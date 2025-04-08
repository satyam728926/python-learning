import numpy as np

user_input=int(input("Enter the value of N : "))

array = np.empty((user_input,user_input),dtype=int)

for i in range(1,user_input+1):
    for j in range(i,0,-1):
        array[i-1,j-1]=i+(i-j)*user_input-((i-j)*(i-j+1))/2
print(array)
# # 1
# # 7 2
# # 12 8 3
# # 16 13 9 4
# # 19 17 14 10 5
# # 21 20 18 15 11 6
# Input for N (size of the pattern)
# N = int(input("Enter the value of N: "))

# # List to store the final array
# result = []

# # Initial value
# start_value = 1

# # Loop through each row
# for i in range(N):
#     row = []
#     # Each row starts at 'start_value' and decreases in steps
#     for j in range(i + 1):
#         row.append(start_value)
#         start_value += 1  # Move to the next number
#     result.append(row)  # Add the row to the final result

# # Now, we need to print the numbers in the reverse order for each row
# for i in range(N):
#     print(" ".join(map(str, result[i][::-1])))  # Print each row in decreasing order
