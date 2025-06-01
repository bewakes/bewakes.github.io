---
title: Performing division without division
date: Jan 05, 2021
tags:
    - math
    - computer-science
location: Bharatpur
---

Suppose we live in a world where there was no division operator like we have for addition, subtraction, and multiplication. In fact, we don't need to suppose this scenario, because in highly efficient computers such as supercomputers, using a division operator takes significantly more time than multiplication, addition, and subtraction. Fortunately, division can be done just by using multiplication and subtraction, and with proper initial guess, within 6 steps in general. Interesting isn't it?


## Enter Newton Raphson Method

It is an iterative method to find out roots of an equation. For example, we can find the roots of the equation:

$$
x^2 - 2x + 5 = 0
$$

or,

$$
f(x) = x^2 - 2x + 5 = 0
$$

without performing analytical operations like factoring.

### The steps are:

1. Find the derivative of the function analytically. In the above case it is:
  $$
  f'(x) = 2x - 2
  $$

2. Start with a guess for \( x \).
3. The next value for \( x \) is given by:
  $$
  x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
  $$
  where \( i \) is the iteration number, initially 0.
4. Repeat the above process until the values obtained for \( x \) seem to converge.


## But how does this help our division?

We can think of division \( a / b \) as \( a \cdot (1 / b) \), that is, multiplication of \( a \) and the inverse of \( b \). Hence our task is just to find out the inverse of \( b \).

If \( x \) is the inverse of \( b \), we have:

$$
x = \frac{1}{b} \quad \text{or} \quad b = \frac{1}{x}
$$

That is,

$$
f(x) = \frac{1}{x} - b = 0
$$

The derivative:

$$
f'(x) = -\frac{1}{x^2}
$$

So far so good. Unless… You notice that the formula for \( x_{i+1} \) itself involves division: \( \frac{f(x_i)}{f'(x_i)} \).

We'll simplify it!

Continuing with our inverse calculation, and using the formula for iteration we have:

$$
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

$$
= x_i - \frac{\frac{1}{x_i} - b}{-\frac{1}{x_i^2}}
$$

$$
= x_i + x_i^2 \left(\frac{1}{x_i} - b \right)
$$

$$
= x_i + x_i - b x_i^2
$$

$$
= 2x_i - b x_i^2
$$

That's it. **No division!**


## Seeing it in action

Let's find out the inverse of:

$$
b = 5
$$

Start with an initial guess \( x_0 = 0.1 \)

> Note: There are lookup tables for finding out initial guess (And initial guess does matter!) But a general rule of thumb is that we can use 0.1 for single digit numbers, 0.01 for two digit numbers, 0.001 for 3 digit numbers and so on.

So, with our initial guess of 0.1, the next values for \( x \) will be:

$$
x_1 = 2x_0 - 5x_0^2 = 2 \cdot 0.1 - 5 \cdot 0.1^2 = 0.19
$$

$$
x_2 = 2x_1 - 5x_1^2 = 2 \cdot 0.19 - 5 \cdot 0.19^2 = 0.1995
$$

$$
x_3 = 2x_2 - 5x_2^2 = 2 \cdot 0.1995 - 5 \cdot 0.1995^2 = 0.2000
$$

In just **3 steps**! Without division.


I hope this was interesting.

