---
title: Performing division without division
date: Jan 05, 2021
tags:
    - math
    - computer-science
location: Bharatpur
---

TODO: fix this

Suppose, we live in a world where there was no division operator like we have for addition, subtraction and multiplication. In fact, we don't need to suppose this scenario, because in highly efficient computers such as supercomputers, using a division operator takes significantly more time than multiplication, addition and subtraction. Fortunately, division can be done just by using multiplication and subtraction, and with proper initial guess, within 6 steps in general. Interesting isn't it?
Enter Newton Raphson Method

It is an iterative method to find out roots of an equation. For example, we can find the roots of the equation: x2−2x+5=0
or,f(x)=x2−2x+5=0

without performing analytical operations like factoring.

The steps are:

* Find the derivative of the function analytically. In the above case it is f′(x)=2x−2
*Start with a guess for x.
* The next value for x is given by xi+1=xi−f(xi)/f′(xi) where i is iteration number initially 0.
* Repeat the above process until the values obtained for x seem to converge.

**But how does this help our division?**

We can think of division a/b
as a∗(1/b) that is, multiplication of a and the inverse of b. Hence our task is just to find out the inverse of b.

If x
is the inverse of b, we have: x=1/b or,b=1/x that is, f(x)=1/x−b=0 The derivative f′(x)=−1/x2

So far so good. Unless... You notice that the formula for xi+1
itself involves division: f(xi)f′(xi).

We'll simplify it!

Continuing with our inverse calculation, and using the formula for iteration we have: xi+1=xi−f(xi)/f′(xi)
or,xi+1=xi−1/xi−b−1/x2i or,xi+1=xi+x2i(1/xi−b) or,xi+1=xi+xi−bx2i or,xi+1=2xi−bx2i

That's it. No division!
Seeing it in action

Let's find out the inverse of 5. b=5
Start with an initial guess x0=0.1

Note: There are lookup tables for finding out initial guess(And initial guess does matter!) But a general rule of thumb is that we can use 0.1 for single digit number, 0.01 for two digit numbers, 0.001 for 3 digit numbers and so on.

So, with our initial guess of 0.1, the next values for x
will be x1=2x0−5x20=2∗0.1−5∗0.12=0.19 x2=2x1−5x21=2∗0.19−5∗0.192=0.1995 x3=2x2−5x22=2∗0.1995−5∗0.19952=0.2000

In just 3 steps ! Without division.

I hope this was interesting.

[Reference](http://nm.mathforcollege.com/topics/newton_raphson.html)
