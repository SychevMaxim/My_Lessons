def summ(N):
	sum_number = 0
	for number in range(1, N + 1):
		sum_number += number
	return  sum_number
	print(sum_number)
def secondSum(totalNumber):
	for number in range(1, totalNumber):
		totalNumber += number
	return totalNumber

N = int(input("Введите число"))
totalNumber = summ(N)
print("Сумма чисел от 1 до", N, "=",totalNumber)
totalNumber = secondSum(totalNumber)
print("Сумма чисел от 1 до", summ(N), "=", totalNumber )
