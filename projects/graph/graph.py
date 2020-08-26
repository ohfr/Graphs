"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # directed as in v1 -> v2

        # make sure they both exist
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex
        # Create an empty set to track visted vertices

        # while queue is not empty:
            # get current vertex (dequeue from queue)
            # print current vertex
            # Mark current vertex as visited
                # add current vertex to a visited_set
            # queue up all current vertex's neighbors that have NOT been seen(so we can visit the next)

        queue = Queue()

        queue.enqueue(starting_vertex)

        visited = set()

        while queue.size() > 0:
            cur = queue.dequeue()

            print(cur)

            if cur not in visited:
                visited.add(cur)

            for v in self.get_neighbors(cur):
                if v not in visited:
                    queue.enqueue(v)





    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack and add the starting vertex
        # Create an empty set to track visted vertices

        # while stack is not empty:
            # get current vertex (pop from stack)
            # print current vertex
            # Mark current vertex as visited
                # add current vertex to a visited_set
            # push all current vertex's neighbors that have NOT been seen(so we can visit the next)


        stack = Stack()

        stack.push(starting_vertex)

        visted = set()

        while stack.size() > 0:
            cur = stack.pop()

            if cur not in visted:
                print(cur)

                visted.add(cur)

            for v in self.get_neighbors(cur):
                if v not in visted:
                    stack.push(v)
                     

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """

        if self.get_neighbors(starting_vertex) == None:
            return
        else:
            if starting_vertex not in visited:
                print(starting_vertex)
                visited.add(starting_vertex)

                for v in self.get_neighbors(starting_vertex):
                    self.dft_recursive(v, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue the path to starting vertex
        # Create an empty set to track visted vertices

        # while queue is not empty:
            # get current vertex PATH (dequeue from queue)
            # set current vertex to last element of the PATH

            # Check if current vertex has not been visited:

                # Check if current vertex is destination
                    # if it is return it

                # Mark current vertex as visited
                    # add current vertex to a visited_set

                # Queue up new paths with each neighbor:
                    # take current path
                    # append neighbor to it
                    # queue up new path
        queue = Queue()

        queue.enqueue([starting_vertex])

        visited = set()

        while queue.size() > 0:
            curPath = queue.dequeue()

            cur = curPath[-1]

            if cur not in visited:

                if cur == destination_vertex:
                    return curPath
                
                visited.add(cur)

                for v in self.get_neighbors(cur):
                    if v not in visited:
                        tempPath = list.copy(curPath)
                        tempPath.append(v)
                        queue.enqueue(tempPath)

        return -1




    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()

        stack.push([starting_vertex])

        visted = set()

        while stack.size() > 0:
            curPath = stack.pop()

            cur = curPath[-1]

            if cur == destination_vertex:
                return curPath
            
            if cur not in visted:
                visted.add(cur)

            for v in self.get_neighbors(cur):
                if v not in visted:
                    tempPath = list.copy(curPath)
                    tempPath.append(v)
                    stack.push(tempPath)




    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), curPath=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if self.get_neighbors(starting_vertex) != None:
            if len(curPath) < 1:
                curPath = [starting_vertex]
            cur = curPath[-1]

            if cur not in visited:
                visited.add(cur)

                if cur == destination_vertex:
                    return curPath
                
                for v in self.get_neighbors(cur):
                    if v not in visited:
                        tempPath = list.copy(curPath)
                        tempPath.append(v)
                        vResult = self.dfs_recursive(v, destination_vertex, visited, tempPath)
                        if vResult:
                            return vResult


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
