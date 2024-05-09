# To schedule task based on the algorithm
# 1. remove the task with the smallest start time
# 2. if there is a machine with no task conflicting with it then schedule it on that machine
# 3. Else schedule it on a new machine
def task_scheduling(tasks):
    # Sort tasks based on their start time in ascending order
    tasks.sort(key=lambda x: x[1])

    schedule = []
    machines = []

    for task, start_time, end_time in tasks:
        min_start_time = float('inf')
        non_conflicting_machine_index = None
        for i, machine in enumerate(machines):
            if machine[-1][2] <= start_time and machine[-1][2] < min_start_time:
                min_start_time = machine[-1][2]
                non_conflicting_machine_index = i

        if non_conflicting_machine_index is not None:
            machines[non_conflicting_machine_index].append((task, start_time, end_time))
        else:
            machines.append([(task, start_time, end_time)])

    for i, machine in enumerate(machines):
        schedule.extend(task for task, _, _ in machine)
        print(f"Machine {i + 1} Schedule:", [task for task, _, _ in machine])

    return schedule


# Example usage:
tasks = [("Task1", 1, 3), ("Task2", 1, 4), ("Task3", 2, 5), ("Task4", 3, 7), ("Task5", 4, 7), ("Task6", 6, 9), ("Task7", 7, 8)]
task_scheduling(tasks)
