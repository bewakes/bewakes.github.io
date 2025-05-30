---
title: The division algorithm
date: August 04, 2020
tags:
    - math
---

Like many things in life, there are many little things in mathematics that we take for granted. We hardly take a moment to look at them, see the beauty that they contain and that they create. The **Division Algorithm**, I think, is one of those beautiful little pieces in mathematics that deserves to be mentioned.

> Let $a$ and $b$ be integers with $b > 0$. Then there exist unique integers $q$ and $r$ such that  
>   
> $$
> a = bq + r
> $$  
>   
> where $0 \leq r < b$

This is so simple and obvious that we never bothered why is it even true.

---

## Existence of $q$ and $r$

We deal with the uniqueness later on. Let

$$
S = a - bk : k \in \mathbb{Z}, a - b \geq 0
$$

Now if $0 \in S$ then $a - bk = 0$ and thus $a = bk \Rightarrow r = 0$.

But if $0 \notin S$ then we first show $S$ is non-empty. If $a$ is positive, $a - b \cdot 0 = a \in S$. If $a$ is negative,

$$
a - b(2a) = a(1 - 2b) \in S
$$

We see that $S$ is non-empty either way.

Let's recall the **Well ordering principle** which states:  
_Every non-empty set of natural numbers contains a minimum element, that is, it is well ordered._

Following the principle, $S$ must have a minimum element, say $r$.  
Let,

$$
r = a - bq \Rightarrow a = bq + r,\quad r \geq 0
$$

We now show $r < b$. Suppose $r > b$, then:

$$
r - b = a - bq - b = a - b(q + 1)
$$

which is of the form $a - bk$. Thus, $r - b \in S$ and obviously $r - b < r$.

But this contradicts the fact that $r$ is the smallest in $S$, led by our assumption $r > b$. Thus, $r < b$. This proves the existence of $q$ and $r$ such that:

$$
a = bq + r,\quad 0 \leq r < b
$$

---

## Uniqueness of $q$ and $r$

Suppose we have another pair $q'$ and $r'$ such that:

$$
a = bq' + r',\quad 0 \leq r' < b
$$

Then,

$$
bq + r = bq' + r' \Rightarrow b(q - q') = r - r'
$$

Let $r > r'$, then we have $b$ dividing $r - r'$, but:

$$
0 \leq r - r' \leq r < b
$$

This is possible only if $r - r' = 0$. Thus, $r' = r$ and $q' = q$.

---

## Conclusion

The seemingly _can-be-taken-for-granted_ statement involves pretty beautiful and not very straightforward proof. So much to learn from mathematics! I hope this was an interesting read.

> **NOTE**: *The proof comes from* _Abstract Algebra Theory and Applications_

