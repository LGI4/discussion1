# Discussion 1: Git and HOF
## Git Basics
[Git Practice Repo](https://github.com/CliffBakalian/git-basics)

## HOF

What are they?
- Basically use functions as parameters for other functions
- Able to assign functions to variables

What's the point?
- More concise code
- Cleaner code
- Abstraction

### HOF and Lambda Practice

`is_present(lst,x)`
- Returns a list of the same length as `lst` which has a `1` at each position in which the corresponding position in `lst` is equal to `x`, and a `0` otherwise.
- Examples:
  + `is_present([1,2,3],1) == [1,0,0]`
  + `is_present([1,2,1],1) == [1,0,1]`

`count_occ(lst,target)`
- Returns how many elements in `lst` are equal to `target`
- Examples:
  + `count_occ([1,2,3],1) == 1`
  + `count_occ([1,1,1],1) == 3`

`uniq(lst)`
-    Given a list, returns a list with all duplicate elements removed. Order does not matter.
- Examples:
  + `uniq([1,2,1,2]) == [1,2]`
  + `uniq([4,3,2,1]) == [4,3,2,1]`

`find_max(matrix)`
- given a list of lists find the maximum. You may assume the inputs are non-negative ints.
- Examples:
  + `find_max([[1,2],[3,4],[5,6]]) == 6`
  + `find_max([[1,1],[1],[1]]) == 1`

`count_ones(matrix)`
- given a matrix count how many 1s are in the matrix
- Examples:
  + `count_ones([[1,1],[1],[1]]) == 4`
  + `count_ones([[],[3],[0]]) == 0`

`addgenerator(x)`
- return a lambda function that adds x to its parameter
- Examples:
  + `addgenerator(4)(5) == 9`
  + `addgenerator(1)(5) == 6`

`apply_to_self()`
- return a lambda function that takes in 2 parameters. The first is an element and the second is a function. The body of the lambda function should add the element to the application of the function to the element. You may assume that the elementis an int
- Examples:
  + `apply_to_self()(2,lambda x: x + 1) == 5 #2 + (2 + 1)`
  + `apply_to_self()(4,lambda x: -x) == 0 #4 + (-4)`

`ap(fns,args)`
- Applies each function in `fns` to each argument in `args` in order, collecting all results in a single list.
- Examples:
  + `ap([lambda x: x + 1, lambda x: -x],[1,2,3]) == [2,3,4,-1,-2,-3]`
  + `ap([lambda x: x - 1, lambda x: 4],[1,2,3]) == [0,1,2,4,4,4]`

`map2(matrix,f)`
- write a function that is similar to `map` but works on lists of lists
- Examples:
  + `map2([[1,2,3],[4,5,6]],lambda x: -x) == [[-1,-2,-3],[-4,-5,-6]]`
  + `map2([[1,2,3],[4,5,6]],lambda x: 0) == [[0,0,0],[0,0,0]]`

## Testing

You should be able to run `pytest` and `pytest` will figure the rest out
