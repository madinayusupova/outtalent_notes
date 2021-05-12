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



![table](https://user-images.githubusercontent.com/67040252/117632675-285c8300-b19f-11eb-8679-7bc29afafbfe.JPG)

## Practice Notes
* Determine time complexity of such snippet of code - **n* log(n)**
      for (int a = 1; a <= n; a++) { 
        for (int b = 1; a * b <= n; b++) {
          counter++;
        }}
      n + n / 2 + n / 3 + n / 4 + … + n / n = n * (1 + ½ + ⅓ + ¼ + … + 1/n) 
      **(1 + ½ + ⅓ + ¼ + … + 1/n) = log(n)**
* What are main differences between singly linked list and doubly linked list? No reversed iteration and ability to remove specific node.
* Run time of hash map with separate chaining is O(N/M) - where N - number of buckets, M- number of input data
* FIFO Cache: удаляем элемент, попавший в кеш раньше всего, std::queue + std::unordered_set
* LIFO Cache: удаляем элемент, попавший в кеш позже всего, std::stack + std::unordered_set
* LRU Cache - last recently used- ![lru](https://user-images.githubusercontent.com/67040252/117773264-eba19200-b259-11eb-8879-306b26ffbfb6.JPG) When accessing element x in cache, remove corresponding list node (if exists) and add new list node to the end, update unordered_map with new list node value
* MRU - most recently used cache : remove element that has not been requested for the shortest time. std::unordered_map {key -> lastUsedTime} + lastUsedKey
When accessing element x in cache, either update corresponding lastUsedTime or remove lastUsedKey and add new key (x). Always update lastUsedKey
* LFU Cache : remove element that has been requested the least number of times
         * LFU Cache: remove element that has been requested the least number of times
         * std::unordered_map {key -> usagesCount} + std::set<{usagesCount, key}>
         * When accessing element x in cache, either either increase usagesCount in both containers (if x is present), or remove the smallest element from set (and corresponding key from unordered_map) and add new key with usagesCount=1 (O(log n))
         * Instead of using std::set<{usagesCount, key}> we can use std::unordered_map {usagesCount -> std::list<key>} and store minUsagesCount which corresponds for first non-empty list in the map
         * When accessing element x in cache, either increase usagesCount in the map and move the element to the next list and possible change minUsageCount or add new key to the map and assign minUsagesCount to 1 (O(1))

* 



   
      







