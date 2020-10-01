## 1. How to find the `middle element` of a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. When `p` reaches the end of the linked list. `q` will be in the middle of the list.

## 2. How to find the `loop` or `cycle` in a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. For every second iteration of `p`, iterate `q`. If `p` and `q` are pointing to the same node, there is a loop or cycle present.

## 3. How to find the `k th` element from the end of a linked list in one pass ?
Solution: Start with two pointer `p` and `q`. When the `p` pointer reahces upto the `k th` element, increment `q`.When `p` reaches the end of the list. `q` is ponting to the element 'k th' from the end.

## 4. List some real world applications of linked list ?
Solution:

*Image viewer* – Previous and next images are linked, hence can be accessed by next and previous button.

*Previous and next page in web browser* – We can access previous and next url searched in web browser by pressing back and next button since, they are linked as linked list.

*Music Player* – Songs in music player are linked to previous and next song. you can play songs either from starting or ending of the list.

## 5. What is a data structure ?

Solution: Data structure refers to the way data is organized and manipulated. It seeks to find ways to make data access more efficient. When dealing with the data structure, we not only focus on one piece of data but the different set of data and how they can relate to one another in an organized manner.

## 6. Explain the `LIFO` scheme.

Solution: LIFO is a short form of Last In First Out. It refers how data is accessed, stored and retrieved. Using this scheme, data that was stored last should be the one to be extracted first. This also means that in order to gain access to the first data, all the other data that was stored before this first data must first be retrieved and extracted.

## 7. What is merge sort ?

Solution: Merge sort, is a  divide-and-conquer approach for sorting the data. In a sequence of data, adjacent ones are merged and sorted to create bigger sorted lists. These sorted lists are then merged again to form an even bigger sorted list, which continues until you have one single sorted list.

## 8. What are the minimum number of queues to implement a prioriy queue ?

Solution: The minimum number of queues needed in this case is two. One queue is intended for sorting priorities while the other queue is used for actual storage of data.

## 9. Which sorting algorithm is the fastest

Solution: There are many types of sorting algorithms: quick sort, bubble sort, balloon sort, radix sort, merge sort, etc. Not one can be considered the fastest because each algorithm is designed for a particular data structure and data set. It would depend on the data set that you would want to sort.

## Some common algorithm problems asked at online tests :

#### 10. Save all leaf nodes of a Binary tree in a Doubly Linked List by using Right node as Next node and Left Node as Previous Node.

#### 11. Given an array,find the maximum j – i such that arr[j] > arr[i]

#### 12. Remove Alternate Duplicate characters from a char array you have to do it in Place.Like keeping only the odd occurences of each character.
`Example: Input: “you got beautiful eyes”
Output: ”you gtbeaiful es”`
Allowed Time Complexity was O(n) and Space Complexity was O(1)

#### 13. In a file there are 1 million words . Find 10 most frequent words in that file.

#### 14. Find all nodes at k-distance from a given node in a binary tree

##### 15. Clone a linked list with next and random pointer

#### 16. Serialise and Deserialise a linked list with next and random pointer.

#### 17. Construct a binary tree from given inorder and preorder traversals.

#### 18. Return a tree such that each internal node stores sum of all its child nodes. Each leaf node stores zero.

#### 19. How will you implement linked list with 1 million nodes? How will you access 999999 th node? Give some optimal design strategy and implementation.

#### 20. Reversal of Linked List in groups of K.

#### 21. Given a positive integer N, count all possible distinct binary strings of length N such that there are no consecutive 1’s.

#### 22. Check whether given binary tree is balanced or not. Definition was no two leaves should have height difference of greater than one.

#### 23. Remove duplicates from string in place in O(n).

#### 24. Connect nodes on same level in a binary tree.

#### 25. Find sum of data of all leaves of a binary tree on same level and then multiply sums obtained of all levels.

#### 26. Given a matrix of characters and a word. You have to count the number of occurrences of that word in that matrix. you can move to any of the eight valid directions from current position.

#### 27. You are given an string as input which represents a path. You have to normalize that path inplace(NO EXTRA SPACE).
`e.g.input : "\a\b\c\..\..\file.txt" output: "\a\file.txt"`

#### 28. Least common ancestor of two nodes in a binary tree

#### 29. Given two sorted arrays (with repetitive elements) find the kth minimum number from both arrays.

#### 30. Given the root to a binary tree, a value n and k.Find the sum of nodes at distance k from node with value n

#### 31. Find an element in a rotated array. The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days.
`For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, 
the maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6. 
If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.`

#### 32. Given two linked lists both represent a number. Create a linked list that contains its sum.

#### 33. Given a binary search tree , print the path which has the sum equal to k and has minimum hops. i.e if there are multiple paths with the sum equal to k then print the path with minimum number of nodes.

#### 34. A MxN matrix containing integers (positive, negative and zero’s). For every position containing 0, mark the corresponding row and column as 0. Rotate MxN matrix by 90 degress.

#### 35. Find the nth number that contains the digit k or is divisible by k. (2 <= k <= 9)

#### 36. Write a program to connect next left node in a binary tree. Also first node of each level should be pointing to last node of next level? (Without using Queue)

#### 37. Convert a binary tree to its sum tree(each node is the sum of its children)

