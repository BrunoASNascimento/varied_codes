import sys
# sys.setrecursionlimit(000000000)


# Opening file
file = open('data/testee.dat', "r").read()

# Separating # of nodes, ids of nodes, # of edges and edges

# Split lines
file = file.split("\n")
# First row is the number of nodes
num_nodes = int(file[0])
node_list = file[1:num_nodes+1]
# First row after the nodes is the number of edges
num_edges = int(file[num_nodes+1])
edges_list = file[num_nodes+2:num_nodes+2+num_edges]
# Separate edges_list elements
edges_list = [i.split(" ") for i in edges_list]


# # ##########
path_dict = {}
for no in node_list:
    indxs = [i for i, x in enumerate(edges_list) if x[0] == no]
    for idx in indxs:
        path_dict.setdefault(
            no, {})[edges_list[int(idx)][1]] = edges_list[int(idx)][2]
    indxs = [i for i, x in enumerate(edges_list) if x[1] == no]
    for idx in indxs:
        path_dict.setdefault(
            no, {})[edges_list[int(idx)][0]] = edges_list[int(idx)][2]
print(path_dict)


point = ['1', '11']
control = point
data = {}

for key in control:
    for value_key in control:
        data.update({value_key: path_dict.get(value_key)})
    control += (list(path_dict.get(key).keys()))
    contains_duplicates = len(control) != len(set(control))
    print(contains_duplicates)
    if contains_duplicates == True:
        control = list(dict.fromkeys(control))
        print(control)
        break

print('OK')
print(data)
path_dict = data

# print(len(node_list)**len(edges_list))
# #TODO add a point not found
# #TODO setar dinamicamente o recursion limit? olhando o dict que sair
# #TODO adicionar nos passos o ponto que começa
passed_points = ['1']
shortest_distance = float("inf")


def travel(current_point, ending_point, distance_so_far=0):
    global passed_points
    global shortest_distance
    if distance_so_far < shortest_distance:
        if path_dict.get(str(current_point)) != None:
            for i in path_dict[str(current_point)]:
                if i not in passed_points:
                    passed_points.append(i)
                    if check_if_destination(i, ending_point):
                        print(passed_points)
                        print(f'traveling from {current_point} to {i}')
                        traveled = distance_so_far + \
                            float(path_dict[str(current_point)][i])
                        print(
                            f'##### CHEGOU! EM {traveled} METROS. O caminho foi: {passed_points} #####')
                        if traveled < shortest_distance:
                            shortest_distance = distance_so_far + \
                                float(path_dict[str(current_point)][i])

                    else:
                        # pass
                        # print(f"not there yet. traveled {distance_so_far} meters")
                        # print(f'traveling from {current_point} to {i}')
                        distance_traveled = distance_so_far + \
                            float(path_dict[str(current_point)][i])
                        travel(i, ending_point, distance_traveled)
                    passed_points = passed_points[:-1]


def check_if_destination(current_point, ending_point):
    if int(current_point) == int(ending_point):
        return True
    else:
        return False


print('start travel')
print(travel(1, 11))
print(shortest_distance)
