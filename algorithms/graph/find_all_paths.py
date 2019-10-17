'''
find all the possible paths in a directed cyclic graph from
a start point to a end point.
'''




def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path: #to prevent cyclic rotations
                newpaths = find_all_paths(graph, node, end, path)
                #print(newpaths)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


graph={1:[2,4],
       2:[3],
       4:[5],
       3:[5]
    }

for i in graph.keys():
    print(i,'to 5',find_all_paths(graph,i,5))
