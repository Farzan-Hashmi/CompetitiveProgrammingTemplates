#path compression with union by size == O(alpha(n)) where alpha(n) is the inverse Ackermann function (< 5 for like any n). TODO: attempt to understand proof at some point
# source: i think from a codeforces blog post?

from collections import defaultdict

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n
    
    def find(self, a):
        a_copy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while a_copy != a:
            self.parent[a_copy], a_copy = a, self.parent[a_copy] # path compression
        return a
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]
    
    def get_groups(self):
        groups = defaultdict(list)
        for i in range(len(self.parent)):
            groups[self.find(i)].append(i)
        return list(groups.values())
    


    


