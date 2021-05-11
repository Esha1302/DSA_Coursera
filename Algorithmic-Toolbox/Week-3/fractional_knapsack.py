# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	if capacity == 0:
		return 0

	dec_list = [] 
	for i in range(n):
		v, w = values[i], weights[i]
		if v == 0:
			continue
		dec_list.append((v, w))

	dec_list.sort(key = lambda x: x[0]/x[1], reverse=True)

	value = 0.0000

	for v,w in dec_list:

		if capacity==0:
			return value

		a = min(w, capacity)

		value += a*(v/w)
		capacity = capacity - a

	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
