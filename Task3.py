"""
Imagine you are leaving your beloved home for a longer vacation.
You leave a few robots at home to take care of it. Their names are Dave, Cris, Nick, Phil and Maxi.

You may give them tasks via a queue, that they will process for you.

The following constraints apply:
1) no more than 3 tasks may be executed in parallel.
2) each robot (Dave for example) can only execute one task at once.
3) each type of task has a rate limit specific to it. This number tells you how often this specific task may be executed per second.
4) the tasks for each robot_name must stay in the same order
​
Your task is to write a task executor that fetches the tasks from the queue and executes them.
It should execute all tasks in the fastest time possible, but there are constraints.

Use of libraries of all kinds is encouraged! 

The code is in python but you may use Java or JavaScript, too. 
If you use python, please use version 3. 

"""
import queue
import time
from concurrent.futures import ThreadPoolExecutor

startTime = time.time()


def get_time_since_start():
    return round(time.time() - startTime, 2)


# definition of our tasks
def clean_the_windows(task_id, robot_name):
    time.sleep(0.3)  # Simulated execution time (0.3 seconds)
    return 'Squeeesh'


def water_the_plants(task_id, robot_name):
    time.sleep(0.7)  # Simulated execution time (0.7 seconds)
    return 'Blub'


def feed_the_cat(task_id, robot_name):
    time.sleep(0.5)  # Simulated execution time (0.5 seconds)
    return 'Meow'


# link task names to functions and rate limiting information
taskConfig = {
    'clean_the_windows': {
        'func': clean_the_windows,
        'rateLimit': 5.0  # Task may only be executed every 5 seconds
    },
    'water_the_plants': {
        'func': water_the_plants,
        'rateLimit': 3.0  # Task may only be executed every 3 seconds
    },
    'feed_the_cat': {
        'func': feed_the_cat,
        'rateLimit': 2.0  # Task may only be executed every 2 seconds
    }
}

# fill queue with jobs that should be done to a robot_name
jobs = queue.Queue()
jobs.put((1, 'Dave', 'clean_the_windows'))
jobs.put((2, 'Dave', 'water_the_plants'))
jobs.put((3, 'Dave', 'clean_the_windows'))
jobs.put((4, 'Dave', 'feed_the_cat'))
jobs.put((5, 'Dave', 'clean_the_windows'))
jobs.put((6, 'Cris', 'water_the_plants'))
jobs.put((7, 'Cris', 'clean_the_windows'))
jobs.put((8, 'Cris', 'clean_the_windows'))
jobs.put((9, 'Cris', 'feed_the_cat'))
jobs.put((10, 'Cris', 'water_the_plants'))
jobs.put((11, 'Maxi', 'clean_the_windows'))
jobs.put((12, 'Maxi', 'water_the_plants'))
jobs.put((13, 'Maxi', 'clean_the_windows'))
jobs.put((14, 'Maxi', 'feed_the_cat'))
jobs.put((15, 'Maxi', 'clean_the_windows'))
jobs.put((16, 'Nick', 'water_the_plants'))
jobs.put((17, 'Nick', 'clean_the_windows'))
jobs.put((18, 'Nick', 'clean_the_windows'))
jobs.put((19, 'Nick', 'feed_the_cat'))
jobs.put((20, 'Nick', 'water_the_plants'))
jobs.put((21, 'Phil', 'clean_the_windows'))
jobs.put((22, 'Phil', 'water_the_plants'))
jobs.put((23, 'Phil', 'clean_the_windows'))
jobs.put((24, 'Phil', 'feed_the_cat'))
jobs.put((25, 'Phil', 'clean_the_windows'))
jobs.put((26, 'Dave', 'water_the_plants'))
jobs.put((27, 'Dave', 'clean_the_windows'))
jobs.put((28, 'Dave', 'clean_the_windows'))
jobs.put((29, 'Dave', 'feed_the_cat'))
jobs.put((30, 'Dave', 'water_the_plants'))

####################################################################
#################### START ASSIGNMENT BELOW ########################
####################################################################


executor = ThreadPoolExecutor(max_workers=3)
prev_task = []

# execute the jobs
while not jobs.empty():
    job = jobs.get()
    task_id = job[0]
    robot_name = job[1]
    function_name = job[2]
    
    
    taskFunction = taskConfig[function_name]['func']
    taskFunctionLimit = taskConfig[function_name]['rateLimit']      
       
   
    task1 = executor.submit(taskFunction,task_id, robot_name)
    
    if len(prev_task) > 0:
        if prev_task[0] == function_name:
            if function_name == 'clean_the_windows':
                time.sleep(5)
            elif function_name == 'water_the_plants':
                time.sleep(3) 
            else:
                time.sleep(2)
    
    print(task1.result())
    prev_task.clear()
    prev_task.append(function_name)
    
       

print('done')
