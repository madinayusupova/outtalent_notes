# Lesson2 
## List vs Arrays
* Python list is built as an array
* Phyton list/Array Reading O(1), inserting O(n)  since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space
* Python is a "higher level" programming language, so you can accomplish a task with little code
* Run time of len() - O(1)

## Linked List
* Each element in array stores value and index, while in linked list each element stores value and reference to the next element
* When you insert new element into linked list, firstly add link from new element to next one, before link from previous to new. so you don't lose a reference
* Insertion, deletion - O(1)
* Doubly linked list - where you have pointers to the next element and the previuos element

## Stacks
*  You put elements on top and remove or look at the top element
*  Useful when you care about only recent elements or the order in which you see and save elements matters
*  Add element = push, Remove = pop
*  In python we can use linked list to implement stack 
*  L.I.F.O. = Last In, First Out

## Queues
* First in, First out structure, oldest element comes out first
* Oldest element = head, newest = tail
* Adding element called = enqueue
* Removing element = dequeue
* Peek = when you look at head element, but you don't remove it
* We use linked list to implement queue
* Also save reference to the tail, so we can acces them in constant time
    ### Dequeue
    * Double ended queue - queue that goes both ways
    * You enqueue and dequeue from both ends
    
    ### Priority Queue
    * When you add element you assign priority
    * So, when you dequeue, you remove element with highest priority
    * If elements have the same priority, the oldest one is dequeued first
    

# Lesson 3
## Binary Search
* Efficiancy O(log n)
* Only for ordered list 

## Recursion
* Function that call itself at some point, and have a base case.
* At some moment it should alter input parameter

## Sorting
* Recursive functions
   ### Bubble Sort
    * Sinking Sort or Naive Approach
    * O(n^2) efficiency
    * Great example of in-place data sorting algorithm
    * Space complexity = O(1)
    
   ### Merge Sort
   * Break up array and sort all the parts and build it back
   * **Divide and Conquer**
   * Efficiency O(nlogn)
   * Auxillary Space = O(n) (extra space memory)
   
   ### Quick Sort
   * One of the most efficient sorting algorithms 
   * Worst case - O(n^2), Average - O(nlogn)
   * In-place
  
  
# Lesson 4
## Maps
* Key - value relation (ex/ dictionary)
* Set - unordered list with unique elements
* Map is a set-based data structure 
* A group of keys is a set- keys are unique

