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


### Eularian Path (read like oilerian)
* Type of path
* Path a specific route in traversal or search.
* Eularian path - path that traverse through every edge in graph at least once
* Basic Eularian path - start at one node, traverse all edges and might end up at at different node (without travelling over edge twicely)
* Eulerian cycle - traverse every edge only once and end up at the same node that you started with 
* Not every graph is capable having an eularian path
* Graphs can only have Eulerian cycles if vertices have an even number of edges(degree) connected to them.
* For Eulerian path, its ok for graph to have two nodes with an odd degree, if they start and end of path
* Quick algorithm for finding Eulerian cycles: start at one vertex follow edges until you return back to that vertex. If you didn't encounter every edge, you can start from an unseen edge connected to a node _you've already visited_. Continue this process until you've seen every edge in the graph once . Then you can simply add the paths together, combining them at the nodes they have in common.
* Efficiency - O(E)
* **Hamiltonian Paths**
* Path that must go through every vertex once.
* Hamiltonian cycle will start and end with the same vertex.
* Trying to decide whether a graph has a Hamiltonian path,is a famous issue in computer science called the Hamiltonian path problems.


# Lesson 7
## Case Studies in Algorithms 
### Shortest Path Problem 
  * About finding the shortest path in graph
  *  When edges stores data (number) (weighted edges), The shortest path is the one where the sum of the edges is as small as possible.
  *  If graph edges unweighted, the shortest path would just be the one with the fewest number of edges.
  *  Solution depends on nature of graph 
  *  For unweighted graph, its BFS, you start at one node and visit the closest nodes first, slowly moving out to more distant nodes until you find the one that you were looking for.
  #### Dijkstra's AlgorithmS
  * Solution to the shortest path problem for weighted undirected graphs is called Dijkstra's Algorithm
  * We begin by giving all vertices a distance value.A distance is the sum of edge weights on a path between our starting point and whatever vertex we're on.At the end of the algorithm, this distance will be the distance of the shortest path. The distance value we start with is infinity. This is a placeholder value that will update whenever we discover a node and have an actual distance to store.The node we're starting with will have a distance of zero.
  * A common implementation of Dijkstra's uses a min priority queue, where the element with minimum distance (priority) in our case, can be removed efficiently
  * We store all of our nodes in the priority queue and use extract min to take out the minimum element, the only one with a distance of zero. We will follow each edge and update the node on the other side with a distance value, which is just the weight of the edge.
  * We'll always pick the node with the smallest distance value, Because we always pick the node with the lowest distance, Dijkstra's is often called a greedy algorithm. The philosophy for this class of algorithms is pick whatever option looks best at the moment.
  * We keep going, extracting the minimum from our queue and exploring adjacent elements, until the node we're looking for has been extracted from the queue or everything else has a distance of infinity. Which means the path we're looking for doesn't exist.
  * Runtime  O(v^2)
  * Dijkstra's Algorithm works only with DAGs - Directed acyclic graphs
  
  ### Knapsack Problem (Backpack)
  * Theoretical knapsack with a limited weight capacity, and more items that can possibly fit in it.
  * Each item has a weight and a value.
  * The question here is, how can I optimize the total value of items in my knapsack, given the weight constraint?
  * First thought: just put the objects with the highest values in first.
  * But what if putting the two elements with the highest values hit the weight limit, but putting all the other elements in together would actually fit and have a higher value?
  * This problem describes an optimization issue that crops up often.
  * we could try every combination of objects and just pick the one that's best, also called the **brute force solution**
  * The runtime O(2^n) where n is the number of objects.
  #### Faster Algorithm 
  * Lets try to maximize value for smallest possible weight, then kept adding them together until we had our maximum weight.
  * We start by creating an array, which we'll use to store the maximum possible value for every weight up into our weight limit, the indices in the array represent those weights.
  * Initially value for every index(weight) is 0
  * Ex/ Take the object with weight 2. We can update the value at index two to the value of the object,then we'll update everything after it as well with the same value. Even if our knapsack can hold six, we've only seen one object so far, so we need to base that best value off one object. We look at the next object (weight 5) Again we can't change anything until index five. The value of this object is bigger than the max and it takes up the whole weight. so compare each object with value at it's index in array. Also check values of addends of particular index, and choose biggest value
  * We go through every object and check if it can increase the maximum value of every possible weight up to our maximum weight. Thus, the runtime O(nW), where W is the weight limit of our knapsack and n is the number of elements.
  * This is a pseudo polynomial time solution. A true polynomial runtime wouldn't have a variable besides n. I reiterate, polynomial time algorithms are much faster than exponential time algorithms for big numbers. So the solution here is generally faster.
 
### Dynamic Programming
* If complicated problem that seems to require trying every combination to find the solution, you need to ask yourself, **can I break this problem into subproblems**? If the answer is yes, then you've got a problem with a **dynamic programming** solution.
* Ploblems like knapsack problem run much faster by breaking it into subproblem 
* Ex/ In the Knapsack the subproblem was finding the answer for a smaller weight. You begin by solving for something like a base case, a subproblem somsmall that the answer is very simple or trivial to compute. We started with one object. With only one thing to consider, finding the maximum possible value for any weight was simple.
* Another common feature of a dynamic programming solution is a **lookup table** that stores solutions to subproblems. We stored the maximum values for different weight limits in our lookup table.
* Dynamic programming solutions take advantage of these **2** things:
    i. solving the problem for a trivial case 
    ii. storing the solution in a lookup table
    by using them to slowly add complexity to a problem.
* Another feature of a dynamic programming solution is an equation used at each step as you add complexity.
* The equation often combines some values previously computed in the lookup table, sometimes with each other and sometimes with a new value you introduce like the value of whatever object you're looking at.
* **Memoization** - using the values already stored in the table, as new objects added. No need to compute every time
* Memoization is hidden power of dynamic programming. You compute and save solutions to smaller problems. Then you don't need to calculate them again for more complex problems.
* 
### Travelling Salesman Problem - Задача о коммивояжере
* What's the fastest way for our salesman to travel between every city and return home?
* It's an Optimization Problem 
* We have a complicated graph and we're looking for the optimal route. TSP is used in everything from microchip design to DNA sequencing.
* TSP is falls into special class of problems called **NP-Hard**
* NP-Hard problems don't have a known algorithm that can solve them in polynomial time.
* Polynimial time - ex/ O(n^2), O(n), O(2)
* The Knapsack problem is actually also an NP-Hard problem. The solution we looked at was in Pseudo-Polynomial time and no true polynomial time solution is known yet.
* Since the problem is so difficult, there are two classes of algorithms considered solutions:
    1. **Exact Algorithms** - which don't happen in polynomial time but will get us the correct answer.
    2. **Approximation Algorithms** -  which don't always find the exact optimal solution but generally find a near optimal solution. They tend to run in a more reasonable amount of time, and several are even polynomial time.
           * One of the most famous, called Christofides algorithm, works by turning a graph into a tree, where the starting note is the root creating and traversing through it in a particularly intelligent way. The algorithm guarantees that the path it produces will be at most 50% longer than the shortest route.
           
* **The Brute Force** solution to TSP has the same philosophy as the one for Knapsack. Find every possible combination and pick the best one, but it takes significantly longer. **O(n!)**
* Dynamic programming solutions for TSP.The most famous one is the **Held-Karp Algorithm.** However, even the dynamic programming solutions are slow. O((n^2)(2^n))
    

