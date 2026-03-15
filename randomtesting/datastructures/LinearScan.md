# Linear Scan - o(n) - Comparing 2 numbers

    When comparing 2 numbers there is a technique called pairwise comparison or Tournament technique. In my previous technique, I am comparing each number 2 times so it becomes o(2n).

    Step 1 - Idea is instead of comparing 1 number to both min and max. You compare a pair all the time. To make a pair, i should check if it is even or odd. If even, i should start with pair. If total count is odd, i will take only 1 for the first time. so, going forward it will be pairs. set starting index value accordingly for the loop.

    Step 2 - now each time, i compare current value and next value. The result i compare with previous min and max. So now i hop 2 elements at a time making it faster.

    When input numbers are not sorted, you have to visit every element atleast once. You cannot avoid that but this way, you visit 2 elements each time.

# Linear Scan - o(n) - 121. Best Time to Buy and Sell Stock

It is faster to iterate over elements than doing it by index
for price in prices is faster than for i in range(len(prices))

# Linear Scan - o(n) - 217. Contains Duplicate

Check if somthing exist - requires o(1) complexity. So, Hashset is the fastest
mymap = set() -- To initialize a set
mymap.add(var) -- To add a value
if var in mymap -- To check if value exist

# Linear Scan - o(n) - 169. Majority Element

Use hashmap because it is faster to update the value of an element by key and to retrieve the final value by key

# Linear Scan - o(n) - 724. Find Pivot Index

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

Technique is to keep subtracting the sum on left side at each position and the number at current position from total sum and checking if it is equal to left sum

# Linear Scan - o(n) - 189. Rotate Array

To rotate an array you should use queue. Because queue has an o(1) to pop an element from tail and to append an element from the head side.

Second point to remember - if an array has 5 elements. if you want to rotate by 5. do 5%5 times which is 0. Because rotating it 5 times will bring it back to same position. So, if the number is 100, do 100%5 = 0 times. this makes it faster

# Linear Scan - o(n) - 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
Best to use hashmap because it is faster to check if exist and also have key/value. If only check is needed, set is best
val_to_index = {}
if requirednumber in val_to_index:
return [i,val_to_index[requirednumber]]
val_to_index[num] = i

# ########## Milestone 1

Learning Summary

1. Always try to do something is o(n) or at max o(2n) or o(3n).. never o(n2). It becomes order of n2 only when for every element you go through every element
2. Use set when you want to check ifsomething exist. But remember set only can have distinct values and it is not guaranteed to maintain position when inserting because it may discard duplicate elements
3. Use hash map when you want to look up but for both key and value scenarios

Now that I learnt how to read elements, next is Precision Sum or Prefix Sum

Precision sum magic formula
Sum(i,j) = sum(j) - sum(i-1) or sum(j) - 0 if i = 0
[10 20 30]
sum(0) = 10
sum(0,1) = sum(0) + sum(1) = 30
sum(0,2) = sum(0) + sum(1) + sum(2) = 60
as per formula, sum(0,2) = sum(2) = 60 sum(1,2) = sum(2) - sum(0) = 60 - 10 = 50

###### TRICK - SLIDING WINDOW ONLY WORKS WHEN ALL NUMBERS ARE POSITIVE

### Prefix Sum

Using the formula learned above for precision sum, you know that
sum(1,2) at 2nd position = sum(2) - sum(0)
= total sum at position 2 - total sum at position 0

Therefore,
total sum at position 0 = total sum at position 2 - sum of a range of numbers

When you are asked to find a range of numbers that sums to a value.

Total sum at position 0 if equal to total sum at current position - target value, that implies this sub array is what we are looking for

### IMPORTANT LESSON ABOUT SLIDING WINDOW AND PREFIX SUM

To solve these problems, in a paper first solve manually. Then find which is the smallest window.
Reason is smallest window is only easy and feasible to calculate. Wherever the smallest window is present, you should start the loop from that side. This is the key.

### Next Learning plan is Difference Array

Main difference between prefix and diff array is
Prefix sum = find sum of all elements in a range
Diff array = Add or subtract to all elements in range a fixed number

Difference array is not useful on its own. It is combined with prefix sum.

Take an example - Car pooling. Passengers are traveling from from to to kilometer. Car has limited capacity.
If anytime for any kilometer range if the number of passengers are more than capacity they cannot travel.

