# class Solution:
#     def dfs(graph, source):
#         print(source)
#         for neighbour in graph[source]:
#             dfs(graph, neighbour)
#
#
# graph = {
#         'a': ['b', 'c'],
#         'b': ['d'],
#         'c': ['e'],
#         'd': ['f'],
#         'e': [],
#         'f': []
#     }
#
# dfs(graph, 'a')
#
# class graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict = []
#         self.gdict = gdict
# Get the keys of the dictionary
#
#     def getVertices(self):
#         return list(self.gdict.keys())
#
# graph_elements = {
#         'a': ['b', 'c'],
#         'b': ['d'],
#         'c': ['e'],
#         'd': ['f'],
#         'e': [],
#         'f': []
#     }
#
# g = graph(graph_elements)
# print(g.getVertices())




# class graph:
#     def __init__(self,gdict=None):
#         if gdict is None:
#             gdict = {}
#         self.gdict = gdict
#
# # Get the keys of the dictionary
#     def edges(self):
#         return self.findedges()
#
#     def findedges(self):
#         edgename = []
#         for vrtx in self.gdict:
#             for nxtvrtx in self.gdict[vrtx]:
#                 if {nxtvrtx, vrtx} not in edgename:
#                     edgename.append({vrtx,nxtvrtx})
#         return edgename
#
#
# graph_elements = {
#         'a': ['b', 'c'],
#         'b': ['d'],
#         'c': ['e'],
#         'd': ['f'],
#         'e': [],
#         'f': []
#     }
#
# g = graph(graph_elements)
# print(g.edges())

class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
            self.gdict = gdict


    def edges(self):
        return self.findedges()

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edgenames
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
            return edgename

graph_elements = {
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())