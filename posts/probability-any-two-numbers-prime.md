---
title: Probability that any two numbers are prime
date: July 03, 2019
tags:
    - math
location: Patan
---

TODO.... fix this


Two numbers are relatively prime if they have no common divisors except 1. It also means that the numbers have no prime factor in common.

The probability that a number is divisible by 2
is 1/2.
The probability that two numbers are both divisible by 2 is (12).12=122. And thus, probability that neither of the two numbers are divisible by 2 is (1−122)

Similarly, probability that neither of the two numbers are divisible by 3
is (1−132)

Thus the probability that neither of the two numbers are divisible by any of the prime numbers is P(RelativelyPrime)=(1−122).(1−132).(1−152).(1−172)...

However, this is the minimum probability limit for any two numbers being relatively prime.

"Wait, but that's an infinite product. What am I gonna do with that big product?"

We'll see.

Let's intruduce an infinite sum, S=112+122+132+142+152+...
Multiplying both sides by 122

,

122.S=122.112+122.122+122.132+122.142+122.152+...
122.S=122+142+162+182+1102+...

Subtracting the last term from S
, (1−122).S=1+(122−122)+132+(142−142)+152+...

S1=(1−122).S=1+132+152+172+192...

All the multiples of 2 are gone.

Now, multiply S1
by 132. 132.S1=132.1+132.132+132.152+132.172...

Subtracting the last term from S1
. (1−132).S1=1+152+172+(192−192)+... (1−132).S1=1+152+172+1112+...+1232+1252+... (1−132).(1−122).S=1+152+172+1112+...+1232+1252+...

All the remaining multiples of 3 are gone.

If we continue this with all the prime numbers, all the terms on the right are gone except 1. S.(1−122).(1−132)(1−152)(1−172)(1−1112)...=1
So, S=1(1−122).(1−132)(1−152)(1−172)(1−1112)... (1−122)(1−132)(1−152)(1−172)(1−1112)...=1S At the beginning, we defined S=112+122+132+142+152+... This is a very famous sum defined as, ζ(2)=112+122+132+142+152+... The very beautiful symbol ζ is called Reimann Zeta Function named after the mathematician Bernhard Riemann. It is defined for all complex numbers as, ζ(s)=11s+12s+13s+14s+15s+... where s

is a complex number.

It might be surprising, but it is true that ζ(2)=π26

The proof to this fact is [here](https://bewakes.com/posts/zeta-of-2-is-pi-squared-by-6/).

So, going back to our original question, P(RelativelyPrime)=(1−122).(1−132).(1−152).(1−172)...
P(RelativelyPrime)=1ζ(2) P(RelativelyPrime)=1π26 P(RelativelyPrime)=6π2

There we go!! Probability that any two numbers are relatively prime to each other is not a very complicated expression.
