# given a linked list with each node having data a single character, check whether it is palindrome
# [2]->[3]->[3]->[2],  [1]->[2]->[1] are valid palindromes.
# [2]->[3]->[4]->[2],  [1]->[a]->[2]->[1] are not.


class node():
    def __init__(self, data):
        self.data = data
        self.next = None

# method1 using stack
# Time Complexity = O(n)
# Extra Space = O(n)
def using_stack( head ):
    ans = "NO"
    if head is None:
        return ans
    stack = []
    temp = head
    while temp is not None:
        stack.append(temp)
        temp = temp.next
    temp = head
    # at any point if stack_top and temp does not match, it means it is not palindrome.
    while temp is not None:
        stack_top = stack.pop()
        if temp.data != stack_top.data:
            return ans
        temp = temp.next
    ans = "YES"
    return ans

# number of linked list nodes
num_nodes = int(input("\nenter number of nodes:"))
# head of Linked List
head = None
# temprory variable just to trace last element of linked list while populating data
temp = None
for i in range( num_nodes ):
    data = int(input("\nenter node data:"))
    # if this is first linked list node
    if head is None:
        head = node(data)
        # point next node to head, initially None
        temp = head
        continue
    temp.next = node(data)
    temp = temp.next

print( "\n", using_stack(head) )

