graph = {
  'A' : ['B','C','D'],
  'B' : ['E'],
  'C' : ['D','F'],
  'D' : [],
  'E' : [],
  'F' : []
}
visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  while queue:
    s = queue.pop(0)
    print (s, end = " ")

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Path using Breadth-First Search")
bfs(visited, graph, 'A')