## Hash Function
* Hash function allows you to do look-ups in constant time 
* The purpose of HF is to transform value into one (index of a array) that can be stored and retrieved easily.
*  Ex/ Storing a ticket in array with index(reminder of last 2 digits/10)
*  **Collisions** - same hash value for 2 different inputs :(
    * 2 ways to solve this: Change the /# in hash function 
    * Or change hash function completely
    * Ex/ Change the structure of array. Save a list of values in slot, not 1 element only 
    * *Bucket* - a slot where you store a **Collcetion** of values
    * In Bucket system, look up time in worst case turns into O(m) - m is length of bucket array
    * There is NO one perfect way to desighn a hash function
    * Ideally - 1-3 element in each bucket
    * Creative - using 2nd hash function inside of a large bucket - works well if you know you're going to have a well spread out data
   
## Hash Maps
* Maps have keys and values, Key is an input to hash function to store <k,v> pair
* Keys are unique, use them to arrange unique bucket
* A Python dictionary is a map!
    ### String Keys
    * ASCII -> letters converted to numbers
    * For <30 words you can use ascii of first letter of the word

# Lesson 5
## Trees
* Extension of Linked List
* First element - root
* Has a few next elements
* Each element in a tree that contain values are called **nodes**
* Constrain#1: A tree must be completely connected
* Cons#2: No any cycles, Cycle - way to came to the same node twice
    #### Tree terms:
    * Root - **Level 1** *Parent*, Directly connected nodes - level 2 *Child*
    * Root - Ancestor, level 3 - Descendant (потомок)
    * Nodes with no children called - **Leaves** or external nodes
    * Parent - internal node
    * Connection - edge
    * Group of connections - path
    * **Height** of the node - number of edges between it and the furthest leaf on the tree
    * Leaves' height is 0, his parent = 1
    * **Depth** of a node - number of edges to the root
    * Height and Depth should move inversely
    * Height of the tree = height of the root
    
* Tree Traversal (обход) (look at every element)   
* 1. _DFS - Depth-First Search_ - if there are children nodes to explore, exploring them is priority 
        * _Pre-Order Traversal_ - check off a node as you see it before you traverse a tree. Root -> LeftChild -> LeftChild (leaf)-> Right Child 
        * _In-Order Traversal_ - from the left most to right, from left leaf toward root etc. from root you find left most, and start there, finish one left parent with all children, after that move to the root and right child
        * _Post-Order Traversal_ - From root you find left most, and start there, check left one, move from parent to right one. when all descendants done, check parent. So last element in this way is the Root 
 * 2. BFS - Breadth-First Dearch - priority is visiting every node on the same level, before visiting child nodes- Level order, from left to right

    ### Binary trees
    * Trees with at most 2 children 
    *  Children can be null
    *  Search O(n)
    *  Delete O(n) - since you are searching the way to shift children
    *  Insert
    *  Number of nodes on each level equivalent to a power of 2

    ### Binary Search Tree
    * Binary tree with rule, that element on left of node is smaller than it, and on right is bigger than it.
    * Average search = O(logn)
    *  BSTcan be unbalanced (ex/ all elements on right side 5>8>23>56)
    *  Unbalanced BST - worst case scenario O(n)
    
    
    ### Heaps
    * Elements are arranged in decreasing or increasing order, so that root is either maximum (*Max Heaps*) or minimum number (*Min Heaps*) in the tree
    * In a Max Heap, a parent must always be greater than its child
    * Opposite in min heap
    * Heaps may not be binary, can have more than 2 children
    * Max Binary Heap (MBH):
    * Binary heap must be "COMPLETE" - all levels except last one should be full
    * If last level isn't totally full, values are added from left to right 
    *  The right most leaf will be empty until the whole row has been filled
    *  Max value function called PEEK - O(1)
    
    *  Search - O(n)
    *  Insert - insert in available place in the tree and **Heapify**
    *  Heapify - heap property - in MBH parent should be bigger than it's child, so keep compairing new element with parent and  swap them when child is bigger
    *  Extract - similar approach,  if root is removed, we put there rightmost leaf, compare to the children and swap where necessary 
    *  Insert, Delete- average O(logn), worst O (height of tree)
    * **Heap Implementation** - often stored in array (Binary heaps)
    *  _Sorted_ array can be a heap. Each level on the tree is twice as big as the one before it.
    *  Saving data in array store memory, no need to save pointers


    ### Red - Black Trees
    * Balanced tree has a few levels, while unbalanced spread to many levels
    * Extreme unbalanced tree - Linked List
    * *Self-Balancing tree* is one that tries to minimize the number of levels that it uses
    * It does some algorithm during insertion and deletion to keep itself balanced 
    * **Red-Black Tree** - BST
    * 1. Each node either black or red
    * 2. Every node in tree that doesn't have two leaves MUST have null children
    * Null leaves are colored black 
    * 3. Red node should have BOTH children null leaves
    * 4. Root should be black 
    * 5. Every path from a node to its descendant null nodes must contain the same number of black nodes
    * Red-Black Trees also should follow the rules of Binary Search Trees
    * Case1. When you insert first element to the tree - root, you can color it black according to the rule 4., all other insertions are red
    * Case2.If you add the node, and the parent is black, everything is ok
    * Case3. If you add a new node and the parent is red: if parent and its sibling are both red, then they should be changed to black, and Grandparent become RED (unless its not a root).
    * Case4. Elif, parent is red, but its subling is black. You need to perform a **Rotation**. if Child and Parent are not on the same side if their parents, you rotate them so both left (or right?). that is case5.
    * Case5. Red Node and its Red parent are on the same side of their parents. Rotate Grand Parent > Parent >Child to the form Child < Parent > Grand Parent. Also swap colors. 
    * ^ The nodes are rearranged without changing the number of black nodes in any path
    * Those are all 5 cases that could arise in insertion
    *   Search and Delete - in average O(logn) and worst cases also!
 
 

# Lesson 6
## Graphs (Network)
* Similar to tress, (Nodes, Edges)
* Tree is a specific type of graph 
* Graph - you can start anywhere and you can follow some path back to the start
* Edges can store data too!!!
* Edges can have Direction
* *Directed Graph* - graph where edges have a sense of direction
* In Directed graphs you can have two edges between the same two node
* Cycles might leed to infinite loops, so when you take a graph as an input, be sure that its acyclic- has no cycles
* **DAG** - Directed Acyclic graph 
* **Connectivity**
    * **Disconnected graph** - has some vertex, that can't be reached by others vertices, one vertex off with no edges
    * Disconnected graphs are very similar whether the graph's directed or undirected—there is some vertex or group of vertices that have no connection with the rest of the graph
    * In graphs some nodes may not be connected at all or connected components (2 mini graphs with no connection between each other)
    * **Connected** graph has no disconnected vertices 
    *  Connectivity Principle - minimum number of elements that need to be removed to make a graph disconnceted 
    *  Use connectivy to answer the questions which graph is stronger
    *  **Weakly Connected** - A directed graph is weakly connected when only replacing all of the directed edges with undirected edges can cause it to be connected. Imagine that your graph has several vertices with one outbound edge, meaning an edge that points from it to some other vertex in the graph. There's no way to reach all of those vertices from any other vertex in the graph, but if those edges were changed to be undirected all vertices would be easily accessible.
    * **Strongly Connected** Strongly connected directed graphs must have a path from every node and every other node. So, there must be a path from A to B AND B to A.
* **Graph Representation**
* We can use OOP's, Classes, and create Vertex and Edge objects
* There are several ways to represent connections on simple graphs using lists
*  Ex/ Edge list, [[0, 1], [1, 2] ...] 2 elements - 1 edge
*  Edge list - list of other lists - **2D** list 
*  Ex/ Adjacency List - in AL, your vertices normally have an ID number that corresponds to the index in an array. Each space in array is used to store a list of nodes that the node with this id is adjacent to. на индексе 1 - сохраняется список nodes которые связанны с элементом 1
*   In an adjacency list, your vertices normally have an id number that corresponds to the index in an array. Also 2D
*   **Adjacency Matrix**
*   2D array, with all lists inside of the same length. Matrix also called a rectangular array
*   Indicies of outer array represents nodes with those ids. And List inside still represents which nodes are adjacent 
*   List inside represents which nodes are adjacent. Inner list has one slot for every node in the array, if theres an adge between these two nodes a 1 goes into the array, if no edge 0
*   Place on every line where the row number equals the column number is always 0, unless there is an edge that started and ended with the same node
*   In matrix 1 edge shows up twice (2, 3)(3, 2)

### Graph Traversal 
* 2 basic methods for traversal 
* DFS - Deapth First Search - follow one path as far as it'll go
* BFS - Breadth First Search - look to all the nodes adjacent to one before moving to the next level 
*  Graph Traversal almost the same thing as Graph Search. Traversal - go through every element, Search - stop traversing when you find element you are looking for.
*  In graph no root, no obvious place to start traversing, so you begin with any nood
*  Common implementation of **DFS** - **Stack** - see 1 node, store in Stack, pick an edge, follow it, check one more node +  add it to the stack. Keep repeating. When you hit a node, that you've seen before, just go back to prev node and try another edge. If no edges left, pop the current node from stack and go back to the one before it. Continue this approach, until you've popped everything off the stack. 
* Another common implementation of **DFS** - **Recursion** no stack - Repeat the same process of picking an edge and marking a node as seen, until you run out of new nodes to explore. That becomes the base to the last level of recursion, and you move back to the last level of recursion, which is previuos node in the search.
* In this algorithm we visit every edge and every node O(|2e|+|V|) ~ O(|e|+|V|)
* **BFS** - also visiting every node and marking off every node, But we search every edge of one node, before continuing on through the graph 
* We start with first node, mark it "seen", visit adjacent node, mark it, add it to QUEUE (first in, first out) , we go back to that first node and visit everything adjacent, marking each seen and adding them to queue. When we've run out of edges we can just dequeue a node from the queue and use it as next starting place. We again look at every node adjacent to that one, add each one to the queue, until no options will left
* BFS is like creating tree from a graph, where starting node becomes a root. Adjacent nodes is the next level nodes in the tree.
* Efficiency O(|e|+|V|)
* 
* 
















