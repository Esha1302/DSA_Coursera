# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    l = []
    
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        
        l.append(0)
        l.append(1)

        for i in range(2, n+1):
            l.append(int(l[i-1]+l[i-2])%10)
            
        return l[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
