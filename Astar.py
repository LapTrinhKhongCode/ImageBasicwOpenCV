import heapq

class Node:
    def __init__(self, label, goal_cost):
        self.label = label
        self.cost = 10000
        self.goal_cost = goal_cost
        self.save_cost = None
        self.pr = []
        self.chld = []
    
    def __repr__(self):
        return str(dict({
            "label": self.label,
            "cost": self.cost,
            "goal_cost": self.goal_cost
        }))
    
    def __eq__(self, other):
        return self.label == other.label
    
    def __lt__(self, other):
        return self.cost + self.goal_cost < other.cost + other.goal_cost
    
    def __hash__(self):
        return hash(self.label)
    
    def get_label(self):
        return self.label
    
    def neighbors(self):
        return self.chld + self.pr


class Tree:
    def __init__(self):
        self.nodes = []
        self.edges = {}
    
    def add_nodes(self, data):
        for node in data:
            self.nodes.append(node)
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def get_index(self, node):
        for i, n in enumerate(self.nodes):
            if n.get_label() == node.get_label():
                return i
        return -1
    
    def add_edge(self, tuple_edges):
        for t in tuple_edges:
            start_label = t[0]
            end_label = t[1]
            w = t[2]
            index_start_label = self.get_index(Node(start_label, None))
            index_end_label = self.get_index(Node(end_label, None))
            
            self.nodes[index_start_label].chld.append(self.nodes[index_end_label])
            self.nodes[index_end_label].pr.append(self.nodes[index_start_label])
            
            self.edges[(self.nodes[index_start_label], self.nodes[index_end_label])] = w
            self.edges[(self.nodes[index_end_label], self.nodes[index_start_label])] = w
    
    def show_nodes(self):
        return [node.get_label() for node in self.nodes]
    
    def get_edge(self, start_node, end_node):
        try:
            return self.edges[(start_node, end_node)]
        except:
            return None

def update_cost(tree, current_node, prev_node):
    edge_cost = tree.get_edge(prev_node, current_node)
    if edge_cost is not None:
        new_cost = prev_node.cost + edge_cost
        if current_node.cost > new_cost:
            current_node.cost = new_cost

def A_Star(tree, start, end):
    start.cost = 0
    frontier = [start]
    heapq.heapify(frontier)
    explored = []
    
    while len(frontier) > 0:
        state = heapq.heappop(frontier)
        explored.append(state)
        print(state)
        
        if state == end:
            return explored
        
        for child in state.neighbors():
            update_cost(tree, child, state)
            if child not in frontier and child not in explored:
                heapq.heappush(frontier, child)
            elif child in frontier:
                heapq.heapify(frontier)
    
    return False

if __name__ == "__main__":
    tree = Tree()
    nodes = [
        Node("A", 6), Node("B", 3), Node("C", 4), Node("D", 5),
        Node("E", 3), Node("F", 1), Node("G", 6), Node("H", 2),
        Node("I", 5), Node("J", 4), Node("K", 2), Node("L", 0),
        Node("M", 4), Node("N", 0), Node("O", 4)
    ]
    
    tree.add_nodes(nodes)
    
    edges = [
        ("A", "B", 2), ("A", "C", 1), ("A", "D", 3), ("A", "E", 5),
        ("B", "F", 4), ("B", "G", 6), ("C", "H", 3), ("C", "I", 2),
        ("D", "J", 4), ("D", "K", 2), ("E", "L", 1), ("F", "M", 4),
        ("H", "N", 2), ("H", "O", 4)
    ]
    tree.add_edge(edges)
    
    start_node = next(node for node in nodes if node.label == "A")
    end_node = next(node for node in nodes if node.label == "N")
    
    result = A_Star(tree, start_node, end_node)
    
    if result:
        print("explored")
        print(" -> ".join([node.label for node in result]))
    else:
        print("404 not found")