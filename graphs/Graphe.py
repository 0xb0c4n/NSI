class GrapheM:
    def __init__(self, n):
        self.n = n
        self.adj = [[False] * n for _ in range(n)]

    def ajouter_arc(self, s1, s2):
        self.adj[s1][s2] = True

    def arc(self, s1, s2):
        return self.adj[s1][s2]

    def voisins(self, s):
        v = []
        for i in range(self.n):
            if self.adj[s][i]:
                v.append(i)
        return v

    def degre(self, s):
        return len(self.voisins(s))

    def nb_arcs(self):
        i = 0
        for f in self.adj:
            for b in f:
                i += 1 if b else 0
        return i

    def supprimer_arc(self, s1, s2)
        self.adj[s1][s2] = False

    
class GrapheD:
    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj:
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj)

    def voisins(self, s):
        return self.adj[s]

    def nb_sommets(self):
        return len(self.sommets())

    def degre(self, s):
        return len(self.voisins(s))

    def nb_arcs(self):
        i = 0
        for f in self.adj:
            i += len(self.adj[f])
        return i

    def supprimer_arc(self, s1, s2):
        s1_v = self.adj[s1]
        if s2 in s1_v:
            s1_v.remove(s2)
            