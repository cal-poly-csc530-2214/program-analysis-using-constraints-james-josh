# program-analysis-using-constraints-james-josh

### Initial Reading
Initially, we both spent time reading the paper, discussing it, and
performing further research with other online sources to clarify
any confusion. We then downloaded Z3 and read the tutorials that
were linked in its README.

### Project
The goal of our project was to create a Python program that takes in
other Python functions as input, parses them, and translates their
statements into constraints that Z3 can check for satisfiability.

We began by reading an input Python file. We then searched for a
function definition, and, upon finding one, we read through it
and parsed all of its integer variables.

We spent time thinking about and discussing it, but we never got 
around to generating any constraints. It is a difficult task, and,
although we did not complete it, we learned while just grappling
with the problem.

It was very interesting to learn how simple programs can be reduced
to satisfiability problems, which can then be efficiently solved.

### Example Input
```
from typing import *

def pv1( y: int ):
    x: int = -50
    while x < 0:
        x = x + y
        y += 1
    assert y > 0

pv1(-324)
```


### Example Output
```
variables: ['y', 'x']
2 vars
```
