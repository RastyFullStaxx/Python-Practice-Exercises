def find_celebrity(n):
    candidate = 0

    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    if is_cele
