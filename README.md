# nth Prime

A program that calculates the n<sup>th</sup> prime number. 

## Context 

A friend of mine showed me a challenge problem he found on a whiteboard at his university.

> Find the 1,000,000,000<sup>th</sup> prime. Gold star for under a minute.

Spoiler alert: I didn't get the gold star. In fact, I'm not sure how it'd be possible.

For a more reasonable goal, I wanted to write something faster than the naive implementation that runs in O(n^(5/2)) time. After doing a bit of research, I found something that would work for me, namely, the Sieve of Eratosthenes. However, if I were to use the Sieve of Eratosthenes for large n, the space complexity would be far too large. To counter this, I learned about segmented sieves, and implemented a segmented sieve instead. In addition, since I was only calculating the nth prime, I did not need to calculate every prime as any primes greater than the sqrt(nth prime) were not needed. Of course, without knowing what the nth prime is, I can't calculate the exact limit, but I could find a rough estimate.

Through this little side project, I also discovered that all primes are of the form `6x - 1` or `6x + 1`. Given a number `P`, if `P % 6 = 0`, then it is divisible by 6. If `P % 6 = 2`, then it is divisible by two since 6 is divisible by 2. If `P % 6 = 3`, then it is divisible by 3 since 6 is divisible by 3. If `P % 6 = 4`, then it is divisible by 2. That leaves two remaining options, `P % 6 = 1` or `5`. So in other words, all prime numbers are of the form `6x - 1` or `6x + 1`.

Calculating the 1,000,000th prime using naive method:

`10 min 24 seconds`


Calculating the 1,000,000th prime using sieve:

`17.6 seconds`


## How to Run
Simply run `python primes.py`.
