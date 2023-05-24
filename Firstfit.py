'''
def add_float_numbers(a:float, b:float):
    return a + b
a:float=4.1
b:float =3.5
result: float = add_float_numbers(a,b)
print(f"The sum of float numbers{a} and {b} is: {result}")




def add_numbers(a: int, b: int):
    return a + b
num1: int = 5
num2: int = 7
result: int = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")




def add_float_numbers(x, y):
    if isinstance(x, float) and isinstance(y, float):
        return x + y
    else:
        raise ValueError("Both arguments must be float numbers.")
x=7.7
y=5.5
result = add_float_numbers(x, y)
print(f"The sum of float numbers{x} and {y} is: {result}")
'''









# Python3 implementation of First-Fit algorithm
 
# Function to allocate memory to
# blocks as per First fit algorithm
def firstFit(blockSize, m, processSize, n):
     
    # Stores block id of the
    # block allocated to a process
    allocation = [-1] * n
 
    # Initially no block is assigned to any process
 
    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                 
                # allocate block j to p[i] process
                allocation[i] = j
 
                # Reduce available memory in this block.
                blockSize[j] =- processSize[i]
 
                break
 
    print(" Process No. Process Size      Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i],
                          "         ", end = " ")
        if allocation[i] != 0:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
 
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
 
    firstFit(blockSize, m, processSize, n)
