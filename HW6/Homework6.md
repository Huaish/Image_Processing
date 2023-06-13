# Homework No.6

Student ID: 41047902S Name: 鄭淮薰

## Problem Statement

Show that the Fourier transforms of

(a) $f(ax)$ is $\frac{1}{a}F(\frac{u}{a})$, where $a$ us any nonzero real number

(b) $f(x-x_0)$ is $F(u)exp(-j2 \pi ux_0)$

## Answer

### (a)

1. (=>) ：Let $t=ax$, $dt=adx$ => $dx=\frac{1}{a}dt$
   
   $$
   \begin{align*}
&\frac{1}{2\pi}\int^{\infty}_{-\infty}f(ax)exp(-jux)dx \\
&=\frac{1}{2\pi}\int^{\infty}_{-\infty}f(t)exp(-ju \frac{t}{a})\ \frac{1}{a}dt \\
&= \frac{1}{a} \ F(\frac{u}{a})
\end{align*}
   $$

2. (<=) ：Let $t = \frac{u}{a}$, $dt=\frac{1}{a} \ du$  => $du=adt$
   
   $$
   \begin{align*}
&\int^{\infty}_{-\infty} 
\frac{1}{a} \ F(\frac{u}{a}) \ exp(jux) \ du \\
&=\int^{\infty}_{-\infty} 
\frac{1}{a} \ F(t) \ exp(j \ at \ x) \ a \ dt \\
&= \int^{\infty}_{-\infty} 
\frac{1}{a} \ F(t) \ exp(jt \ ax) \ a \ dt \\
&= \int^{\infty}_{-\infty} \ F(t) \ exp(jt \ ax) \ dt \\
&= f(ax)
\end{align*}
   $$

### (b)

1. (=>)：Let $t=x-x_0$, $dt=dx$
   
   $$
   \begin{align*}
&\int^{\infty}_{-\infty}f(x-x_0)exp(-j 2\pi ux)dx \\
&=\int^{\infty}_{-\infty}f(t)exp(-j 2\pi u (t+x_0))dt \\
&=\int^{\infty}_{-\infty}f(t)exp((-j 2\pi ut) + (-j 2\pi u x_0))dt \\
&=\int^{\infty}_{-\infty}f(t)exp(-j 2\pi ut)exp (-j 2\pi u x_0)dt \\
&=F(u) \ exp (-j 2\pi u x_0)
\end{align*}
   $$

2. (<=)
   
   $$
   \begin{align*}
&\int^{\infty}_{-\infty}F(u)exp(-j 2\pi ux_0)exp(-j 2\pi ux)du \\
&\int^{\infty}_{-\infty}F(u)exp((-j 2\pi ux_0) + (-j 2\pi ux))du \\
&\int^{\infty}_{-\infty}F(u)exp(-j 2\pi u(x+x_0))du \\
&=f(x+x_0)
\end{align*}
   $$
