---
title: "Divisibility test for 9: How and why is it so?"
date: Oct 31, 2017
tags:
    - math
---

We have studied in our 4th or 5th grade that that if the sum of the digits of a number is divisible by 9 then the number is divisible by nine.

**For example:**

72 is divisible by 9 because, $7 + 2 = 9$ which is divisible by 9.

198 is divisible by 9 because, $1 + 9 + 8 = 18$ which is divisible by 9.

**Now, why is it so??**

Any number can be written terms powers of 10:

$1234 = 1 \times 1000 + 2 \times 100 + 3 \times 10 + 4 \times 1$

$32 = 3 \times 10 + 2 \times 1$

In similar fashion, any number can be written as,

$$n = a_1 \times 1 + a_2 \times 10 + a_3 \times 100 + \ldots$$

And,

$100 = 99 + 1$, and so on.

So,

$$n = a_1 \times (0 + 1) + a_2 \times (9 + 1) + a_3 \times (99 + 1) \ldots$$

Separating the sums (using associativity),

$$n = (a_1 \times 0 + a_2 \times 9 + a_3 \times 99 + \ldots) + (a_1 \times 1 + a_2 \times 1 + a_3 \times 1 + \ldots)$$

$$n = 9 \times (a_1 \times 0 + a_2 \times 1 + a_3 \times 11 + \ldots) + (a_1 + a_2 + a_3 + \ldots)$$

$$n = 9 \times X + \text{Sum of digits}$$

**Now comes the reason.**

If $n$ is divisible by 9, the right hand side should also be divisible by 9. It is obvious that $9 \times X$ is divisible by 9. And thus, $\text{Sum of digits}$ is forced to be divisible by 9.

That's where divisibility test for 9 came from.
