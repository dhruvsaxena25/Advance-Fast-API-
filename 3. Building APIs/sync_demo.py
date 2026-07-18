import time
from timeit import default_timer as timmer

def run_task(name, seconds):
    print(f'{name} started at: {timmer()}')
    time.sleep(seconds)
    print(f'{name} completed at: {timmer()}')
    
start = timmer()

run_task('Task-1', 2)
run_task('Task-2', 1)
run_task('Task-3', 3)

print(f'\nTotal time taken: {timmer() - start:.2f} s')

