def Square(X): 
	return (X * X) 

def SumofSquares(numbers, n): 
	Sum = 0
	for i in range(n): 
		SquaredValue = Square(numbers[i]) 
		Sum += SquaredValue 
	return Sum

numbers = [1, 2, 3, 4] 
n = len(numbers) 
 
Total = SumofSquares(numbers, n) 
print("Sum of the Square of List of Numbers:", Total) 