#### 38. Given a directed graph. Construct another graph from given graph such that if path exists from vertices A to vertices B and from B to C, then path from A to C and from C to A also should exists.

#### 39. Implement hashmap on your own. Write good hashing function for string.

#### 40. Given an array, arrange the elements such that the number formed by concatenating the elements is highest.
`E.g.: input = [9, 93, 24, 6], 
the output should be: [9,93,6,24].
 This is because if you concatenate all the numbers, 
993624 is the highest number that can be formed.`

#### 41. Given a string, find the longest substring which is palindrome.

#### 42. Given that integers are read from a data stream. Find median of elements read so for in efficient way. For simplicity assume there are no duplicates.

#### 43. Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.

#### 44. Given unsorted array and a number K. Find 2 numbers such that sum is K.

#### 45. Given n-ary tree. zigzag level order traversal.

#### 46. Given string s and string t find whether all permutation of t is present as substring in s.

#### 47. Design a stack which holds an integer value such that getMinimum() function should return the minimum element in the stack. Implement popMin() function which would pop minimum element from the original stack.

#### 48. Given a set of intervals like 5-10, 15-20, 25-40, 30-45, 50-100. Find the ith smallest number in these intervals. Assume there are no duplicate numbers.
`e.g:  1st smallest number = 5	  6th smallest number = 10	
7th smallest number = 15 and so on.`

#### 49. Given an array which is first strictly increasing and then strictly decreasing. Find an element in this array.

#### 50. Given a string example : shoppingwithflipkartiseasy, Now we are given this string and a dictionary containing valid words , now we need to break the sentence into words separated by space. Output : shopping with flipkart is easy

#### 51. Given a series 2,3,4,5,6,8,9,10,……, here in this series all the numbers are present which have factors only and only either 2,3 or 5. Need to write a node to generate nth number for the series . With best approach and complexity

#### 52. Given a tree with edge weights, find any path in the tree with maximum sum of edges.

#### 53. Merge k sorted arrays.

#### 54. Given a maze, a start point and end point find the shortest path to reach the end point from the starting point.

#### 55. Given a sentence and a set of characters. Find the minimum window within which the set of characters can be found in the sentence in any order.

#### 56. You are given a string of 0’s and 1’s you have to find the number of substrings in the string which starts and end with a 1.
`eg : input : 0010110010 output : 6`

#### 57. You are given a mapping like a -> 1, b-> 2… z-> 26. You have to print all possible combinations of a given number using the above information.
`eg : input : 121 output : aba,la,au`

#### 58. Given a dictionary of 50,000 words. Given a phrase without spaces, add spaces to make it a proper sentence.
`e.g:input:  thequickbrownfoxjumpoverlazydog	
output: the quick brown fox jump over lazy dog`

#### 59. Given an unsorted array of n integers which can contain integers from 1 to n. Some elements can be repeated multiple times and some other elements can be absent from the array. Count frequency of all elements that are present and print the missing elements.
`Examples:Input: arr[] = {2, 3, 3, 2, 5} 
Output: Below are frequencies of all elements 
1 -> 0        2 -> 2        3 -> 2        4 -> 0        5 -> 1`

#### 60. Get the next bigger number using the same digits of a number.
`Eg, For 123456, next number would be 123465`

#### 61. Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands
`Input : mat[][] = 
{{1, 1, 0, 0, 0},
 {0, 1, 0, 0, 1}, 
  {1, 0, 0, 1, 1},
  {0, 0, 0, 0, 0}, 
 {1, 0, 1, 0, 1}}
Output : 5`

#### 62. Given two strings in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find minimum number of characters to be deleted to make both the strings anagram?
If two strings contains same data set in any order then strings are called Anagrams.

``Examples:
 
Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.
 
Input : str1 = "cddgk" str2 = "gcd"
Output: 2
 
Input : str1 = "bca" str2 = "acb"
Output: 0``

#### 63. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Examples:
 
``Input: arr[]   = {2, 0, 2}
Output: 2
Structure is like below
| |
|_|
We can trap 2 units of water in the middle gap.
 
Input: arr[]   = {3, 0, 0, 2, 0, 4}
Output: 10
Structure is like below
     |
|    |
|  | |
|__|_| 
We can trap "3*2 units" of water between 3 an 2,
"1 unit" on top of bar 2 and "3 units" between 2 
and 4.  See below diagram also.
 
Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
       | 
   |   || |
_|_||_||||||
Trap "1 unit" between first 1 and 2, "4 units" between
first 2 and 3 and "1 unit" between second last 1 and last 2``

#### 64. Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.
Insert

Remove

Replace

All of the above operations are of equal cost.

``Examples:
 
Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.
 
Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.
 
Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a``

#### 65. Given a string with repeated characters, task is rearrange characters in a string so that no two adjacent characters are same.
Note : It may be assumed that the string has only lowercase English alphabets.

``Examples:
 
Input: aaabc 
Output: abaca 
 
Input: aaabb
Output: ababa 
 
Input: aa 
Output: Not Possible
 
Input: aaaabc 
Output: Not Possible``

#### 66. This problem is know as Clock angle problem where we need to find angle between hands of an analog clock at a given time.
`Examples:Input:  h = 12:00, m = 30.00
Output: 165 degreeInput:  h = 3.00, m = 30.00 Output: 75 degree`
————————————————————————————————
