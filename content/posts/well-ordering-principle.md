---
title: Well ordering Principle
date: July 13, 2017
tags:
    - math
---

"Well Ordering Principle" is a very simple concept. It just says,

> Every non-empty subset of Natural Numbers is well ordered i.e. every such subset of Natural Numbers contains a least element.

See, nothing could be more trivial. And if you are wondering is this even
useful? Believe me, I did that the first time I heard about it and now I am its
fan. Another trivial looking principle is Pigeonhole Principle which I won't
talk in detail about here though. It says, If there are N holes and N+1
pigeons then the pigeons cannot have a hole for each, two pigeons must share a single hole.

Now let's prove a theorem using well ordering principle.
(Theorem) Let n be a positive integer such that n>1 then $n=p_1 p_2...p_k$ where all $p_i$s are prime numbers.

### Proof
Let S be a set of positive integers that cannot be written as product of
primes. By the well ordering principle S has a least element, say a. Now, if
the factors of a are a and 1 then a is a prime number and thus, this is a
contradiction(since S consists of elements which don't have prime factors).

Next, if $a$ is not prime, let $a_1$ and $a_2$ are the factors of $a$. If both of them
are prime then it again results in contradiction because $a$ can be written as
product of primes.

Now, it is obvious $a_1<a$ and $a_2<a$. If either of $a_1$ or $a_2$ can
not be written as product of primes then, either $a_1 \in S$ or $a_2 \in S$. But we already
said that $a$ is the smallest element in $S$. So, $a_1$ and $a_2$ must be product of
primes i.e. $a_1=p_1p_2...p_r$ and $a_2=q_1q_2...q_s$. Thus, $a=a_1.a_2=p_1...p_r.q_1...q_s$ which
is a prime product.

This again created a contradiction that $a \in S$. Thus, it can
be concluded that there is no positive integer > 1 that can not be written as
prime products.

Well Ordering Principle is pretty cool, right?
