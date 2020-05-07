import concurrent.futures
import time

def do_sth(seconds):
    print(f'Staring a {seconds} seconds operation')
    time.sleep(seconds)
    return f'Done {seconds} seconds task'


start_time = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executer:
    secs = [4, 2, 5, 1]
    # results = [ executer.submit(do_sth, sec) for sec in secs ]
    # for f in concurrent.futures.as_completed(results):
        # print(f.result())
   
    results = executer.map(do_sth, secs)
    for r in results:
         print(r)
   

end_time = time.perf_counter()

print(f'It takes {round(end_time - start_time)} seconds to resolve in total') 

