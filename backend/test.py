

class Solution:

    def __init__(self):
        pass

    def isValid(self, s):
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack

    @classmethod
    def remove_duplicates(self, arr):
        output = []
        for n in arr:
            for j in range(1, len(arr)):
                if arr[j] != n:
                    output.append(arr[j])
        print(output)

    # given an array and a result return true if the array have the numbers that returns the value

    # array = [1,2,3,6,7]
    # result = 9
    # output boolean
    @classmethod
    def two_sum(self, arr, result):
        # I can substract the result from each item of the array
        # store it, and then if that item exist return True
        stored = set()  # set is a list of unique elements, in an array you can have duplicates
        for a in arr:
            if a in stored:
                return True
            stored.add(result - a)
        return False


class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length = self.length + 1

    def pop(self):
        if self.length == 0:
            raise IndexError("Pop from empty array")

        last_index = self.length - 1
        last_item = self.data[last_index]
        del self.data[last_index]
        self.length -= 1
        return last_item

    def delete(self, index):
        if self.length == 0:
            raise IndexError("Delete from empty array")
        deleted_item = self.data[index]
        self._shift_items(index)
        return deleted_item

    def _shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length - 1]
        self.length = self.length - 1


def reverse(string):
    """
    input: Str abc
    output: Str cba
    """

    string_dict = {}
    reversed = ""

    for s in enumerate(string):
        string_dict[s[0]] = s[1]

    for s in range(len(string), 0, -1):
        reversed += string_dict[s-1]
    return reversed


def reverse_improved(string):
    """
    input: Str abc
    output: Str cba
    """
    reversed_string = ""

    for i in range(len(string) - 1, -1, -1):
        print(i)
        reversed_string += string[i]

    return reversed_string


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()  # temp var to create the new list}
    tail = dummy

    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2


def mergeTwoArrays(a1, a2):
    merged = []
    item1 = a1[0]
    item2 = a2[0]
    count1 = 0
    count2 = 0

    if len(a1) == 0:
        return a2

    if len(a2) == 0:
        return a1

    while item1 or item2:
        if item2 is None or item1 < item2:
            merged.append(item1)
            item1 = a1[count1]
            count1 = count1 + 1
        else:
            merged.append(item2)
            item2 = a2[count2]
            count2 = count2 + 1
    return merged

# hash map is the same thing as dict/obj
# basically is a key value pair


class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if (self.data[address] is None):
            self.data[address] = []
            self.data[address].append([key, value])
        else:
            self.data[address].append([key, value])

        return self.data

    def get(self, key):
        address = self._hash(key)
        current = self.data[address]
        if current:
            for i in current:
                if key == i[0]:
                    return i[1]
        else:
            return None

    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i]:
                keys_array.append(self.data[i][0][0])
        return keys_array


def get_first_recurring_char(array):
    """
    array: [2,3,4,5,5,5,2,3,1,5]
    return: 5
    return first recurring character
    """
    # convert that array into an hash map with key as index of the array
    # and value 0
    # itarate over the array and increase the size of the count
    # return the key when count == 2 (second time the value was seeing)
    hash_map = {}

    for i in array:
        hash_map[i] = 0

    for i in array:
        hash_map[i] = hash_map[i] + 1
        if hash_map[i] == 2:
            return i
    return None


hash_map = HashTable(30)
hash_map.set('grapes', 1000)
hash_map.set('apples', 1000)
hash_map.set('manzana', 1000)
hash_map.set('divino', 1000)
value = hash_map.get('grapes')


# print(get_first_recurring_char([1, 2, 2, 3, 4]))

# linked lists
# pointer is a reference to another place in memory

class NewNode:
    def __init__(self, value):
        self.node = {
            'value': value,
            'next': None
        }


