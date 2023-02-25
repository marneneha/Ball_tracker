import numpy as np 

input_mat = np.array([])
node_list = np.array([])
match_found = False
# print("type the matrix row-wise and enter 0 in space of blank space")
# for i in range (9):
#     val = int(input())
#     input_mat = np.append(input_mat, val)
# input_mat = np.reshape(input_mat, (3,3))

input_mat = np.array([[4,5,8], [1,6,9], [0,7,2]])
node_list = [input_mat,input_mat]
print("node list is")
print(node_list)
def generate_children(node):
    global node_list, match_found, input_mat
    print("inside generate")
    print(node_list)
    index = np.argwhere(node == 0)
    index_i = index[0, 0]
    index_j = index[0, 1]
    input_node_copy = node
    print(input_node_copy)
    input_node_copy[1, [0,1]] = input_node_copy[1, [1,0]]
    # input_node_copy[0, [0,1]] = input_node_copy[0, [1,0]]
    print("input copy is ")
    print(input_node_copy)
    node_list.append(input_node_copy)
    print("node list is")
    print(node_list)
    print("first element of node list is")
    print(node_list[0])
    match_found = True


while(not match_found):
    node = input_mat
    generate_children(node)

# print(node_list)