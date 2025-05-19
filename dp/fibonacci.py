def fib_recursion(n):
    if n==1 or n==2:
        return 1
    else: return fib_recursion(n-1) + fib_recursion(n-2)

def fib_iter(n):
    fib_list = []
    for i in range(n):
        if i==0 or i==1:
            fib_list.append(1)
        else: fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list[n-1]

print("# recursion")
print("fib(1)", fib_recursion(1))
print("fib(2)", fib_recursion(2))
print("fib(3)", fib_recursion(3))
print("fib(4)", fib_recursion(4))
print("fib(5)", fib_recursion(5))

print("#iterative")
print("fib(1)", fib_iter(1))
print("fib(2)", fib_iter(2))
print("fib(3)", fib_iter(3))
print("fib(4)", fib_iter(4))
print("fib(5)", fib_iter(5))