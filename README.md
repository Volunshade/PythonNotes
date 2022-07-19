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

## Strings

```python

message = 'Hello World'

 Print Welcome Message
print('Hello world')
````

 Python doesn't need semi colons to end each line as it operates on white space alone. variables are all lower case and if multiple words they are separated by _ 

 Varibles can be simple, however if they are simple with no documentation on what they are others could get confused by looking at the code

```python

m= 'Hello World'
print('Hello world')
````

 You can use a variable similar to below.

```python
message = 'Hello World'
print(message)
```

 In a string if you need a multiple line sting you'd add three " to the beginning and end. Example below

```python
message = """Bobb's World was a good
cartoon in the 1990s"""
```

 len function will determine the length of the string.

```python

```python
message = 'Hello World'
print(len(message))
```

 You can add [] in the string to access the index.

```python
message = 'Hello World'
print(message[0])
```

 To get a range of the index you can do a slice. In the example below
 0 = H and 5 = the space between Hello and World
 Position of the index starts at ***0***
```python
message = 'Hello World'
print(message[0:5])
```

 Method is a function that belongs to an objection

 .lower can turn the sting to lower case as seen in the example below.

```python
message = 'Hello World'

print(message.lower())
```

 .upper will change it to upper case.

```python
message = 'Hello World'

print(message.upper())
```

 .count will count how many characters match in the message.

 .replace will replace the values to what you want them to be. If you don't use a new varible or overwrite them it won't return anything.

```python
message = 'Hello World'

message = message.replace('World', 'Universe')
print(message)
```

 In order to concatenate multiple strings you can use a + sign however if a long string it can get long.
 For formated strings you can do something similar to the second example

```python

greeting = 'Hello'
name = 'Michael'

message = greeting +', ' + name

print(message)
```

 Result = Hello, Michael

```python


greeting = 'Hello'
name = 'Michael'

message = '{}, {}. Welcome!'.format(greeting, name)

print(message)

```

 3.6 and above you have access to f strings like below. Still very new in python.

```python


greeting = 'Hello'
name = 'Michael'

message = f'{greeting}, {name}. Welcome!'

print(message)

```

 can use things like .upper in the f strings by adding it into the varible. 

 dir() shows all attributes and methods that are available to be used.

## Lists , Tuples, and Sets

 Lists has alot more functionality compared to Tuples and Sets.
 Lists use square brackets []

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

print (courses)

```

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

print (courses[0])

```

 Result will be History

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

print (courses[3])

```

 Result wil be Compsci
 Can use negative indexs

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

print (courses[-1])

```

 Result will be Compsci
 If you try to access an index that doesn't exist you will get a error
 You can get a range of indexes by slicing the index field. x:y The Y will show the index before that value.
 to add an item to the end of a list you would want to use the append function

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

courses.append('Art')
print (courses)

```

 to insert a value to a specific location in the list you will need to use insert

```python

courses = ['History', 'Math', 'Physics', 'Compsci']

courses.insert(0, 'Art')
print (courses)

```

 You can insert a list into a list with the insert method.

```python

courses = ['History', 'Math', 'Physics', 'Compsci']
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print (courses)

```

 Results will be [['Art', 'Education'], 'History', 'Math', 'Physics', 'Compsci']

 if you want to add a second list you will want to use extend.

```python

courses = ['History', 'Math', 'Physics', 'Compsci']
courses_2 = ['Art', 'Education']
courses.extend(0, courses_2)
print (courses)

```

 Results will be ['Art', 'Education', 'History', 'Math', 'Physics', 'Compsci']

 If you want to remove a value you'd want to use the remove method
 If you want to use the list as a cude you can use the pop method which will pop off the value 
 If you want to see your list in reverse, you'd want to use the reverse method. 
 If you want to sort your list you'd want to use the sort method.

## Dictionaries 

 Key valued pairs, these are two linked values where the key is a unique identifier. 

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

print(student['name'])

```

 results pass back the name field. 
 The data can be any immutable data type.
 if you try to access a key where no data exists it will error out.
 .get method will pull the data without erroring out if there is a key that doesn't exist it will come back as none.  
 This is unless you pass a second arguement specifying what you want.

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

print(student.get{'phone', 'Not Found'})

```

 Results will print out Not Found for Phone number

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

student['phone'] = '555-5555'

print(student.get{'phone', 'Not Found'})

```

 Result will be that the number 555-5555 will show up since you added the phone to the dictionary in the second line.
 you can also update using the update method using similar as below.

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

student.update({'name': 'Jane', 'age':26, 'phone':'555-5555'})

 print(student.get{'phone', 'Not Found'})
print(student)

```

 results will update the name to jane, age to 26 and add in the phone number.
 If you wanted to delete a record you would use the del on the key or use the pop method.

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

del student['age']

print(student)

```

 Results when printed is that there will be no age returned.
 to loop through all the data in a dictionary you can do the following.

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

for key in studen:
    print(key)

```

 This will print out the keys.
 To loop through the keys and values you will need to use the .items method.

```python

student = {'name':  'John', 'age': 25, 'courses': ['Math', 'Compsci']}

for key, value in student.items():
    print(key,value)

```

 Results this will print out the key and values for each key. 

