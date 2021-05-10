# Uses python3
import sys

def gcd_naive(a, b):
	if b==0:
		return a
	else:
		a = a%b
		res = gcd_naive(b, a)
		return res

def lcm_naive(a, b):
    gcd = gcd_naive(a,b)

    return int((a*b)/gcd)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

