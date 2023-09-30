import threading
import multiprocessing

def worker_thread():
    print("Thread task")

def worker_process():
    print("Process task")

if __name__ == "__main__":
    thread = threading.Thread(target=worker_thread)
    process = multiprocessing.Process(target=worker_process)

    thread.start()
    process.start()

    thread.join()
    process.join()
