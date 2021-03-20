**Map**
* Applies function on each element in iterrable object
* Map returns map object, we should make list again
* new_list = list(map(func, itter)

**Lambda**
* Function written in 1 row
* lambda input1: operation with input
* Often used with map 
* Ex/ list(map(lambda x: round(x/2,3) iter))
* Also can be used with 2 itter: list(map(lambda x,y: x+y, itter1, itter2)))

**Filter**
* creates a list of elements for which a function returns true
* list(filter(lambda x: x.startswith('M'), itter)

**Reduce**
* import functools.reduce
* input function and itter, returns 1 element 
* sum = functools.reduce(lambda x, y: x + y, items)

**List Comprehension**
* my_lst = [i for i in range(1, 20)]
* list_2 = [number for number in list_1 if number % 2 == 0]
* list_3 = [x if x < 0 else x** 2 for x in list_1]
* На следующем примере мы считаем количество символов в строке и если меньше 5 то
мы конкатенируем слово - smaller, а если больше то слово more, также мы фильтруем
так, что только попадаются строка в котором только буквы
* names = ["raychel", "john", "peter", "jessica", "jill", "steven", "Catherine", "james",
"steven123", "Kira123"]
filtered_names = [x + "more" if len(x) >= 5 else x + "smaller" for x in names if x.isalpha()]
print(filtered_names)
['raychelmore', 'johnsmaller', 'petermore', 'jessicamore','jillsmaller', 'stevenmore', 'Catherinemore', 'jamesmore']

**Dictionary Comprehension**
* f_dict = {f:i for i,f in enumerate(fruits)}
* fruits = ['apple', 'mango', 'banana','cherry']
* dict comprehension to create dict with fruit name as keys
* {f:len(f) for f in fruits}
* dict_123 = {value: key for key, value in dict_abc.items()}
* 

