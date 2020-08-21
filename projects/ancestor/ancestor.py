def create_mapping(ancestors):
    graph = {}
    for item in ancestors:
        if item[1] in graph:
            graph[item[1]].add(item[0])
        else:
            graph[item[1]] = set()
            graph[item[1]].add(item[0])
    return graph

def get_neighbors(node, graph):
    if node in graph:
        return graph[node]
    else:
        return -1


def earliest_ancestor(ancestors, starting_node):
    graph = create_mapping(ancestors)
    
    stack = []

    stack.append(starting_node)

    visited = set()

    cur = None

    while len(stack) > 0:
        cur = stack.pop()
        if cur not in visited:
            visited.add(cur)

        if get_neighbors(cur, graph) != -1:
            unsortedNeighbors = get_neighbors(cur, graph)
            sortedNeighbors = sorted(unsortedNeighbors)
            for v in sortedNeighbors:
                if v not in visited:
                    stack.append(v)
    if cur == starting_node:
        return -1
    else:
        return cur
