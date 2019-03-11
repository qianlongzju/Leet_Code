def BFS(root, target):
    queue = []  # store all nodes which are waiting to be processed
    step = 0    # number of steps neeeded from root to current node
    # initialize
    add root to queue
    # BFS
    while queue is not empty:
        step += 1
        # iterate the nodes which are already in the queue
        size = len(queue)
        for i in range(size):
            cur = the first node in queue
            return step if cur is target
            for next_node in the neighbors of cur:
                add next_node to queue
            remove the first node from queue;
    return -1     # there is no path from root to target

# no duplicate visit
def BFS(root, target):
    queue = []   # store all nodes which are waiting to be processed
    used = set() #store all the used nodes
    step = 0     # number of steps neeeded from root to current node
    # initialize
    add root to queue
    add root to used
    # BFS
    while queue is not empty:
        step += 1
        # iterate the nodes which are already in the queue
        size = len(queue)
        for i in range(size):
            cur = the first node in queue
            return step if cur is target
            for next_node in the neighbors of cur:
                if next_node is not in used:
                    add next_node to queue
                    add next_node to used
            remove the first node from queue;
    return -1     # there is no path from root to target
