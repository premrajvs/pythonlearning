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

Now that I learnt how to read elements, next is Precision Sum

Precision sum magic formula
Sum(i,j) = sum(j) - sum(i-1) or sum(j) - 0 if i = 0
[10 20 30]
sum(0) = 10
sum(0,1) = sum(0) + sum(1) = 30
sum(0,2) = sum(0) + sum(1) + sum(2) = 60
as per formula, sum(0,2) = sum(2) = 60 sum(1,2) = sum(2) - sum(0) = 60 - 10 = 50
