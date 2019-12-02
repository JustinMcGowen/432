import random
import time

def dist(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(.5)

def random_graph(num_nodes, num_edges, connected = True):
    v = [i for i in range(num_nodes)]
    e_check = []
    e = []

    e_num = 0
    while (e_num < num_edges):
        v1 = random.randrange(0,num_nodes)
        v2 = random.randrange(0,num_nodes)
        w = random.randrange(0,100)

        if((v1,v2) in e_check or (v2,v1) in e_check or v1==v2):
            pass
        else:
            e_check.append((v1,v2))
            e.append((v1,v2,w))
            e_num +=1

    return v, e

def linear_graph(num_nodes, num_edges):
    v = [i for i in range(num_nodes)]
    e = []
    e_check = []
    if num_edges<num_nodes-1:
        num_edges = 0
    else:
        num_edges = num_edges - num_nodes + 1
    for i in range(num_nodes-1):
        w = random.randrange(0,100)
        e.append((i,i+1,w))
        e_check.append((i,i+1))
    while num_edges!=0:
        if((v1,v2) in e_check or (v2,v1) in e_check or v1==v2):
            pass
        else:
            e_check.append((v1,v2))
            e.append((v1,v2,w))
            num_edges -=1
    return v, e

def main():
    #O(n) = iter through each vertex
    #O(m) = iter through each edge
    #O(n) <= O(m) for any non-trivial graph (m>n otherwise, the graph is either not connected or the graph is the mst)
    n,e = random_graph(10,45)
    e_prime = []

    #O(n)
    n_prime = {i:('n','n',101) for i in n}

    print(n_prime)
    #O(m)
    for i in e:
        v1 = i[0]
        v2 = i[1]
        w = i[2]
        if n_prime[v1][2] > w:
            n_prime[v1] = i
        if n_prime[v2][2] > w:
            n_prime[v2] = i



main()
