The theoretical derivation process presented here is a continuation and supplementary explanation of Section 4-Illustrative Example in the article.



For the first functional scenario:

$$
T_1 := x \leq 0, \, D_1 := n = 0
$$

Let's take $$x = -10$$ as an example:

The actual execution path of the program is:

$$
sum = 0; \\

n = 0; \\
\neg(sum < x)
$$

The derivation process of Hoare logic is as follows:

$$
\{n = 0\} \\
\neg(sum < x) \\
\{n = 0 \land \neg(sum < x)\} \\
n = 0 \\
\{0 = 0 \land \neg(sum < x)\} \\
sum = 0 \\
\{0 = 0 \land \neg(0 < x)\}
$$

$$
T \land Ct \Rightarrow D' := x \leq 0 \land !(0 < x) \Rightarrow (0 = 0)
$$

That is to prove

$$
x \leq 0 \land !(0 < x) \Rightarrow (0 = 0)
$$

is a tautology, which is obviously true.
