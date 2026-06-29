from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    number = 0
    last = x % 10

    while x > 0 :
        
        number = x % 10
        if number > last :
            return False
        else:
            x = x // 10
            last = number

    return True
        
        









def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    
    last = None
    final = None
    number = None
    all_runs = [] #list后面还可以加入list
    curr_run = []
    
    
    while  n > 0:
        number = n % 10
        n = n // 10

        if last is None:
            last = number
            curr_run = [number]
        elif number >= last:
            last = number
            all_runs.append(curr_run[::-1]) 
            curr_run = [number]
            
      
        else:
            last = number
            curr_run.append(number)
       
    all_runs.append(curr_run[::-1])  #list[start:end:step] 步长为-1时表示从后往前取
    # print(all_runs) 适当的时候打印allrun查看值
    final = all_runs[k][0] #变成二维数组，用二维数组来取值 

    return final


def make_repeater(func, n): #这道题不是很理解
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"    
    def repeater(x):
        if n == 0 :
            return x
        else :
            return func(make_repeater(func,n-1)(x))
           
    return repeater



def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func,2)


def div_by_primes_under(n): #通过lambda不断地定义的新的循环，有点复杂 
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False #先定义第一个checker，无论如何第一个x都是false
    i = 2 
    while i <=  n:
        if not checker(i):
            checker = (lambda f ,i: lambda x : x % i == 0 or f(x))(checker,2 )
        i = i+1
    return checker

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f,i):
                def inner(x):
                    return x % i ==0 or f(x)
                return inner
            checker = outer(checker,i)
        i = i+ 1
    return checker
