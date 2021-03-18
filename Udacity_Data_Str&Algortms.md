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
* 1. DFS - Depth-First Search - if there are children nodes to explore, exploring them is priority 
        * Pre-Order Traversal - check off a node as you see it before you traverse a tree. Root -> LeftChild -> LeftChild (leaf)-> Right Child 
        * In-Order Traversal - from the left most to right, from left leaf toward root etc. from root you find left most, and start there, finish one left parent with all children, after that move to the root and right child
        * Post-Order Traversal - From root you find left most, and start there, check left one, move from parent to right one. when all descendants done, check parent. So last element in this way is the Root 
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
