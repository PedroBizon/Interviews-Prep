def dijkstra(graph, start, finish):
    ''' 
        Takes a graph, a start node and a finish node, and returns the cost of going from
        node start to node finish.

        This can be easily altered to be more effective in real-life scenarios. To do so,
        the function should be adapted to: 
        1. Not take finish as input, so it doesn't stop computating when there are still 
        nodes left; 
        2. Return both parents and costs, in full.  
        3. Have helper function or additional logic to easily calculate a path to any node,
        given it's provided  
        
    '''


    infinite = float("inf")
    costs = {}
    parents = {}
    processed = []

    # 1. Setting up the costs
    for i in graph.keys():
        costs[i] = infinite

        if i == start:
            costs[i] = 0
                    
    for i in graph[start].keys():
        costs[i] = graph[start][i]
        parents[i] = start

    minimum_cost = infinite
    minimum_cost_node = None

    # Find first minimum cost node
    for c in costs.keys():
            if costs[c] < minimum_cost and c not in processed:
                minimum_cost = costs[c]
                minimum_cost_node = c

    while minimum_cost_node != None:

        processed.append(minimum_cost_node)

        if minimum_cost_node == finish:
            # Finish line has already been crossed, no need for further computation 
            break

        # Put current node's neighbor costs into costs
        for node in graph[minimum_cost_node].keys():
            if node not in processed:
                
                if minimum_cost + graph[minimum_cost_node][node] < costs[node]:
                    costs[node] = minimum_cost + graph[minimum_cost_node][node]
                    parents[node] = minimum_cost_node

        # Getting a new minimum cost node
        minimum_cost = infinite
        minimum_cost_node = None
        for c in costs.keys():
            if costs[c] < minimum_cost and c not in processed:
                minimum_cost = costs[c]
                minimum_cost_node = c

    return costs[finish]
        


def tests():
    graph = {}
    graph['start'] = {}
    graph['start']['A'] = 6
    graph['start']['B'] = 2
    graph['A'] = {}
    graph['A']['finish'] = 1
    graph['B'] = {}
    graph['B']['A'] = 3
    graph['B']['finish'] = 5
    graph['finish'] = {}

    result = dijkstra(graph, 'start', 'finish')

    print(result)


tests()