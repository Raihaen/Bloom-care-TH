# Approach

In this file, I will be documenting my walkthrough of the problem.

I started by installing poetry and checking it out. Next I had to decide on an approach to start with, between trying a greedy algorithm (since it might be faster due to the small size of the data provided), but for i don't think that's what the OR aims to test, so I'll be proceeding with a good old CP approach...

Next step was documenting on how ORtools work and creating a first model (basic constraints). We will then add more and more au fur et à mesure. 

We start by defining our objective function and just put in constraints to satisfy.
What was really fairly simple (what made the task simpler than i first thought) were the already defined methods.

Now for optimization metrics, i want to prioritize reasoning that holds IRL than treating this as a game and trying to get the highest scores while compromizing the reasoning.
We can just optimize for the metrics that are given but i think this might end up costing time complexity IRL. And so, i wanted to maximize / minimize metrics that are related, faster to calculate but still could give us a good score : 
- Instead of checking for $\texttt{average}(\frac{\texttt{unique}(\texttt{caretakers})}{\texttt{n visits}})$ or $\texttt{average}(\frac{\texttt{unique}(\texttt{caretakers})}{\texttt{n visits}})$, I instead opted for $\texttt{max(n caretakers)}$ as it would be faster. Implementing this made the continuity score rise from 0.50ish into 0.66, the thing is, I tried to check and every client only has one caretaker, i wanted to check the code for the `evaluator.py` file but ran out of time for the task. 
- I wanted to implement the same approach for the second criterion : Travel efficiency, with a $\texttt{max(}\Sigma$ of zone switches over the whole period $\texttt{)}$ - instead of an average daily sum or a max daily sum. My thinking process here was that when some client uses the logiciel, he wouldn't directly schedule a whole month but rather schedule on a weekly basis (I might be wrong tho), and so, it could still enough of a constraint, plus the fact that minimizing the sum means compensating : you might have a full day here, but a very lean day later in the week. This is not perfect in real life tho, due to traffic, train schedules etc... 

One last point I wanted to discuss : In case of using `AddAtMostOne` instead of using `AddExactlyOne` vu the fact that there might be no solution / we want the model to exit with at least some solution. In this case, we will need to have a weighted sum of all that we need to maximize (a metric for the count of assigned visits (percentage for ex) + 2 metrics for score (each out of 1 too)), my approach here would be to use a weight $<$ $\frac{1}{2} (\texttt{nb tasks})^{-1}$ for the sum of the 2 score metrics (my rationale is that I rather have one more visit assigned than peak allocation with less assignments). 

I'm not very familiar with how variables work in `ORTools`, which burned some of my time and getting the syntax faster would have saved me some time.

## Running :

we start by adding ortools : 
`poetry add ortools`
this should be enough.
Since I uploaded the updated `poetry.lock` file, no need for this command anymore.