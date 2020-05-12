from graph import Graph
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

# def earliest_ancestor(ancestors, starting_node):
    
#     # use BFS to search for the oldest
#     # EdGE case: if no relevant parent node return -1 
#     valid = False
#     # loop all ancestors and check to see if no parent node exists then return -1
#     for parent in ancestors:
#         if parent[1] == starting_node:
#             valid = True
#             break

#     if valid == False:
#         return -1

#     # create an empty queue to store visited ancestors
#     q = []
#     q.append([starting_node])

#     visited = set()

#     # search the queue until it is empty
#     while len(q) > 0:
#         # dequeue the first one 
#         path = q.pop(0)
#         #print('path', path)
#         # current vert is not the end of the path
#         v = path[-1]
#         #print('current v:', v)
        
#         # if the vert is not in visited add it 
#         if v not in visited:
#             visited.add(v)
#             print('visited', visited)

#         valid = False

#         # seach for the oldest
#         for parent in ancestors:
#             #print(parent[0])
#             if parent[1] == v:
#                 new_path = list(path)
#                 new_path.append(parent[0])
#                 q.append(new_path)
#                 valid = True

#         # if v has no ancestors, break the loop
#         if valid == False:
#             print('no more', v)
#             q.append(list(path))
#             break


#         # now find the earliest 
#     earliest = []
#     # loop the q
#     for path in q:
#         print(path, earliest)
#         # as long as the path is larger than earliest add that path to the earliest
#         if len(path) > len(earliest):
#             earliest = list(path)
#         # if they are the same length compare the last elements in the list
#         elif len(path) == len(earliest):
#             print('in here', path[-1], earliest[-1])
#             #if the earliest is larger add the path to the list
#             if path[-1] < earliest[-1]:
#                 earliest = list(path)

#     return earliest[-1]
            

"""short hand"""

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    # PSUEDOCODE:
    # import Graph
    # iterate through the array or ancestors
    for tuple_ in ancestors:
        # make a dictionary/ or some how find a way to add connected vertex
        # how do i creat each vertex?
        # if the tuple_ is not already in the vertices
        if tuple_[0] not in g.vertices:
            # add each tyuple_[0] to graph vertex
            g.add_vertex(tuple_[0])
        if tuple_[1] not in g.vertices:
            g.add_vertex(tuple_[1])
    #print(g.vertices, "================")
    for linked_pair in ancestors:
        # index of 0 in each tuple would be the v1 in add_edge
        # index of 1 in same tuple would be the v2 in add egde
        # make sure all edges are added
        g.add_edge(linked_pair[0], linked_pair[1])
    #print(g.vertices, "********************")
    all_paths = []
    # implement the vertex
    for vertex in g.vertices:
        dfs_call = g.dfs(vertex, starting_node)
        print(dfs_call)
        if dfs_call is not None:
            if len(dfs_call) > len(all_paths):
                all_paths = dfs_call
            elif len(dfs_call) == len(all_paths):
                if dfs_call[0] < all_paths[0]:
                    all_paths = dfs_call
    # needs to return in order to
    if len(all_paths) == 1:
        return -1
    return all_paths[0]
    # CONDITIONALS
    # if there is more than one earliest ancestor
    #   # return the min value of the nodes in question
    # if input aka start_node has no parents:
    #   # return the value of -1



print('1:', earliest_ancestor(test_ancestors, 1))
print('2:', earliest_ancestor(test_ancestors, 2))
print('3:', earliest_ancestor(test_ancestors, 3))