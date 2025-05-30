---
title: Implementing dictionaries as functions(Javascript)
date: September 15, 2020
tags:
    - programming
    - functional-programming
lcoation: Bharatpur
---

>   Warning: Please don't try this at production. This is just for demonstration purpose.

This article was concieved when [my friend](https://gnikesh.com/) introduced me to the concept of dictionaries as functions.

Imagine a language very similar to javascript which did not have objects or say dictionaries in it. Dictionaries are the data structures that store key-value pairs and the values are accessed by specifying keys which we call lookup. Lookups in dictionary are constant time operations[not in the one we are implementing]. But we sure won't bother with hashing and all.
Recap of JS arrow syntax

Arrow syntax comes with javascript es6. There are tons of articles about that. Let's just recap the basic notation here.

```javascript
// Traditional function
function myFucntion(arg1, arg2) {
    // do something
    return 0;
}

// Equivalent to
const myFunction = (arg1, arg2) => {
    // do something
    return 0;
}

// Another traditional function
function getInitialObject(arg1) {
    return {
        a: 1,
        b: 2
    };
}

// Equivalent to                   v------ Note the braces before object initialization
const getInitialObject = (arg1) => ({a: 1, b: 2});  // We don't need return statement

// Function returning function
function getArithmeticFunction(operation) {
        reurn function(x, y) {  // This is an anonymous function
            return operation == 'add' ? x + y : x - y;
        };
}

// Equivalent to
//  Function argument -------------v           v--------- Returned function arguments
const getArithmeticFunction = (operation) => (x, y) => operation == 'add' ? x + y : x - y;
```

### Our Dictionary Implementation

Our dictionary is just going to be a function that takes a key and returns the value if present else undefined. Let's create a constructor function that returns a new dictionary.

```javascript
const newDict = () => (key) => undefined;

let dict = newDict();
```

So far so easy. The function newDict returns another function, our dictionary, that returns undefined for any key because it does not have any entries in it now.

Lookup is very easy, just call the dictionary function.

```javascript
const val = dict(key);
// dict("anykey") --> undefined, because dictionary is empty
```

Let's create a function that inserts some key value to our dictionary.

```javascript
const insert = (dict, k, v) => (x) => x == k ? v : dict(x);

dict = insert(dict, "newkey", 5); // Now holds value for "newkey"
dict = insert(dict, "anotherkey", 10); // Now holds value for "another key"
// dict("newkey") --> 5
// dict("anotherkey") --> 10
// dict("any other key") --> undefined
```

This insert function takes in a dictionary, key and a value and returns a dictionary(which should be another function). Note that the original dictionary is not modified at all. We completely return a new dictionary function.

There we go! A fully functional dictionary where we can insert and lookup values. Why not try popping keys out?

```javascript
const pop = (dict, k) => (x) => x == k ? undefined : dict(x);
dict = pop(dict, "newkey");
// dict("newkey") --> undefined
// dict("anotherkey") --> 10
// dict("any other key") --> undefined
```

### Limitations
It's highly important to be aware of the limitations though. Our dictionary cannot list out the keys and values present. To support that we need to modify the structure quite a bit. I don't think that's much fun though.

### Bonus
What if we want to transform all the values of the dictionary by a function, say squaring the values(assuming number values)? Well that's pretty straightforward and cool!

```javascript
const mapDictionary = (dict, mapFunction) => (x) => {
    const originalValue = dict(x);
    return originalValue && mapFunction(originalValue);
}
dict = insert(dict, "five", 5);
dict = insert(dict, "six", 6);

const square = (x) => x * x;
const squaredDictionary = mapDictionary(dict, square);
squaredDictionary("five"); // 25
squaredDictionary("bla"); // undefined because this key does not exist

// One more example
const isEven = (x) => x % 2 == 0;
const isEvenDictionary = mapDictionary(dict, isEven);
isEvenDictionary("five"); // false
isEvenDictionary("six"); // true
isEvenDictionary("bla"); // undefined
```

This, I think, is one of the many many beauties of functional programming.
