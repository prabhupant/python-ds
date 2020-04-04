# Notes

## Linked List

### Advantages over Array

1. Dynamic size
2. Ease of insertion/deletion

### Drawbacks

1. Random access is not allowed
2. Extra memory is required with each pointer
3. Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.

### Applications

1. Implementation of stack and queue and adjacency list representation of graphs
2. Dynamic memory allocation [Why?](https://www.slideshare.net/profansari/linked-list-static-and-dynamic-memory-allocation)
3. Maintaining directory of names
4. Image viewer, where images are linked in slideshows
5. Previous and next page in web browsers
6. Playlist in music players

---

## Circular Linked List

### Advantages

1. Any node can be a starting point
2. Easy to go from the last node to the first node

### Disadvantages

1. More memory
2. Not easy to reverse the list

### Applications

1. Computers use Circular Linked List to cycle through active applications. Basically Round Robin Scheduling algorithm
2. Task queues
3. Snake game on Nokia phones
4. Never ending playlist

---

## Doubly Linked List

### Advantages

1. Can be traversed in both directions
2. Deletion is more efficient as we can easily fetch the previous node

### Disadvantages

1. Consumes more space because of extra pointer

[See XOR Linked List](https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/)

### Applications

1. Schedulers in operating systems
2. Undo-Redo functionality
3. MRU and LRU in operating systems

---

## Tree

### Applications

1. Store hierarchial data
2. Trie are used in autocompletion and suggestion of words
3. BST can be used in searching
4. B-Tree and B+ Trees are used in database indexing

### Misc

1. [Advantages of BST over Hash Table](https://www.geeksforgeeks.org/advantages-of-bst-over-hash-table/)
2. [Ternary Search Tree - space efficient Trie](https://www.geeksforgeeks.org/ternary-search-tree/)
3. Heaps are better at finding Min/Max whereas BSTs are finding specific values
4. Insertion in heaps is O(1) whereas it is O(log(n)) for BST. This is the killer feature of heaps
5. Binary heap creation is O(n) whereas it is O(n log(n)) for BST.

### Advantages of BST over heap

1. Search for arbitrary element is O(log(n)) in BST whereas it is O(n) for heap. [Reference](https://stackoverflow.com/questions/6147242/heap-vs-binary-search-tree-bst)

---

## Heap

### Applications

1. Graph algorithms like Djikstra
2. Priority queues

### Misc

For differences between Heap and BST - [Reference](https://stackoverflow.com/questions/6147242/heap-vs-binary-search-tree-bst)

[Why is binary heap preferred over BST for priority queue](https://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/)

---

## Graph


### Difference between Graph and Tree

|   Graphs   |   Trees  |
| --- | --- | --- |
| No unique node called root    |   Has a unique root node  |
| There can be a cycle  |   No cycle    |
| Network model | Hierarchial model |

### Applications

1. Networking
2. Social networks to find friends
3. Maps
4. Finding dependencies (Topological Sort)
5. Topological sort -
    1. Finding dependencies
    2. Job scheduling among dependent jobs
6. Kosaraju's algorithm -
    1. To find strongly connected components (which are used in social networks)
7. Bipartite Graph - 
    1. Student and class scheduling
    2. Stable marriage
    3. Text analyzer to cluster documents
    4. Netflix movie preference algorithm
8. Depth First Search - 
    1. For a **weighted** graph, DFS produces Minimum Spanning Tree
    2. Cycle check
    3. Path finding
    4. Topological Sorting
    5. Finding strongly connected components
9. Breadth First Search - 
    1. For a **unweighted** graph, BFS produces Minimum Spanning Tree
    2. Used in BitTorrent to find all neighbour nodes
    3. Crawlers in search engine [Why BFS not DFS is used in web crawlers](https://stackoverflow.com/a/20580936/12360506)
    4. Broadcasting in networking
    5. Garbage collection. Breadth First Search is preferred over Depth First Search because of better locality of reference.
    6. Ford-Fulkerson algorithm
10. Minimum Spanning Tree -
    1. Network design (like connecting all offices in a city with the lowest cost of cables)
11. Articulation Point - 
    1. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more disconnected components. They are useful for designing reliable networks.

---

## Stack

### Application

1. Expression handling, infix to postfix etc
2. Function calls
3. Parenthesis checking
4. Backtracking

---

## Queue

### Application

1. BFS traversal
2. Handling interrupts in operating system
3. IO Buffers, pipes

---

## Priority Queue

### Application

1. Prim's algorithm
2. Data compression. Used in Huffman coding
