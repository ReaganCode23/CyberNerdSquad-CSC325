from time import time

# given functions
def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total

def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total

def example3(S):
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1 + j):
            total += S[k]
    return total

def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total

# runtime functions
def time1(S):
    start_time = time()
    n = range(S)
    example1(n)
    end_time = time()
    T_time = end_time - start_time
    print("Execution time = {}".format(T_time))

def time2(S):
    start_time = time()
    n = range(S)
    example2(n)
    end_time = time()
    T_time = end_time - start_time
    print("Execution time = {}".format(T_time))

def time3(S):
    start_time = time()
    n = range(S)
    example3(n)
    end_time = time()
    T_time = end_time - start_time
    print("Execution time = {}".format(T_time))

def time4(S):
    start_time = time()
    n = range(S)
    example4(n)
    end_time = time()
    T_time = end_time - start_time
    print("Execution time = {}".format(T_time))

if __name__ == '__main__':

    # example1 implementation; data points at 1000, 5000, 10000, 15000
    time1(1000)
    time1(5000)
    time1(10000)
    time1(15000)

    # example2 implementation; data points at 1000, 5000, 10000, 15000
    time2(1000)
    time2(5000)
    time2(10000)
    time2(15000)

    # example3 implementation; data points at 1000, 5000, 10000, 15000
    time3(1000)
    time3(5000)
    time3(10000)
    time3(15000)

    # example4 implementation; data points at 1000, 5000, 10000, 15000
    time4(1000)
    time4(5000)
    time4(10000)
    time4(15000)