class LinkedList:

    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):

        new_node = NewNode(value)
        self.tail['next'] = new_node.node
        self.tail = new_node.node  # updates reference
        self.length = self.length + 1
        return self

    def preppend(self, value):
        new_node = NewNode(value)
        new_node.node['next'] = self.head
        self.head = new_node.node  # updates reference
        self.length = self.length + 1

    def insert(self, index, value):
        if index > self.length:
            raise TypeError("Index out of range")
        # call append method if index is the last element
        if index == self.length:
            self.append(value)
            return

        # call preppend method if index is 0
        if index == 0:
            self.preppend(value)
            return

        current_node = self._traverse_to_index(index-1)
        new_node = NewNode(value)
        new_node.node['next'] = current_node['next']
        current_node['next'] = new_node.node
        self.length = self.length + 1

    def remove(self, index):
        if index > self.length:
            raise TypeError("Index out of range")
        leader = self._traverse_to_index(index-1)
        unwanted_node = leader['next']
        leader['next'] = unwanted_node['next']
        self.length = self.length - 1

    def _traverse_to_index(self, index):
        counter = 0
        current_node = self.head
        while counter != index:
            current_node = current_node['next']
            counter = counter + 1
        return current_node

    def lookup(self, index):
        return self._traverse_to_index(index-1)

    def print_linked_list(self):
        array = []
        current_node = self.head
        while current_node != None:
            array.append(current_node['value'])
            current_node = current_node['next']
        print(array)


# algoritmos
# recursion
# recursion rules
# 1 - Identify base case
# 2 - Identify the recursive case
# 3 - 2 return one for the base case and return the recursive case

# write the factorial
# factorial means multiply n * n-1 until we reach 1

def factorial_number(number):
    if number < 0:
        return "Error: negative number"
    if number == 0 or number == 1:
        return 1

    answer = number * factorial_number(number - 1)
    return answer


def iterative_factorial(number):
    if number < 0:
        return 'error'
    factorial = 1
    for n in range(number, 0, -1):
        factorial *= n
    return factorial


# given N return the index value of the Fibonacci sequence
# i.e: n = 5 return 2+
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ...

def recursive_fibo(index):
    """index: fibonaci index
       return fibonacci number
    """

    if index < 2:
        return index
    return recursive_fibo(index-1) + recursive_fibo(index-2)


def iterative_fibo(number):
    arr = [0, 1]
    for i in range(2, number+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[number]


iterative_fibo(7)


# Binary Search Tree
# all child nodes to the right increases
# all child nodes to the left decreases
# a node can only have up to 2 childrens

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value=value)
        if self.root == None:
            self.root = node

        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    # Left
                    if current_node.left == None:
                        current_node.left = node
                        return self
                    current_node = current_node.left
                else:
                    # Right
                    if current_node.right == None:
                        current_node.right = node
                        return self
                    current_node = current_node.right

    def lookup(self, value):
        if self.root == None:
            return None
        current_node = self.root

        while current_node != None:

            if value < current_node.value:
                current_node = current_node.left

            elif value > current_node.value:
                current_node = current_node.right

            elif current_node.value == value:
                return current_node
        return None


def traverse(node):
    tree = {
        'value': node.value
    }
    tree['left'] = None if node.left == None else traverse(node.left)
    tree['right'] = None if node.right == None else traverse(node.right)
    return tree


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)

# print(tree.lookup(66))


def merge_sorted_array(nums1, nums2, m, n):
    x, y = m-1, n-1

    for z in range(m + n - 1, -1, -1):
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
        elif y < 0:
            break
        elif nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
        else:
            nums1[z] = nums2[y]
            y -= 1


# loop through the array and:
# store the index with the lowest value first -> perfect time to buy
# loop through the array begining at the time you buy (index of the buying stock):
# store the index with the highst value
# if the lowest price is at the end of the array there is no profit, return 0
arr = [7, 6, 4, 3, 1]


def max_profit(array):
    lowest_index = 0
    min_price_so_far = array[0]
    max_price_so_far = 0

    length = len(array)
    for n in range(0, length):
        if array[n] < min_price_so_far:
            min_price_so_far = array[n]
            lowest_index = n

    for n in range(lowest_index, length):
        if array[n] > max_price_so_far:
            max_price_so_far = array[n]

    # return max_price_so_far - min_price_so_far
    print(min_price_so_far)
    print(max_price_so_far)


max_profit(arr)
