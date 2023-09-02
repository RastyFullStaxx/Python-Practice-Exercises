import multiprocessing

def square_number(number):
    return number * number

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    pool = multiprocessing.Pool(processes=len(numbers))
    results = pool.map(square_number, numbers)
    pool.close()
    pool.join()

    print("Original numbers:", numbers)
    print("Squared numbers:", results)
