function factorial (n : int): int
    decreases n;
    requires n >= 0;
{
    if n == 0 then 1 else n * factorial(n - 1)
}

method computeFactorial(n: int) returns (f: int)
    requires n >= 0
    ensures f == factorial(n)
{
    var i := 0;
    
    if n == 0 { f := 1; }
    else 
    {
        f := n;
        while i < n - 1 
            decreases n - 1 - i
            invariant 0 <= i <= n - 1;
            invariant f * factorial(n - i - 1) == factorial(n)
        {
            i := i + 1;
            f := f * (n - i);
        }
    }
}