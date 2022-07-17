class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    # Finding all the routes in the city
    def getPaths(self, start, end, path=[]):
        path = path+[start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = [] # All possible paths

        # All the key's in the dictionary
        for node in self.graph_dict[start]:
            if node not in path:
                # check if a perticular destination has visited or not
                new_path = self.getPaths(node,end,path) # Example: node:[Any city], end = [destination city]
                for p in new_path:
                    paths.append(p)
        return paths


    # Finding shortest route
    def getShostestPath(self, start, end, path=[]):
        path = path + [start]

        sp = None

        if start not in self.graph_dict:
            return []
        if start == end:
            return path
        for node in self.graph_dict[start]:
            if node not in path:
                shotest_path = self.getShostestPath(node, end, path)
                if shotest_path:
                    if sp is None or len(shotest_path)<len(sp):
                        sp = shotest_path
        return sp

if __name__ == '__main__':
    routes = [("Mumbai", "Paris"),
              ("Mumbai","Dubai"),
              ("Paris", "Dubai"),
              ("Paris", "New York"),
              ("Dubai", "New York"),
              ("New York", "Toronto")]

    route_graphs = Graph(routes)


    start = "Mumbai"
    end = "New York"
    print(f"Path Between {start} and {end}:", route_graphs.getPaths(start,end))
    print(f"Shotest Path Between {start} and {end}:", route_graphs.getShostestPath(start, end))