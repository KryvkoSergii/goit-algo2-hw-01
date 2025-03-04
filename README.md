# Home work 1

## Task 1. Finding the maximum and minimum elements
According to master theorem
![master theorem](/doc/image.png)

where

a≥1— the number of subtasks at each level, i.e. how many subtasks are created.

b>1— the problem size reduction factor. It shows how many times the problem size is reduced at each recursion step.

f(n)— the additional cost not related to recursive calls (for example, the cost of merging in the Merge Sort algorithm). In fact, this is the cost of additional work at each level of recursion, i.e. the work that is performed after splitting into subtasks.

In our case a=2, b=2, f(n)=f(1). 

For our case is:
![first case](/doc/image-1.png)

### the time complexity is O(n)

## Task 2. Finding the k-th smallest element
Implement an algorithm for finding the k-th smallest element in an unsorted array using the Quick Select principle.

## Run test
```bash
python -m unittest .\tests\testFunc.py
```