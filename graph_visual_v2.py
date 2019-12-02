import turtle
import random
import time

class Graph:
    def __init__(self, tur, nodes, edges):
        tur.hideturtle()
        self.tur = tur
        self.nodes = nodes
        self.edges = edges
        self.node_positions = {}

    def __str__(self):
        string = 'nodes: ' +str(self.nodes)+"; edges: "+ str(self.edges)
        return string
    def set_nodes(self, positions):
        self.node_positions = positions

    def random_nodes(self):
        copy = self.nodes.copy()
        curr = copy.pop(0)

        self.node_positions = {}

        while(copy or curr!='done'):
            #x = random.randrange(-350,350)
            #y = random.randrange(-350,350)
            x = random.randrange(-350,0)
            y = random.randrange(-350,350)

            too_close = False
            for name, pos in self.node_positions.items():
                if dist((x,y),pos)<70:
                    too_close = True

            if not too_close:
                if(not copy):
                    self.node_positions.update({curr:(x,y)})
                    curr = 'done'
                else:
                    self.node_positions.update({curr:(x,y)})
                    curr = copy.pop(0)

    def offset(self,x,y):
        for i in self.node_positions:
            t = (self.node_positions[i][0] + x , self.node_positions[i][1] + y)
            self.node_positions[i] = t

    def draw_num(self, num):
        dots = [(-7,3),(0,3),(7,3),(-7,-3),(0,-3),(7,-3)]
        bit = "{0:b}".format(num).zfill(6)
        self.tur.pensize(4)
        pos = self.tur.pos()
        self.tur.up()
        idx = 0
        for i in dots:
            new_loc = (pos[0]+i[0], pos[1]+i[1])
            self.tur.goto(new_loc)
            if(bit[idx]=='1'):
                self.tur.color('black')
            else:
                self.tur.color('white')
            self.tur.down()
            self.tur.forward(1)
            self.tur.up()
            idx+=1

    def draw_nodes(self, color, show_number = False):
        self.tur.shape('circle')
        self.tur.color(color)
        self.tur.up()
        for i in self.node_positions:
            self.tur.goto(self.node_positions[i])
            self.tur.color(color)
            self.tur.stamp()
            if(type(i)==int and show_number):
                self.draw_num(i%64)

    def draw_edges(self, color):
        self.tur.shape('circle')
        self.tur.pensize(3)
        self.tur.color(color)
        self.tur.up()
        for i in self.edges:
            self.tur.goto(self.node_positions[i[0]])
            self.tur.down()
            self.tur.goto(self.node_positions[i[1]])
            self.tur.up()

    def spec_edges(self, edges, color):
        self.tur.shape('circle')
        self.tur.pensize(3)
        self.tur.color(color)
        self.tur.up()
        for i in edges:
            self.tur.goto(self.node_positions[i[0]])
            self.tur.down()
            self.tur.goto(self.node_positions[i[1]])
            self.tur.up()

    def random_graph(self, num_nodes, num_edges, connected = True):
        v = [i for i in range(num_nodes)]
        e_check = []
        e = []

        e_num = 0
        while (e_num < num_edges):
            v1 = random.randrange(0,num_nodes)
            v2 = random.randrange(0,num_nodes)
            w = dist(self.node_positions[v1],self.node_positions[v2])

            if((v1,v2) in e_check or (v2,v1) in e_check or v1==v2):
                pass
            else:
                e_check.append((v1,v2))
                e.append((v1,v2,w))
                e_num +=1

        return v, e

    def linear_graph(self, num_nodes, num_edges):
        v = [i for i in range(num_nodes)]
        e = []
        e_check = []
        if num_edges<num_nodes-1:
            num_edges = 0
        else:
            num_edges = num_edges - num_nodes + 1
        for i in range(num_nodes-1):
            w = dist(self.node_positions[i],self.node_positions[i+1])
            e.append((i,i+1,w))
            e_check.append((i,i+1))
        while num_edges!=0:
            v1 = random.randrange(0,num_nodes)
            v2 = random.randrange(0,num_nodes)
            w = dist(self.node_positions[v1],self.node_positions[v2])
            if((v1,v2) in e_check or (v2,v1) in e_check or v1==v2):
                pass
            else:
                e_check.append((v1,v2))
                e.append((v1,v2,w))
                num_edges -=1
        return v, e

def dist(x,y):
    return ((x[0]-y[0])**2 + (x[1]-y[1])**2)**(.5)

def main():
    wn = turtle.Screen()
    wn.setup(width=800, height=800)
    bob = turtle.Turtle()
    bob.speed(0)

    n = 10
    v = 40
    g = Graph(bob, [i for i in range(n)], v)
    g.random_nodes()
    n,e = g.linear_graph(n,v)
    print(e)
    g.edges = e

    g.draw_edges('red')
    #g.draw_nodes('blue',True)
    g.draw_nodes('blue')

    e_prime = []

    #O(n)
    n_prime = {i:('n','n',100000) for i in n}

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
    print(n_prime)
    e_list = [n_prime[i] for i in n_prime]

    print(g.edges)
    print(e_list)

    g.offset(350,0)
    g.spec_edges(e_list,'red')
    #g.draw_nodes('blue',True)
    g.draw_nodes('blue')

    wn.exitonclick()


main()


#example
'''
wn = turtle.Screen()
wn.setup(width=800, height=800)
bob = turtle.Turtle()
bob.speed(0)

#HERE is where you can define the graph with a number of nodes n and random edges e
n,e = random_graph(10,45)
g = Graph(bob, n, e)

#n,e = linear_graph(46,45)
#g = Graph(bob, n, e)

g.random_nodes()
g.draw_edges('red')
g.draw_nodes('blue')
#g.spec_edges([(2,4)],'black')
g.draw_nodes('blue')
print(g)

g.spec_edges([(2,4)],'black')
g.draw_nodes('blue')
time.sleep(1)
g.spec_edges([(5,9)],'black')
g.draw_nodes('blue')
'''
