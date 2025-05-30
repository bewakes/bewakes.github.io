---
title: Probability that any two numbers are prime
date: July 03, 2019
tags:
    - math
location: Patan
---

Two numbers are relatively prime if they have no common divisors except 1. It also means that the numbers have no prime factor in common.

The probability that a number is divisible by 2 is $1/2$.  
The probability that two numbers are both divisible by 2 is $(\frac{1}{2})^2 = \frac{1}{4} = \frac{1}{2^2}$.  
And thus, probability that neither of the two numbers are divisible by 2 is:

$$
\left(1 - \frac{1}{2^2} \right)
$$

Similarly, probability that neither of the two numbers are divisible by 3 is:

$$
\left(1 - \frac{1}{3^2} \right)
$$

Thus the probability that neither of the two numbers are divisible by any of the prime numbers is:

$$
P(\text{RelativelyPrime}) = \left(1 - \frac{1}{2^2} \right)\left(1 - \frac{1}{3^2} \right)\left(1 - \frac{1}{5^2} \right)\left(1 - \frac{1}{7^2} \right)\cdots
$$

However, this is the minimum probability limit for any two numbers being relatively prime.

> "Wait, but that's an infinite product. What am I gonna do with that big product?"

We'll see.

Let's introduce an infinite sum,

$$
S = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \frac{1}{5^2} + \cdots
$$

Multiplying both sides by $\frac{1}{2^2}$:

$$
\frac{1}{2^2} \cdot S = \frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{6^2} + \frac{1}{8^2} + \frac{1}{10^2} + \cdots
$$

Subtracting the last term from $S$:

$$
\left(1 - \frac{1}{2^2} \right) \cdot S = 1 + \left(\frac{1}{3^2} + \frac{1}{5^2} + \frac{1}{7^2} + \frac{1}{9^2} + \cdots\right)
$$

All the multiples of 2 are gone.

Now, multiply $S_1$ by $\frac{1}{3^2}$:

$$
\frac{1}{3^2} \cdot S_1 = \frac{1}{3^2} + \frac{1}{9^2} + \frac{1}{15^2} + \frac{1}{21^2} + \cdots
$$

Subtracting the last term from $S_1$:

$$
\left(1 - \frac{1}{3^2} \right) \cdot S_1 = 1 + \frac{1}{5^2} + \frac{1}{7^2} + \frac{1}{11^2} + \cdots + \frac{1}{23^2} + \frac{1}{25^2} + \cdots
$$

All the remaining multiples of 3 are gone.

If we continue this with all the prime numbers, all the terms on the right are gone except 1:

$$
S \cdot \left(1 - \frac{1}{2^2} \right)\left(1 - \frac{1}{3^2} \right)\left(1 - \frac{1}{5^2} \right)\left(1 - \frac{1}{7^2} \right)\left(1 - \frac{1}{11^2} \right)\cdots = 1
$$

So,

$$
S = \frac{1}{\left(1 - \frac{1}{2^2} \right)\left(1 - \frac{1}{3^2} \right)\left(1 - \frac{1}{5^2} \right)\left(1 - \frac{1}{7^2} \right)\left(1 - \frac{1}{11^2} \right)\cdots}
$$

At the beginning, we defined:

$$
S = \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \frac{1}{5^2} + \cdots
$$

This is a very famous sum defined as:

$$
\zeta(s) = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \frac{1}{5^s} + \cdots
$$

Where $s$ is a complex number.

It might be surprising, but it is true that:

$$
\zeta(2) = \frac{\pi^2}{6}
$$

The proof to this fact is here.


So, going back to our original question,

$$
P(\text{RelativelyPrime}) = \left(1 - \frac{1}{2^2} \right)\left(1 - \frac{1}{3^2} \right)\left(1 - \frac{1}{5^2} \right)\left(1 - \frac{1}{7^2} \right)\cdots
$$

$$
P(\text{RelativelyPrime}) = \frac{1}{\zeta(2)}
$$

$$
P(\text{RelativelyPrime}) = \frac{1}{\pi^2/6}
$$

$$
P(\text{RelativelyPrime}) = \frac{6}{\pi^2}
$$

There we go!! Probability that any two numbers are relatively prime to each other is not a very complicated expression.


*July 04, 2019, Patan Dhoka*

