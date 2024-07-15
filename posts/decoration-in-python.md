---
title: Decoration with Decorators(Python)
date: March 12, 2018
tags:
    - programming
    - python
---

Decorators let us decorate and make things beautiful. So does python. It lets us decorate functions and classes. Let's see how.

### Functions are 'first class citizens'
First class citizens is just a fancy name for things in a computer program that can be treated as 'values', assigned to, passed around functions, returned from function and so on. The easiest and the most basic first class citizen that we can think of in python is an integer. Consider 5, which is an integer and can be assigned to variables, sent to functions or returned from functions.

To understand why functions are first class citizens, let's create some functions:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
```

I know, I know. There's nothing new with them. Everybody knows how to define functions. Let's define another function:

```python
def apply(function, x, y):
    return function(x, y)
```

Now this is something. With the apply function, we can do things like:

```python
apply(add, 3, 4)
# >>> 7
apply(subtract, 2018, 1994)
# >>> 24
```

See, we've passed our functions add and subtract to the function apply just like we've passed in 3, 4 and 2018, 1994. One reason why functions are first class citizens.

Let's write some more functions.

```python
def get_function(name):
    if name == 'add':
        return add
    elif name == 'subtract':
        return subtract
    elif name == 'multiply':
        f = lambda x, y: x*y
        # Congratulations! we've just assigned a function(lambda) to a value(f)
        # The lambda expression is equivalent to:
        # def f(x, y)
        #  return x*y
        # The values before ':' are arguments and after ':' is the return value.
        return f
    elif name == 'divide':
        def divide(x, y):  # Yes, we can define a function inside a function.
            return x/y
        # However, we can't call 'divide' outside 'get_function', but we can return 'divide'. Of course!!
        return divide
```

Contratulations!! we've returned function from a function. Next reason why functions are first class citizens. Why not see it in action?

```python
add_function = get_function('add')
add_function(5, 6)
# >>> 11
get_function('subtract')(3, 4)
# This evaluates to: subtract(3, 4)
# >>> -1
get_function('multiply')(8, 11)
# >>> 88
```

### Decorators

Decorators are functions, which return another function. It often happens in python that we want to add some common but extra functionality to python functions. Let's say we want to print how long a function took to execute. We can do this:

```python
def my_function_to_be_tracked(value):
    print('The value passed is {}'.format(value))

# code to track time for our function
import time
start = time.time()
my_function_to_be_tracked("hello there")
end = time.time()
print("elapsed time: ", start - end)
# >>> hello there
# >>> elapsed time: 123.33 ms
```

Yukk!! It works, but I am not going to write this mess for every function I am going to time track.

A better approach would be:

```python
def tracker(func_to_be_tracked):
    def wrapper(value):
        start = time.time()
        function_to_be_tracked(value)
        end = time.time()
        print("elapsed time: ", start - end, "ms")
    return wrapper

# now we can do this
tracked_func = tracker(my_function_to_be_tracked)
tracked_func("hello there")  # This works!!
# >>> hello there
# >>> elapsed time: 123.33 ms
another_tracked_function = tracker(another_function_with_single_arg)  # This works like charm as well.
```

Quite clean, right? Python lets even cleaner code:

```python
@tracker  # this is actually decorator syntax
def my_function_to_be_tracked(value):
    print('The value passed is {}'.format(value))

# it will be equivalent to
my_function_to_be_tracked = tracker(my_function_to_be_tracked)
# and we can now call it as
my_function_to_be_tracked('hello')
# >>> hello
# >>> elapsed time: 123.11 ms
```

That's all about decorators. Just a syntactic sugar to the wrapper function and renaming the returned function to the wrapped function's name.
However, the tracker wrapper can wrap only the functions with single argument. It is because the wrapper function inside takes only single parameter. We can generalize this to function taking any parameters using the sweet python constructs *args and **kwargs as:

```python
def tracker(func_to_be_tracked):
    def wrapper(*args, **kwargs):
        start = time.time()
        function_to_be_tracked(*args, **kwargs)
        end = time.time()
        print("elapsed time: ", start - end, "ms")
    return wrapper
```

Cool!! Now we're ready to write codes with decorators. I'll write about decorators taking arguments next time.
Till then, keep decorating !!

> This article is inspired by [this article](https://realpython.com/blog/python/primer-on-python-decorators/)
