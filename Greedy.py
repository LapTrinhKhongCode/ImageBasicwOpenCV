import heapq

class TreeNode:
    def __init__(self, value, goal_cost):
        self.value = value
        self.goal_cost = goal_cost
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def get_children(self):
        return self.children

def update_frontier(frontier, new_node):
    for idx, n in enumerate(frontier):
        if n.value == new_node.value:
            if n.goal_cost > new_node.goal_cost:
                frontier[idx] = new_node
            return

def GBFS_search(initial_state, goalTest):
    frontier = []
    explored = []
    
    heapq.heapify(frontier)
    heapq.heappush(frontier, (initial_state.goal_cost, initial_state))
    
    while len(frontier) > 0:
        _, state = heapq.heappop(frontier)
        explored.append(state)
        
        if state == goalTest:
            return explored
        
        for neighbor in state.get_children():
            if neighbor not in frontier and neighbor not in explored:
                heapq.heappush(frontier, (neighbor.goal_cost, neighbor))
            elif any(n[1] == neighbor for n in frontier):
                update_frontier(frontier, neighbor)
    
    return False

A = TreeNode('A', 6)
B = TreeNode('B', 3)
C = TreeNode('C', 4)
D = TreeNode('D', 5)
E = TreeNode('E', 2)
F = TreeNode('F', 1)
G = TreeNode('G', 6)
H = TreeNode('H', 3)
I = TreeNode('I', 5)
J = TreeNode('J', 4)
K = TreeNode('K', 2)
L = TreeNode('L', 0)
M = TreeNode('M', 4)
N = TreeNode('N', 0)
O = TreeNode('O', 4)

A.add_child(B)
A.add_child(C)
A.add_child(D)
B.add_child(E)
B.add_child(F)
C.add_child(G)
C.add_child(H)
D.add_child(I)
D.add_child(J)
E.add_child(K)
F.add_child(L)
F.add_child(M)
H.add_child(N)
I.add_child(O)


goal_node = L  

result = GBFS_search(A, goal_node)

if result:
    print("explored:", [node.value for node in result])
else:
    print("404 not found.")
