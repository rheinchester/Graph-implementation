# build node
# build edge
# build digraph
# build graph
# run dfs
class Node(object):
    """ creates a node with name """
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name

    def __str__(self):
        return self.name
class Edge(object):
    """ Assumes that src and dest are nodes """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return self.src.getName() +" -> "+self.dest.getName()

class Digraph(object):
    """edge is a dict mapping each node to a list of
        its children"""
    def __init__(self, edge):
        self.edge = {}

    def addNode(self, node):
        """ create a non-duplicate node key and with an empty list to contain its destination """
        if node in self.edge:
            raise ValueError('Duplicate Node')
        self.edge[node] = []
    
    def addEdge(self, edge):
        """ Add an edge with source and destination nodes """
        src = edge.getSource()# get source
        dest = edge.getDestination()  # get dest
        # else, add the node as a key in edge dict
        if not (src in self.edge and dest not in self.edge):
             # if node does not have source or destnation it is not in graph
            raise ValueError(' There is no node' )
        return self.edge[src].append(dest) #bind it to the class edge, using self
    
    # children, has node, get node
    def childrenOf(self, node):
        """ Return node's distributaries (Google distributary) """
        return self.edge[node]

    def hasNode(self, node):
        """ Check if edge has nodes """
        return node in self.edge
    
    def getNode(self, name):
        """ Get node from name passed in as parameter, else raise nameError """
       # on a good day, we are supposed to coerce this parameter to a string
        for n in self.edge:
            if name == n.getName():
                return n
        else:
            raise NameError(name)
    
    def __str__(self):
        """ Get string representation of graph """
        result = ''
        for src in self.edge:
            for dest in self.edge[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1]  # omit final newline


def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

def DFS(graph, start, end, path, shortest, toPrint=False):
    """Assumes graph is a Digraph; start and end are nodes;
          path and shortest are lists of nodes
       Returns a shortest path from start to end in graph"""
    path = path + [start] # it adds nodes to the list of travelled paths
    if toPrint:
        print('Current DFS path:', printPath(path))
    if start == end:
        # if start is equal to end, it means we are on the same node,
        #  hence no need of movement
        return path
    for node in graph.childrenOf(start):
        if node not in path:  # avoid cycles, by not entering a previously traversed  place in path
            if shortest == None or len(path) < len(shortest):#if we don't have  value for shortest, stop traversing. 
                newPath = DFS(graph, node, end, path, shortest,
                              toPrint)
                if newPath != None:
                    shortest = newPath
        elif toPrint:
            print('Already visited', node)
    return shortest
