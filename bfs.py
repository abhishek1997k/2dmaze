import pygame
green=(0,255,0)
black=(0,0,0)
clock=pygame.time.Clock()
def bfss(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited
    
    
    
def bfs_paths(graph, start, goal,bl,gameDisplay):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))
                w=bl[vertex]
                v=bl[next]
                pygame.draw.line(gameDisplay,green,(w.x,w.y),(v.x,v.y),3)
                clock.tick(10)
                #pygame.draw.line(gameDisplay,black,(v.x,v.y),(w.x,w.y),3)
                #clock.tick(10)
                pygame.display.update()
                
                
                
                
def shortest_path(graph, start, goal,bl,gameDisplay):
    try:
        return next(bfs_paths(graph, start, goal,bl,gameDisplay))
    except StopIteration:
        return None
