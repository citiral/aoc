import sys

def count_paths(graph, path, doubled):
    connections = graph[path[-1]]

    count = 0
    
    for (connection, big) in connections:

        # dont visit small caves twice
        small_and_already_visited = not big and connection in path
        if doubled and small_and_already_visited or connection == "start":
            continue
        
        if connection == "end":
            #print(path + [connection])
            count += 1
        else:
            count += count_paths(graph, path + [connection], doubled or small_and_already_visited)
    
    return count

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        graph = {}
        input = [l.strip() for l in f.readlines()]
        for line in input:
            (inp, out) = line.split("-")
            inp_big = inp.isupper()
            out_big = out.isupper()

            if not inp in graph:
                graph[inp] = [(out, out_big)]
            else:
                graph[inp].append((out, out_big))
            if not out in graph:
                graph[out] = [(inp, inp_big)]
            else:
                graph[out].append((inp, inp_big))

        print(graph)
        print(count_paths(graph, ["start"], False))