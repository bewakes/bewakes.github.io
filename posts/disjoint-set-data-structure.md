---
title: Disjoint Set Data Structure
tags:
    - computer-science
date: May 5, 2017
---

As the name suggests, it is a data structure to keep track of the disjoint partitions formed in a set. In case the data structure sounds like 'WAT??' or 'I have not heard about it. Is it useful?', rest assured, we'll be seeing the practical application of disjoint set in the next post: [finding a Minimal Spanning Tree for an undirected graph](/posts/minimum-spanning-tree-kruskal.html).

Here, we will be seeing its implementation in Python which is my favourite language(I kind of had love at first sight with python :D ). It is assumed that the reader knows basics of python, and what set, partition, tree, array and list mean.

Okay, now into the technicality of the data structure. It basically provides the following three functions:

* `make_set(e)`: It adds a partition to the set. The partition consists of a single element e. For example, consider a set A={a,b,c,d}
with partitions {a,b} and {c,d}. After the operation, A={a,b,c,d,e} and a new partition {e}.

* `find(e)`: It finds/returns the identification of the partition that e lies in. For example, if the set is A={a,b,c}
, and partitions are B={a} and C={b,c}
, `find(b)` will return C [We will have some very easy ways to identify a set. Don't worry about it now.]

* `union(a, b)`: And this wonderful operation will union the sets that contain elements a and b. For example, if the given set is A={a,b,c,d,e}
and the partitions are {a,b}, {c} and {d,e}, union(c, e) will result in the partitions {a,b} and {c,d,e}.

## Implementation

We will implement the data structure using tree(implemented as array, relax!! ). A tree represents a set. The root of the tree is the identification of the set. Now, two elements are in same set if they have same root element.

Let's begin with the basic list to hold the sets. We call it `parents_array` which holds the parent of an element. Let n be the total number of elements in our set.

`parents_array = [x for x in range(n)]`

For example, if `parents_array = [2 0 2 2 4]`, this means that there are 5 elements and:

    2 is parent of 0,
    0 is parent of 1,
    2 is parent of 2 and is the root,
    2 is parent of 3,
    4 is parent of 4 and is the root and the only element.

Okay, now let's implement make_set() function. Since the function is supposed to make a single set of an element, it takes a number as parameter.

```python
def make_set(i):
    parents_array[i] = i
```

That's it. What this does is, sets the parent of an element to itself, which means, that is the set consisting of only that element.

Now, `find()` function, which finds the parent of an element.

```python
def find(e):
    while parents_array[e] != e:
        e = parents_array[e]
    return e
```

Here, the tree is traversed until the root element is found (an element is root if its parent is itself).

We're almost there, only `union()` remains which unions the sets containing the
input elements. The idea is that, we find the root elements of both elements.
Union means both elements having same root. So, we make one root the parent of
other. Here's the basic implementation:

```python
def union(i, j):
    ir = find(i) # root(set id) of element i
    jr = find(j) # root(set id) of element j

    if ir == jr:
        return # same roots means they are in same set

    # set one element as parent of other
    parents_array[ir] = jr
    # or parents_array[jr] = ir, we'll talk about efficincy later
    # that's it
```

However, we would like to make our data structure and operations on it as optimal as possible, right? First thing we need to be clear is that, we want the find() operation to be as fast as possible. This is obtained when the height of tree is low i.e, reaching the root element from child requires as less steps as possible.

## Optimization

Now, imagine a situation in which we are doing union. We append one set(tree)
as the child of the other so that both have same root. Appending a shorter tree
to the longer one will result in a tree with height same as the initial height
of the longer tree. If we did otherwise, the height of the shorter tree would
be increased by 1.

So, to keep track of the heights(also called ranks) of the trees, we introduce
another array ranks_array which is initialized as:

`ranks_array = [0 for x in range(n)] # initial height is zero`

Now, `make_set()` becomes,

```python
def make_set(i):
   parents_array[i] = i
   ranks_array[i] = 0 # height of single element tree is zero, of course
```

In `union()`, we append shorter tree to the longer one and if they have same
`rank(height)` we can append in any way. But, we need to be careful to increase
the height of the parent tree by 1(You guess why). Changed implementation of
`union()` will be included in the full code below, which implements Disjoint Set
as class.

## Full code
```python
class DisjointSet:
"""
Implementation of disjoint sets
"""

    def __init__(self, n):
        """
        n is the number of elements
        """
        # create different sets where each is a unique set
        self.parents_array = [x for x in range(n)]
        self.ranks_array = [0 for x in range(n)] # initial rank is zero for all

    def find(self, p):
        """
        find the parent of the element (0 indexed)
        """
        while self.parents_array[p] != p:
            p = self.parents_array[p]
        return p

    def make_set(self, i):
        """
        assign element i to its own set
        """
        self.parents_array[i] = i
        self.ranks_array[i] = 0

    def union(self, i, j):
        """
        i and j are 0 indexed elements which are to be unioned
        """
        i_root = self.find(i)
        j_root = self.find(j)

        if i_root == j_root:
            # nothing to be done already in same set
            return

        if self.ranks_array[i_root] < self.ranks_array[j_root]:
            self.parents_array[i_root] = j_root
        else:
            self.parents_array[j_root] = i_root
            if self.ranks_array[i_root] == self.ranks_array[j_root]:
                self.ranks_array[i_root]+=1
```

I hope that was helpful. Feel free to contact me if there are any problems.
