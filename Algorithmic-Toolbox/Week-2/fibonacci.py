# Uses python3
def calc_fib(n):
	l = []
	if n==0:
		return 0
	elif n==1:
		return 1
	else:
		l.append(0)
		l.append(1)

		for i in range(2, n+1):
			l.append(l[i-1]+l[i-2])
			
		return l[n]

n = int(input())
print(calc_fib(n))
