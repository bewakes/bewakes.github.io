---
title: Deriving Poisson Equation
date: May 21, 2017
tags:
    - math
---

Poisson distribution is defined as,

$$P(x; \lambda) = \frac{e^{-\lambda} \lambda^x}{x!}$$

Where,
- $P(x; \lambda)$ is the probability that an event occurs $x$ times in the given interval,
- $\lambda$ is the expected rate/probability of an event occurring.

In Binomial distribution, probability that one of the two events ($p$ and $q$) occurs $x$ times out of $n$ trials is,

$$P(X = x) = \binom{n}{x} p^x q^{n-x}$$

where $q = 1 - p$. Now, if $\lambda$ is the expected number of successes then, $p = \lambda/n$.

Substituting value of $p$ in (1), we obtain

$$P(X = x) = \binom{n}{x} \frac{\lambda^x}{n^x} (1 - \frac{\lambda}{n})^{n-x}$$

Expanding $\binom{n}{x}$,

$$P(X = x) = \frac{n \cdot (n-1) \cdots (n-x+1) \lambda^x}{x!} \cdot \frac{1}{n^x} (1 - \frac{\lambda}{n})^n (1 - \frac{\lambda}{n})^{-x}$$

As $n \to \infty$, it's obvious that $(1 - \lambda/n) \to 1$ and by definition, $(1 - \lambda/n)^n = e^{-\lambda}$. So,

$$P(X = x) = \frac{n \cdot (n-1) \cdots (n-x+1) \lambda^x}{n^x} \cdot \frac{1}{x!} e^{-\lambda}$$

$$= \frac{n}{n} \cdot \frac{n-1}{n} \cdots \frac{n-x+1}{n} \cdot \frac{\lambda^x}{x!} e^{-\lambda}$$

Thus, as $n \to \infty$ we obtain,

$$P(X = x) = \frac{\lambda^x e^{-\lambda}}{x!}$$

And hence, our Poisson equation.
