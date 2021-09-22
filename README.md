# Python (3.8.2)

## Algorithm

### Array

#### [imos(l, r, add, p=0)](https://github.com/1b0325h/ac-python/blob/main/library/imos.py)

An imos method can be implemented as the result of repeating the operation "add a certain number v to a certain continuous interval" K times in a 1-dimensional array of length N.

- [ABC127C - Prison](https://atcoder.jp/contests/abc127/tasks/abc127_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc127/submissions/26022371)
- [ABC183D - Water Heater](https://atcoder.jp/contests/abc183/tasks/abc183_d) [:heavy_check_mark:](https://atcoder.jp/contests/abc183/submissions/26024118)

### Searching

#### [binary_search(ok, ng, f)](https://github.com/1b0325h/ac-python/blob/main/library/binary_search.py)

A binary search is an algorithm to find a particular element in the list. Suppose we have a list of thousand elements, and we need to get an index position of a particular element. We can find the element's index position very fast using the binary search algorithm.

```python
>>> arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
>>> target = 64
>>> binary_search(-1, len(arr), lambda x: arr[x] >= target)
6
```

- [ABC146C - Buy an Integer](https://atcoder.jp/contests/abc146/tasks/abc146_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc146/submissions/26023532)
- [ABC192D - Base n](https://atcoder.jp/contests/abc192/tasks/abc192_d) [:heavy_check_mark:](https://atcoder.jp/contests/abc192/submissions/26024471)

## Math

### Number Theoretic Functions

#### [igcd(x, y)](https://github.com/1b0325h/ac-python/blob/main/library/igcd.py)

Computes nonnegative integer greatest common divisor.

```python
>>> igcd(8, 9)
1
>>> igcd(30, 12)
6
```

- [ABC162C - Sum of gcd of Tuples(Easy)](https://atcoder.jp/contests/abc162/tasks/abc162_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc162/submissions/26023783)
- [ARC105B - MAX-=min](https://atcoder.jp/contests/arc105/tasks/arc105_b) [:heavy_check_mark:](https://atcoder.jp/contests/arc105/submissions/26024666)

#### [ilcm(x, y)](https://github.com/1b0325h/ac-python/blob/main/library/ilcm.py)

Computes integer least common multiple.

```python
>>> ilcm(2, 3)
6
>>> ilcm(123, 456)
18696
```

- [ABC148C - Snack](https://atcoder.jp/contests/abc148/tasks/abc148_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc148/submissions/26023651)
- [ARC110A - Redundant Redundancy](https://atcoder.jp/contests/arc110/tasks/arc110_a) [:heavy_check_mark:](https://atcoder.jp/contests/arc110/submissions/26024772)

### Congruences

#### [crt(m, v)](https://github.com/1b0325h/ac-python/blob/main/library/crt.py)

Chinese Remainder Theorem.

```python
>>> crt([783, 278], [151, 57])
(31471, 217674)
>>> crt([12, 6, 17], [3, 4, 2])
(-1, 0)
```

- [ABC186E - Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e) [:heavy_check_mark:](https://atcoder.jp/contests/abc186/submissions/26024331)

### Prime Numbers

#### [primefactors(n)](https://github.com/1b0325h/ac-python/blob/main/library/primefactors.py)

Return a sorted list of n's prime factors.

```python
>>> primefactors(42)
[2, 3, 7]
>>> primefactors(72)
[2, 2, 2, 3, 3]
```

#### [isprime(n)](https://github.com/1b0325h/ac-python/blob/main/library/isprime.py)

Test if n is a prime number (True) or not (False).

```python
>>> isprime(1)
False
>>> isprime(73)
True
>>> isprime(-1)
False
```

- [ABC149C - Next Prime](https://atcoder.jp/contests/abc149/tasks/abc149_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc149/submissions/26023709)

### Divisors

#### [divisors(n)](https://github.com/1b0325h/ac-python/blob/main/library/divisors.py)

Return all divisors of n sorted from 1..n.

```python
>>> divisors(4)
[1, 2, 4]
>>> divisors(12)
[1, 2, 3, 4, 6, 12]
```

- [ABC057C - Digits in Multiplication](https://atcoder.jp/contests/abc057/tasks/abc057_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc057/submissions/26041456)
- [ABC106B - 105](https://atcoder.jp/contests/abc106/tasks/abc106_b) [:heavy_check_mark:](https://atcoder.jp/contests/abc106/submissions/26021854)
- [ABC180C - Cream puff](https://atcoder.jp/contests/abc180/tasks/abc180_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc180/submissions/26024009)

### Permutations

#### [rperm(p)](https://github.com/1b0325h/ac-python/blob/main/library/rperm.py)

An inverse permutation is a permutation in which each number and the number of the place which it occupies are exchanged.

```python
>>> rperm([2, 3, 1])
[3, 1, 2]
>>> rperm([5, 3, 2, 4, 1])
[5, 3, 2, 4, 1]
```

- [ABC217C - Inverse of Permutation](https://atcoder.jp/contests/abc217/tasks/abc217_c) [:heavy_check_mark:](https://atcoder.jp/contests/abc217/submissions/25646036)

### Radix Representation

#### [decimal(s, b)](https://github.com/1b0325h/ac-python/blob/main/library/decimal.py)

Converts a string representation of a number in a given base into a decimal number.

```python
>>> decimal("123", 8)
83
>>> decimal("1234", 10)
1234
```

- [ABC192D - Base n](https://atcoder.jp/contests/abc192/tasks/abc192_d) [:heavy_check_mark:](https://atcoder.jp/contests/abc192/submissions/26024471)

#### [base(n, b)](https://github.com/1b0325h/ac-python/blob/main/library/base.py)

Converts a number into a string representation with the given base (radix).

```python
>>> base(11, 2)
'1011'
>>> base(1010101, 10)
'1010101'
```

- [ABC156B - Digits](https://atcoder.jp/contests/abc156/tasks/abc156_b) [:heavy_check_mark:](https://atcoder.jp/contests/abc156/submissions/26037581)
