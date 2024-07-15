---
title: The division algorithm
date: August 04, 2020
tags:
    - math
---

TODO... fix this

Like many things in life, there are many little things in mathematics that we take for granted. We hardly take a moment to look at them, see the beauty that they contain and that they create. The Division Algorithm, I think, is one of those beautiful little pieces in mathematics that deserves to be mentioned.

> Let a
>
> and b be integers with b>0. Then there exist unique integers q and r such that a=bq+r where 0≤r<b

This is so simple and obvious that we never bothered why is it even true.

### Existence of q and r
We deal with the uniqueness later on. Let

S=a−bk:k∈Z,a−b≥0

Now if 0∈S then a−bk=0 and thus a=bk⇒r=0.

But if 0∉S, then we first show S is non-empty. If a is positive, a−b.0=a∈S. If a is negative, a−b(2a)=a(1−2b)∈S. We see that S is non-empty either ways.

Let's recall Well ordering principle which states Every non-empty set of natural numbers contains a minimum element, that is, it is well ordered.

Following the principle, S must have a minimum element, say r. Let, r=a−bq⇒a=bq+r, r≥0.

We now show r<b. Suppose r>b then, r−b=a−bq−b=a−b(q+1) which is of the form a−bk. Thus, r−b∈S and obviously r−b<r.

But, this contradicts with the fact that r is the smallest in S, led by our assumption r>b. Thus, r<b. This proves the existence of r and q such that a=bq+r,0≤r<b.

### Uniqueness of q and r
Suppose we have another pair q′
and r′ such that a=bq′+r′,0≤r′<b. Then, bq+r=bq′+r′⇒b(q−q′)=r−r′ Let r>r′ then we have b dividing r−r′ but, 0≤r−r′≤r<b This is possible only if r−r′=0. Thus, r′=r and q′=q.

### Conclusion
The seemingly can-be-taken-for-granted statement involves pretty beautiful and not very straightforward proof. So much to learn from mathematics! I hope this was an interesting read.

NOTE: The proof comes from [Abstract Algebra Theory and Applications](https://github.com/twjudson/aata)
