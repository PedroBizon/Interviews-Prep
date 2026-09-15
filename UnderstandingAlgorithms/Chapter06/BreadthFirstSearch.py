def breath_first_seach(target, graph, start):
    ''' 
        Returns a boolean. 
        
        If it's possible to reach the target from the given start, this function returns True.
        If it's not possible to reach the target from the given start, this function returns False.
        
        Returning False DOES NOT necessarily mean the target is not on the graph. 
        It is possible that the target is unreacheable from the given start.

    '''

    # Edge Cases:
    if start == target:
        # Already found
        return True 

    if start not in graph.keys():
        # Start isn't on the graph
        return False

    searched = []
    to_search = []

    current_vertex = start

    while current_vertex != target:
        # 1. Append neighbors for future search
        for i in graph[current_vertex]:
            if i not in searched:
                to_search.append(i)

        # Moves current vertex from "to search" to "searched"
        searched.append(current_vertex)
        to_search.pop(0)

        # If to_search is empty, the search failed to find the target
        if to_search:
            current_vertex = to_search[0]
        else:
            return False

    # Target Found
    if current_vertex == target:
        return True

def tests():
    graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8],
    8: [5, 7, 9, 10],
    9: [6, 8, 10],
    10: [8, 9]
    }

    print(f"Test 1: {breath_first_seach(1, graph, 1)}")

    print(f"Test 2: {breath_first_seach(5, graph, 1)}")


    print(f"Test 3: {breath_first_seach(100, graph, 1)}")
    

    print(f"Test 4: {breath_first_seach(1, graph, 10)}")


tests()