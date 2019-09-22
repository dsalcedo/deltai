# Run

[factorial.py](factorial.py)

`python3 factorial.py`

```bash
The factorial of 3 is 6

The factorial of 20 is 2432902008176640000
```

Ref + https://docs.python.org/3/library/timeit.html

Using "reduce + lambda" to calculate the result :muscle:!

```      
➜ deltai python -m timeit -s "reduce(lambda x, y: x * y, range(1, 100 + 1))" 
100000000 loops, best of 3: 0.00748 usec per loop
    
➜ deltai python -m timeit -s "reduce(lambda x, y: x * y, range(1, 1000 + 1))"
100000000 loops, best of 3: 0.00756 usec per loop
```

Using loops only generating range numbers D: !

```    
➜ ~ python -mtimeit -s'L=range(1000)' '[x+1 for x in L]'
10000 loops, best of 3: 33.3 usec per loop

➜ ~ python -mtimeit -s'L=range(100)' '[x+1 for x in L]' 
100000 loops, best of 3: 4.27 usec per loop
```

The differences in performance between these options (for, reduce + lambda ) is much more related to the algorithms each one is using, rather than any difference between list comprehensions and lambda.
