---
title: Project Euler problem 25 solution
date: February 25, 2017
author: Bibek
tags:
    - math
---

> What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

The question actually asks to find the first fibonacci term, whose number of digits crosses 1000.

An obvious way to solve it is to brute force all the way to find Fn
(nth Fibonacci number) such that $log_10(F_n)$ is 1000.
The solution becomes too easy if we use the Golden ratio $\phi=1.61803398875$

After some research on Golden ratio and Fibonacci numbers, we can find out an important fact that

> $\phi^{n-2} \leq F_n$

Now, if a number N has n digits in it then, $log_{10}N=n−1$
. For example, $log_{10}100=2$ and $log_{10}999=2.999$.
So, for 1000 digits, its logarithm is 999
because both 100 and 999 have 3 digits.

Using this fact in the above inequality(greater than sign is omitted as we are concerned with the first number to have 1000 digits),

$log(ϕ^{n−2})=999$

$or, (n−2)∗log(ϕ)=999$

$or,(n−2)∗0.2089=999$


which gives $n= 4782$, our answer.
Cheers!!
