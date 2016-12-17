---
layout: post
title:  "Welcome to Jekyll!"
date:   2016-03-07 14:16:31 -0500
categories: jekyll update
---
705 HW1 Due Sept 1. 3pm 

C1: 3,8,13
C2: 1,4,7,20
C3: 8,22,33

# Q1.3
Let $\Omega$ be a sample space and let $A_1, A_2, \cdots ,$ be events.
Define $B_n=\bigcup^\infty_{i=n}A_i$ and $C_n=\bigcap^\infty_{i=n}A_i$.

## 1.3.a
Show that $B_1\supset B_2\supset\cdots$ and that $C_1\subset C_2\subset\cdots$. 
###### 1.3.a.1
To prove $B_1\supset B_2\supset\cdots$, we need to prove $B_n\supset B_{n+1}$, $\forall n>0, n\in N$. 
$$B_n=\bigcup^\infty_{i=n}A_i=A_n\cup(\bigcup^\infty_{i=n+1}A_i)=A_n\cup B_{n+1}$$
For any $\omega\in B_{n+1}$, $\omega\in B_n$ by the defination of union. Thus, $B_n\supset B_{n+1}$, and $B_1\supset B_2\supset\cdots$. 
###### 1.3.a.2
To prove $C_1\subset C_2\subset\cdots$, we need to prove $C_n\subset C_{n+1}$, $\forall n>0, n\in N$. 
$$C_n=\bigcap^\infty_{i=n}A_i=A_n\cap(\bigcap^\infty_{i=n+1}A_i)=A_n\cap C_{n+1}$$
For any $\omega\in C_n$, $\omega\in C_{n+1}$ by the defination of intersection. Thus, $C_n\subset C_{n+1}$, and $C_1\subset C_2\subset\cdots$.

## 1.3.b
Show that $\omega\in\bigcap^\infty_{i=n}B_n$ if and only if $\omega$ belongs to an infinite number of the events $A_1, A_2, \cdots$. 
###### 1.3.b.1
To prove $\omega\in\bigcap^\infty_{i=n}B_n\Rightarrow(\omega$ belongs to an infinite number of the events $A_1, A_2, \cdots)$, df
###### 1.3.b.2
## 1.3.c
Show that $\omega\in\bigcup^\infty_{i=n}C_n$ if and only if $\omega$ belongs to an infinite number of the events $A_1, A_2, \cdots$. 

# Q1.8
Suppose that $P(A_i)=1$ for each $i$, prove that $$P(\bigcap_{i=1}^\infty A_i)=1$$
Proof: 
\begin{aligned}
&P(A_i)=1\\
\Rightarrow&P(A_i^c)=0\\
\Rightarrow&P(\bigcup_{i=1}^\infty A_i^c)=0
\end{aligned}
# Q1.13
Suppose a fair coin is tossed repeatedly until both a head and a tail has appeared at least once. 
## 1.13.a
Describe the sample space $\Omega$

## 1.13.b
What is the probability that three tosses will be required? 
