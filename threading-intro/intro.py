import threading
import time


def operation(seconds=1):
    print(f'Doing {seconds} operation')
    time.sleep(seconds)


start_time = time.perf_counter()

t1 = threading.Thread(target=operation, args=[2])
t2 = threading.Thread(target=operation, args=[1])

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.perf_counter()

print(f'Overall operation takes {round(end_time - start_time)} seconds to resolve')
