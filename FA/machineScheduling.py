import heapq

def branch_and_bound(tasks, m):
    if not tasks:                         # If no tasks
        return 0, [], 0

    tasks = sorted(tasks, reverse=True)   # O(n log n)
    n = len(tasks)
    total = sum(tasks)                    # O(n)

    best = float('inf')
    best_assign = None

    heap = []
    heapq.heappush(heap, ((total + m - 1)//m, 0, (0,)*m, []))   # O(1)

    nodes = 0

    while heap:
        lb, i, loads, assign = heapq.heappop(heap)   # O(log k)

        if lb >= best:                               # O(1)
            continue

        if i == n:
            makespan = max(loads)                    # O(m)
            if makespan < best:
                best = makespan
                best_assign = assign[:]
            continue

        seen = set()

        for j in range(m):                           # O(m)
            if loads[j] in seen:
                continue
            seen.add(loads[j])

            new_loads = list(loads)                  # O(m)
            new_loads[j] += tasks[i]

            rem = sum(tasks[i+1:])                   # O(n)
            new_max = max(new_loads)                 # O(m)

            lb_child = max(new_max, (rem + m - 1)//m) if rem else new_max  # O(1)

            if lb_child >= best:                     # O(1)
                continue

            heapq.heappush(heap,                    # O(log k)
                (lb_child, i+1, tuple(new_loads), assign + [(j, tasks[i])])
            )

        nodes += 1

    return best, best_assign, nodes


def lpt(tasks, m):
    if not tasks:                         # If no tasks
        return 0, []

    tasks = sorted(tasks, reverse=True)   # O(n log n)

    heap = [(0, i) for i in range(m)]
    heapq.heapify(heap)                   # O(m)

    assign = []

    for t in tasks:                       # O(n)
        load, i = heapq.heappop(heap)     # O(log m)
        assign.append((i, t))
        heapq.heappush(heap, (load + t, i))  # O(log m)

    makespan = max(load for load, _ in heap)  # O(m)
    return makespan, assign


def run_test(tasks, m, title):
    print("\n" + "="*50)
    print(title)
    print(f"Tasks = {tasks}, Machines = {m}")

    bb_ms, _, _ = branch_and_bound(tasks, m)
    lpt_ms, _ = lpt(tasks, m)

    print(f"B&B Makespan  : {bb_ms}")
    print(f"LPT Makespan  : {lpt_ms}")



# Case 1: Normal case
run_test([8, 7, 6, 5], 2, "Case 1: Normal Input")

# Case 2: Empty task list
run_test([], 3, "Case 2: No Tasks")

# Case 3: Single machine
run_test([4, 3, 2, 1], 1, "Case 3: Single Machine")

# Case 4: More machines than tasks
run_test([10, 5], 5, "Case 4: More Machines than Tasks")

# Case 5: All tasks equal
run_test([5, 5, 5, 5], 2, "Case 5: Equal Tasks")

# Case 6: One very large task
run_test([20, 2, 2, 2], 2, "Case 6: One Large Task")

# Case 7: Already balanced
run_test([6, 6, 6, 6], 2, "Case 7: Perfectly Balanced")