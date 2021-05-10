# Complexities

* Main rules: 
* n^C = o(e^n);
* log(n)^a = o(n^b);
* log^2(n) = o(n^(1/4))
* n* sqrt(n) = o(n^log(n)), as by taking logarithm we get 
* 3/2 * log(n) = o(log(n) * log(n))
* n^log(n) = o(2^n), as by taking logarithm we get
* log(n) * log(n) = o(n)
* n! > (n/2)^(n/2) as n! > n*(n-1)*...*(n/2) > (n/2)^(n/2)
* 2^n = o((n/2)^(n/2)) = O(n!), as by taking logarithm we get
* n = o(log(n/2) * (n/2)) 
* n! = O(n^(n - 1)) = o(n^n)


## Fixed size array
* get(i) -- O(1)
* set(i,x) -- O(1)

## Dynamic array (vector C++)
* get(i) -- O(1)
* set(i, x) -- O(1)
* pop_back() -- O(1)
* push_back(x) -- O(1) average

## Stack 
* push(x) -- O(1)
* pop() -- O(1)
* 
## Queue 
* front() -- O(1)
* back() -- O(1)
* push_back(x) -- O(1)
* pop_front() -- O(1)

## Deque
* get(i) -- O(1)
* front() -- O(1)
* back() -- O(1)
* push_back(x), pop_back() -- O(1)
* push_front(x), pop_front() -- O(1)

## Singly linked list
* front() -- O(1)
* insert_after(it, x), erase_after(it) -- O(1)
* push_front(x), pop_front() -- O(1)

## Doubly linked list
* front(), back() -- O(1)
* insert(it, x), erase(it) -- O(1)
* push_front(x), pop_front() -- O(1)
* push_back(x), pop_back() -- O(1)

## Hash table - Dict - unordered set
* insert(x), erase(x) -- O(1) average
* size() -- O(1)
* find(x), count(x) -- O(1) average
* 2 types of implementation
    * **Separate chaining**:
    * If using good hash function length of all lists are O(1).
    * Adding n same items could take O(n) for each adding.
    * Good hash function: hash(x) = x % P, P is random big prime number
    * **Open addressing**:
    * Why should we use -1 in erase() function? 
    * Example when adding to hash table takes O(n)? 
    * Adding n same items; 
    * Size of table is n + C, where n is number of added items;
    * Good hash function: hash(x) = x % P, P is random big prime number.

## Heap 
* insert(x) -- O(log n) 
* getMin() -- O(1)
* extractMin() -- O(log n)
* Indexation: Elements form binary tree with root in node 1. Node i has two children – nodes 2*i and 2*i+1. Parent of node i is node ⌊i/2⌋.
* ![heap](https://user-images.githubusercontent.com/67040252/117632408-ecc1b900-b19e-11eb-92ec-94de9cd64542.JPG)

## Binary Search Tree
* insert(), erase() -- O(log n)
* size() -- O(1)
* find(), count(), [] -- O(log n)
* begin(), end() (minimum / maximum) -- O(1)
* ![table](https://user-images.githubusercontent.com/67040252/117632675-285c8300-b19f-11eb-8679-7bc29afafbfe.JPG)
* 




