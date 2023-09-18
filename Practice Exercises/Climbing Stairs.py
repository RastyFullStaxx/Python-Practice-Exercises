def climb_stairs(n):
    if n <= 2:
        return n

    prev, current = 1, 2
    for i in range(3, n + 1):
        prev, current = current, prev + current

    return current

n_steps = 4
result = climb_stairs(n_steps)
print(result)
