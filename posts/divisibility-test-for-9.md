---
title: "Divisibility test for 9: How and why is it so?"
date: Oct 31, 2017
tags:
    - math
---

We have studied in our 4th or 5th grade that that if the sum of the digits of a number is divisible by 9 then the number is divisible by nine.

For example:
72 is divisible by 9 because, 7+2=9 which is divisible by 9.
198 is divisible by 9 because, 1+9+8=18 which is divisible by 9.

Now, why is it so??

Any number can be written terms powers of 10:

1234=1∗1000+2∗100+3∗10+4∗1

32=3∗10+2∗1

In similar fashion, any number can be written as,

n=a1∗1+a2∗10+a3∗100+...

And,

1=0+1,

10=9+1,

100=99+1 , and so on.

So,

n=a1∗(0+1)+a2∗(9+1)+a3∗(99+1)...

Separating the sums (using associativity),

or,n=(a1∗0+a2∗9+a3∗99+...)+(a1∗1+a2∗1+a3∗1+...)

or,n=9∗(a1∗0+a2∗1+a3∗11+...)+(a1+a2+a3+...)

or,n=9∗X+Sumofdigits

Now comes the reason.

If n is divisible by 9, the right hand side should also be divisible by 9. It is obvious that 9∗X is divisible by 9. And thus, Sumofdigits is forced to be divisible by 9.

That's where divisibility test for 9 came from.


