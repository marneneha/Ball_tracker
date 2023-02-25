import numpy as np 
import copy
from pprint import pprint
from collections import deque

# print("type the matrix row-wise and enter 0 in space of blank space")
# for i in range (9):
#     val = int(input())
#     input_mat = np.append(input_mat, val)
# input_mat = np.reshape(input_mat, (3,3))

input_mat = np.array([[1,2,0], [4,6,3], [7,5,8]])
node_list = deque([input_mat])
global goal_node, match_found
match_found = False
goal_node = np.array([[1,2,3],[4,5,6],[7,8,0]])
generated_graph = {}
visited_nodes = [input_mat]
def goal_node_check(input_node_copy):
    global match_found
    if(np.array_equal(goal_node, input_node_copy)):
        match_found = True
        print("match found")

def previous_node_check(input_node_copy):
    for i in (node_list):
        if(np.array_equal(i, input_node_copy)):
            return True

def add_right_node(node, index_i, index_j):
    if (index_j != 2):
            input_node_copy = copy.deepcopy(node)
            input_node_copy[index_i, [index_j,index_j+1]] = input_node_copy[index_i, [index_j+1,index_j]]
            goal_node_check(input_node_copy)
            if(previous_node_check(input_node_copy)):
                return False
            node_list.append(input_node_copy)
            visited_nodes.append(input_node_copy)
            return True

def add_left_node(node, index_i, index_j):
    if (index_j != 0):
            input_node_copy = copy.deepcopy(node)
            input_node_copy[index_i, [index_j,index_j-1]] = input_node_copy[index_i, [index_j-1,index_j]]
            goal_node_check(input_node_copy)
            if(previous_node_check(input_node_copy)):
                return False
            node_list.append(input_node_copy)
            visited_nodes.append(input_node_copy)
            return True

def add_up_node(node, index_i, index_j):
    if (index_i != 0):
            input_node_copy = copy.deepcopy(node)
            input_node_copy[[index_i,index_i-1], index_j] = input_node_copy[[index_i-1,index_i], index_j]
            goal_node_check(input_node_copy)
            if(previous_node_check(input_node_copy)):
                return False
            node_list.append(input_node_copy)
            visited_nodes.append(input_node_copy)
            return True

def add_down_node(node, index_i, index_j):
    if (index_i != 2):
            input_node_copy = copy.deepcopy(node)
            input_node_copy[[index_i,index_i+1], index_j] = input_node_copy[[index_i+1,index_i], index_j]
            goal_node_check(input_node_copy)
            if(previous_node_check(input_node_copy)):
                return False
            node_list.append(input_node_copy)
            visited_nodes.append(input_node_copy)
            return True

def generate_children(node):
    global node_list, match_found, input_mat, global_node_count
    index = np.argwhere(node == 0)
    index_i = index[0, 0]
    index_j = index[0, 1]
    children_list =[]
    if(not match_found):
        if(add_down_node(node, index_i, index_j)):
            global_node_count = global_node_count+1
            children_list.append(global_node_count)
    if(not match_found):
        if(add_right_node(node, index_i, index_j)):
            global_node_count = global_node_count+1
            children_list.append(global_node_count)
    if(not match_found):
        if(add_left_node(node, index_i, index_j)):
            global_node_count = global_node_count+1
            children_list.append(global_node_count)
    if(not match_found):
        if(add_up_node(node, index_i, index_j)):
            global_node_count = global_node_count+1
            children_list.append(global_node_count)
    return children_list
i =1
node_count_iterator = 1
global_node_count = 1
while(not match_found):
    children_list  = generate_children(node_list[0])
    generated_graph[node_count_iterator] = children_list
    node_count_iterator=node_count_iterator+1
    node_list.popleft()
    # print("node list is")
    # pprint(node_list)

    i =i+1

def bfs(graph, init_node, end_node):
    queue = []
    queue.append([init_node])
    while queue:
        BFS_planned_path = queue.pop(0) 
        node = BFS_planned_path[-1]
        if node == end_node:
            return BFS_planned_path
        for i in graph.get(node, []):
            new_BFS_planned_path = list(BFS_planned_path)
            new_BFS_planned_path.append(i)
            queue.append(new_BFS_planned_path)
print("visited nodes are")
pprint(visited_nodes)
print("Genrated graph is")
pprint(generated_graph)
print("node BFS_planned_path is")
print (bfs(generated_graph, 1, global_node_count))