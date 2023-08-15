class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
    
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    
    def getVertices(self):
        return list(self.gdict.keys())
    
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def getNeighbors(self, node):
        if node in self.gdict:
            return self.gdict[node]
        return []

    """
    DFS: visit a node A and iterate through each of A's neighbors.
    When visiting a node B that is a neighbor of A, we visit all of
    B's neighbors before visiting the rest of A's neighbors.

    Note: preorder etc tree traversals are DFS.
    """
    def dfs(self, node, visited):
        if not node:
            return
        visited.add(node)
        print(node)
        neighbors = self.getNeighbors(node)
        for n in neighbors:
            if n not in visited:
                self.dfs(n, visited)
  
    """
    BFS is not recursive, it uses a queue iteratively.
    Visits each of A's neighbors before visiting any of their neighbors.
    """
    def bfs(self, node):
        queue = []
        visited = set()
        visited.add(node)
        queue.append(node)

        while queue:
            cur = queue.pop(0)
            print(cur)
            neighbors = self.getNeighbors(cur)
            for n in neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)

    """4.1 Route Between Nodes"""
    def routeBetweenNodes(self, node1, node2):
        queue = []
        visited = set()
        visited.add(node1)
        queue.append(node1)

        while queue:
            curr = queue.pop(0)
            print(curr)
            if curr == node2:
                print('there is a route.')
                break
            neighbors = self.getNeighbors(curr)
            for n in neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)

    """4.7 Build Order"""
    def connectedNodes(self, elements):
        nodes = set()
        for node in elements.keys():
            nodes.add(node)
        for nodeList in elements.values():
            for node in nodeList:
                nodes.add(node)
        
        return nodes
    
    def buildorder(self, connected_nodes):
        for node in connected_nodes:
            queue = []
            visited = set()
            order = []
            visited.add(node)
            queue.append(node)

            while queue:
                cur = queue.pop(0)
                order.append(cur)
                neighbors = self.getNeighbors(cur)
                for n in neighbors:
                    if n not in visited:
                        queue.append(n)
                        visited.add(n)

            if len(order) == len(connected_nodes):
                return order
            
        return None

    
        
# Create the dictionary with graph elements
graph_elements = { 
    "a" : ["b","c"],
    "b" : ["a", "d"],
    "c" : ["a", "d"],
    "d" : ["e"],
    "e" : ["d"]
}
g = graph(graph_elements)
print(g.edges())
g.addVertex("f")
print(g.getVertices())
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
g.AddEdge({'a','f'})
print(g.edges())
print(g.getNeighbors('a'))
print('\n')

"""DFS"""
print('dfs:')
g.dfs('a', set())
print('\n')

"""BFS"""
print('bfs:')
g.bfs('a')
print('\n')

"""4.1 Route Between Nodes"""
print('route between nodes:')
g.routeBetweenNodes('a', 'e')
print('\n')

"""4.7 Build Order"""
print('build order:')
graph_elements = { 
    "a" : ["d"],
    "b" : ["d"],
    "d" : ["c"],
    "f" : ["a", "b"]

}
g = graph(graph_elements)

connected_nodes = g.connectedNodes(graph_elements)
res = g.buildorder(connected_nodes)
print(res)
print('\n')