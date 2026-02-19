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
