def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1


def scale(it, multiplier):
    """Yield elements of the iterable it scaled by a number multiplier.

    >>> m = scale([1, 5, 2], 5)
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"
    # for i in it:
    #    i = multiplier * i
    #    yield i  #虽然代码在这个地方停下来，但是外面还有next在提着他易懂
    yield from (i * multiplier for i in it) # [] 会当场算出所有结果，（）是空的，只有踢一脚才会算一个




def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"  #递归两个核心点：当前应该做什么，然后递归的终止条件，还有递归的步骤
    yield n 
 
    if n == 1 :
        return  #yield已经把值传出去了 ，所以return直接空着就可以
    elif n % 2  == 0:
        n = n // 2  #两个//是代表整数结果
        yield from hailstone (n)
    elif n % 2 != 0:
        n  = n *3 + 1
        yield from hailstone (n) #yield from 直接把这个值yield出来 
     
    
    

