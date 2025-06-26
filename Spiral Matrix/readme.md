# Spiral Order

This was a pretty hard challenge. I created a method early on, but it took me a while to realize when to stop the loop.
let me explain:

The first thing I thought was "how many straight lines does this spiral have?"
After drawing some matrices I reached the formula for the number N of straight lines in a $m$ x $n$ matrix:\

```math
N_{m,n}=
\begin{cases}
  2m - 1, & \text{if } m \le n \\
  2n,     & \text{if } m > n
\end{cases}
```

I made a for loop that extends a list called `spiral` with elements from 4 different directions, each one corresponding to the outermost side of the matrix (like the sides of a square). After that I reduce the matrix to a smaller $m-2$ x $n-2$ matrix and repeat the process. The problem was in the stop condition. I know that the number of iterations should be `N//4 + 1`, but for some matrices the last iteration isn't a complete square! After struggling a lot I reached a simple solution! Instead of using a lot of if statements (it already has a lot of if statements in the code) I simply build the list with repeated values (for those whose last iteration is less than 4) and return a slice of the list with the correct size `m * n`, which excludes the excess values.

I wanted to write about this solution because it took me a while to reach it. I was thinking about it in a more mathematical way, with the sensation that something was missing. There are likely many smarter ways to do this, but I liked my solution! That's it