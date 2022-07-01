## Python Notes

    string = "This is a string" #str
    integer = 69                #int
    decimal = 3.14              #float
    boolean = True              #bool
    imaginary = 2j              #complex


type(str(True)) This is an example of type casting. This will show the type as a string, when it's a boolean wrapped as a string.

bool(integer) As long as the integer is not 0 (or empty) it will show as True, otherwise if the integer equals to 0 (or empty) it will be false.

dir - Will tell you what you can do.

tuples are the same as lists but you can't tell it to change a value of a position

```python
x = [1,2,3,4,5]
id(x)
472

x += [6,7,8]
```

type - Will tell you what that object is

help - Will tell you about the object

round

len - tells you the lenght of an int

Sets:

```python
x = {1,2,3,4,5}
type (x)
```

Set is the fast data stucture in python, since it is not indexable there is no gurantee that the data will return in order. It is unordered. 

Sets are unique

When you set a list or tuple you are removing the duplicate values (if there are any) of the same type. IE `[1,2,3,4,5[1,2,3],[1,2,3,4]` <- Contains multiple lists. If you try to Set this it will not allow it due to it being unhashable