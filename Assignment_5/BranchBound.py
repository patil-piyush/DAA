from queue import Queue
import heapq


def sort_items(items):
    n = len(items)
    for i in range(n):
        for j in range(i+1, n):
            if items[i][0]/items[i][1] < items[j][0]/items[j][1]:
                items[i], items[j] = items[j], items[i]
    return items


# Bound function
def bound(level, profit, weight, W, items):
    if weight > W:
        return 0

    total_profit = profit
    total_weight = weight
    i = level + 1

    while i < len(items) and total_weight + items[i][1] <= W:
        total_weight += items[i][1]
        total_profit += items[i][0]
        i += 1

    if i < len(items):
        total_profit += (W - total_weight) * (items[i][0] / items[i][1])

    return total_profit


# FIFO 
def fifo_knapsack(items, W):
    q = Queue()
    q.put((-1, 0, 0))   
    max_profit = 0

    while not q.empty():
        level, profit, weight = q.get()

        if level == len(items) - 1:
            continue

        new_weight = weight + items[level+1][1]
        new_profit = profit + items[level+1][0]

        if new_weight <= W and new_profit > max_profit:
            max_profit = new_profit

        if bound(level+1, new_profit, new_weight, W, items) > max_profit:
            q.put((level+1, new_profit, new_weight))

        if bound(level+1, profit, weight, W, items) > max_profit:
            q.put((level+1, profit, weight))

    return max_profit


# LC 
def lc_knapsack(items, W):
    pq = []
    heapq.heappush(pq, (-bound(-1,0,0,W,items), -1, 0, 0))
    max_profit = 0

    while pq:
        _, level, profit, weight = heapq.heappop(pq)

        if level == len(items) - 1:
            continue

        new_weight = weight + items[level+1][1]
        new_profit = profit + items[level+1][0]

        if new_weight <= W and new_profit > max_profit:
            max_profit = new_profit

        b = bound(level+1, new_profit, new_weight, W, items)
        if b > max_profit:
            heapq.heappush(pq, (-b, level+1, new_profit, new_weight))

        b = bound(level+1, profit, weight, W, items)
        if b > max_profit:
            heapq.heappush(pq, (-b, level+1, profit, weight))

    return max_profit


tests = [
    ([(60,10),(100,20),(120,30)], 50),
    ([(10,5),(40,4),(30,6),(50,3)], 10)
]

for i in range(len(tests)):
    items, W = tests[i]

    items = sort_items(items)

    print("\nTest Case", i+1)
    print("FIFO:", fifo_knapsack(items, W))
    print("LC:", lc_knapsack(items, W))