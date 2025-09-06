def memoize(funs):
    cache = {}

    def wrapper(*args,**kwarges):
       key = (args,tuple(sorted(kwarges.items())))

       if key in cache:
          print(f"Fetching from cache for{args} {kwarges}")
          return cache[key]
       print(f"computing result for for{args}{kwarges}")

       result = funs(*args,**kwarges)
       cache[key] = result
       return result
    return wrapper

    
def fibonancci(n):
    if(n <= 1):
        return n
    return fibonancci(n-1) + fibonancci(n-2)
print(fibonancci(10))
print(fibonancci(15))