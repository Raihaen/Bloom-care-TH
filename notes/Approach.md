# Approach

In this file, I will be documenting my walkthrough of the problem.

I started by installing poetry and checking it out. Next I had to decide on an approach to start with, between trying a greedy algorithm (since it might be faster due to the small size of the data provided), but for i don't think that's what the OR aims to test, so I'll be proceeding with a good old CP appraoch...

Next step was documenting on how ORtools work and creating a first model (basic contstraints). We will then add more and more au fur et a mesure. 

We start by defining our objective function :
just put in constraints to satisfy.
What was really great (and made the task simpler than i first thought) were the -already defined- methods.

Now for optimization metrics, i want to prioritize reasoning that holds irl than treating this as a game and trying to get the highest scores while compremizing the reasoning.
We can just optimize for the metrics that are given but i think in termes of Some ideas on what to minimize. 
Since time complexity is a big issue irl, i wanted to maximize / minimize metrics that are slightly more accurate but still could give us a good score : 

I'm not very familiar with how variables work in 

## Running :

we start by adding ortools : 
`poetry add ortools`

this should be enough.