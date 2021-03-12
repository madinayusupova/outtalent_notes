# Lesson2 
## List vs Arrays
* Python list is built as an array
* Phyton list/Array Reading O(1), inserting O(n)  since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space
* Python is a "higher level" programming language, so you can accomplish a task with little code
* Run time of len() - O(1)

## Linked List
* Each element in array stores value and index, while in linked list each element stores value and reference to the next element
* when you insert new element into linked list, firstly add link from new element to next one, before link from previous to new. so you don't lose a reference
* insertion, deletion - O(1)
* Doubly linked list - where you have pointers to the next element and the previuos element

## Stacks
*  You put elements on top and remove or look at the top element
*  Useful when you care about only recent elements or the order in which you see and save elements matters
*  Add element = push, Remove = pop
*  in python we can use linked list to implement stack 
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
    

