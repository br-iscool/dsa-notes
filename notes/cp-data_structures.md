# Competitive Programming Data Structures Notes

## Data Structures

A data structure is a way to store data in the memory of a computer. It is important to choose an appropriate data structure for a problem because each data structure has advantages and disadvantages. 

Across the majority of programming languages, *arrays* are a type of data structure which can store multiple values in a single variable. There are two types of arrays, static and dynamic arrays. 

- Static Array
  - In this type of array, memory is allocated at compile time. The size of the array is fixed, and cannot be altered or updated.
- Dynamic Array
  - In this type of array, memory is allocated at run time. However, the memory doesn't have a fixed size, meaning users can declare any size of an array when they create it. 

Arrays (and other similar data structures) all have a few properties in common. 

1. Ordered / Unordered
   - When data structures are described as being ordered, it means that the items in the data structure have a defined order. Objects in the data structure can be described as coming "before" or "after" another object. 
2. Mutability
   - Mutability / changeability means that we can add, remove, or modify items in a data structure after it has been created. 
3. Duplicates
   - Some data structures allow having duplicate elements, while others do not. 

The following section will first introduce the four main data structures, other important data structures, and their implementations in Python. 

### List

In Python, a list is an implementation of the dynamic array. Lists are created with square brackets ```list1 = []``` and are ordered, mutable, and allow duplicates. 

It is possible to use the ```list()``` constructor to create lists.

### Tuple

A tuple is another built-in data structure in Python that can be created with round brackets (parentheses) ```tuple1 = ()```. The primary defining characteristic between lists and tuples is mutability. Tuples cannot be modified, added to, or deleted once they have been created. Otherwise, tuples are ordered and allow duplicates. 

In order to create a tuple with only one item, a comma has to be placed behind the item. ```tuple1 = ("mango",)```

It is possible to use the ```tuple()``` constructor to create tuples. 

### Set

Sets are another type of data structure in Python that are created with curly brackets ```set1 = {}```. Sets are unordered, unindexed, and do not allow duplicates. Because they are unordered, set items appear in a different order each time they are used, and cannot be referred to by an index.

A notable property of sets is their mutability. Existing items in the set cannot be modified, but items can be added or removed. 

It is possible to use the ```set()``` constructor to create sets. 

Frozensets are versions of sets that are completely immutable. Unlike regular sets, elements can't be added or removed from frozensets. It is possible to use the ```frozenset()``` constructor to create frozensets. 

### Dictionary

Dictionaries are a data structure in Python that are used to store data in ```key: value``` pairs. Dictionaries are created using curly brackets, and have keys and values. Dictionaries are ordered, mutable, and do not allow duplicates.

An example of a dictionary:
```python
dict1 = {
   "type": "fruit",
   "name": "mango"
}
```

It is possible to use the ```dict()``` constructor to create dictionaries.

