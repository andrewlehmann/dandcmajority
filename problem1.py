import math


def merge(a, b):
	c = []
	if a:
		for i in range(0, len(a)):
			c.append(a[i])
	if b:
		for j in range(0, len(b)):
			c.append(b[j])
	print("C: ", c)
	return c


def Majority(A):
	# print(A)
	if len(A) == 1:
		print(A[0])
		return [A[0]]

	elif len(A) == 2:
		if A[0] == A[1]:
			print(A[0])
			return [A[0]]

		else:
			return A

	else:
		A1 = []
		A2 = []
		mid = math.floor(len(A) / 2)

		for i in range(0, mid):
			A1.append(A[i])

		for j in range(mid, len(A)):
			A2.append(A[j])

		print("A1, A2: ", A1, A2)

		R1 = Majority(A1)
		R2 = Majority(A2)

		print("R1, R2: ", R1, R2)
		if len(A1) == 1:
			if len(A2) == 1:
				return Majority(merge(R1, R2))

			else:
				if R1[0] in R2:
					return [R1[0]]

				else:
					return Majority(R2)

		else:
			if len(A2) == 1:
				if R2[0] in R1:
					print("R2: ", R2[0])
					return [R2[0]]

				else:
					return Majority(R1)

			else:
				return Majority(merge(R1, R2))


def main():
	A = [0, 0, 0, 0, 0, 1, 1, 1, 1]
	counts = {}
	majorityVal = Majority(A)
	print("Most common element", majorityVal)

if __name__ == '__main__':
	main()