Without differnece array, I should loop through each list from and to and in a list for each location add or subtract.
With difference array, FIRST QUESTION TO ASK - Is the range inclusive at from and to ?
Flight Booking Problem - Add seats to every flight from first to last. Keyword - INCLUDING last.
[first, last] ← inclusive
[1, 2, 10]
If array is 0-based: Flight 1 → index 0 Flight 2 → index 1
So range is: index 0 to index 1 (inclusive)
diff[L] += val
diff[R + 1] -= val
Why R+1? = Because we want effect to stop AFTER R. So for booking [1,2,10]:
diff[0] += 10 diff[2] -= 10 Because index 2 is first place we DON’T want 10.

Car Pooling Problem = [passengers, from, to] Pick up at from and Drop off at to.
Passengers are in car from: They are inside at from and They are NOT inside at to. So from inclusive. To not inclusive.
so range is [from, to-1]
[2, 1, 5] = Passengers are inside at 1, 2, 3, 4. so
For half-open range [L, R): diff[L] += val and diff[R] -= val

THIS IS HOW YOU DETERMINE HOW THE index range should be.

###### LEARNING SUMMARY

We already covered:
Scanning (linear scan)
Aggregation (prefix / diff)
Now moving from aggregation over ranges to controlled scanning over ranges.

Prefix Sum: “I precompute totals so I don’t recalculate”
Difference Array: “I mark boundaries and aggregate later”
Two Pointers: “I maintain a valid window and adjust it smartly”

##### Two Pointers

Think “Two Pointers” when you see:
Sorted array
Subarray / window
Pairs
Condition-based shrinking or expanding
“Find if / find count / find max-min under constraint”

Anytime you need 3 points to get an answer. Remember to keep the one point constant. So, other 2 pointers become left and right.
Think of 2 pointers as one starting point 0 and one from the end length-1. and slowly move inwards on condition.

#### Variable Sliding Window

Window is nothing but left and right pointer. When to use window vs left right pointer. when you want continuous something, use window.
Trick to remember, if you want something some data structure to store the position of something and retrieve in o(1) use hashmap dictionary.

### Common Mistakes

In Python you use self in a function only when the function is declared inside a class because self makes it a instance method.
if outside a class, it is just another variable.

Second mistake with function, if a function is inside a class, it is mandatory to have a variable called self as first arg.

When you want to call a class, you do not need new operator. In python calling a class is same as calling a function.
Second, when you just say fi=findminmax, you are not creating a new object. you are renaming the class findminmax. like changing the name of the blueprint. Instead you should use () next to class name. now it creates object

In Java you can have multiple classes and functions and then declare void main function in on class and it automatically becomes the entry point. But python runs top down. So, it does not work that way. When you import the python class in another class in a big project, you dont have to worry about what gets called when because code logic takes care of that. But if you want to run a file directly, use **name** == "**main**". Python knows to run this automatically.

In python if i want to search if something exist, fastest data structure is Hashmap but if you do not want values, faster is set because it does not store any values.

It is very important to understand how Stack and Queue works so you can use it in different scenarios. For example, in min stack requirement I am using stack.

Understanding summary.

List [1, 2, 3] = List in Python always follows stack

Step Action List State [Head ... Tail] Head Value Tail Value
1 Push 1 [1] 1 1
2 Push 2 [1, 2] 1 2
3 Push 3 [1, 2, 3] 1 3
4 Push 4 [1, 2, 3, 4] 1 4
5 Push 5 [1, 2, 3, 4, 5] 1 5

Always first element is Head = 1
Always last element is Tail = 3
Always push and pop both interacts with Tail that is 3
Always when i append, it moves Tail to new element

Now For Queue - default data structure is collections dequeue
Step Action Deque State [Head ... Tail] Head Tail
1 Enqueue 1 [1] 1 1
2 Enqueue 2 [1, 2] 1 2
3 Enqueue 3 [1, 2, 3] 1 3
4 Enqueue 4 [1, 2, 3, 4] 1 4
5 Enqueue 5 [1, 2, 3, 4, 5] 1 5

Always first element is Head = 1
Always last element is Tail = 3
**DIFFERENCE ** Push interacts with Tail and Pop interacts with Head
.pop() is to remove the tail element and see the tail element
.appendleft(value) is to add an element to head
Always when i append, it moves Tail to new element

When you want to rotate an array, always use % operator target%length so it becomes faster. If an array has 5 elements and if you want to rotate 5 times. 5%5=0 - no rotation needed. if rotation target is 6, 6%5=1 so you just rotate once. it is same effect.

Remove range(len()): Iterating directly over the list (for price in prices) is faster than indexing (prices[i]) because it avoids repeated getitem calls.
for p in prices: better than for price in range(len(prices))

# Monotonic Stack

you will use a stack to store numbers in an order - increasing or decreasing based on the problem you want to solve
So instead of going o(n square), you go o(2n)
But remember you need a hash map to store key value to support your implementation
