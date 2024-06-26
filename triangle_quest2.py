#Triangle Quest

# You are given a positive integer .
# Your task is to print a palindromic triangle of size .

for i in range(1, int(input()) + 1): 
    print((10**i // 9)**2)