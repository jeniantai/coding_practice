# To depict the steps of a recursive function, we’ll use a call stack and execution contexts for each function call.
# The call stack stores each function (with its internal variables) until those functions resolve in a last in, first out order.

def sum_to_one_iter(n):
  result = 1
  call_stack = []
  # loop of recursive calls which lead to a base case.
  while n != 1:
    execution_context = {'n_value': n}
    # push the recusive function calls onto the system's call stack
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print('BASE CASE REACHED')

  while len(call_stack) != 0:
    return_value = call_stack.pop()
    # see how execution contexts are removed from call stack
    print(call_stack)
    print("Return value of {0} adding to result {1}".format(return_value['n_value'], result))
    result += return_value['n_value']

  return result, call_stack




# Now lets create a truly recusive function
def sum_to_one_recur(n):
  if n == 1:
    return n
  # help visualize
  print("Recursing with input: {0}".format(n))
  # return argument + recursive_call(argument - 1)
  return n + sum_to_one_recur(n - 1)


# Linear - O(N), where "N" is the number of digits in the number
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n != 0:
    result += n % 10
    n = n // 10
  return result + n

# sum_digits recursively
def sum_digits2(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  if n <= 9:
    return n
  last_digit = n % 10
  return sum_digits(n // 10) + last_digit


# O(N)
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min

# find_min recursively
def find_min2(my_list, min = None):
  # if input is an empty list, return min
  if not my_list:
    return min
  # if min is None OR first element of list is < min
  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min2(my_list[1:], min)

# Palindromes are words which read the same forward and backward.
# In each iteration of the loop that doesn’t return False, we make a copy of the string with two fewer characters.
# Copying a list of N elements requires N amount of work in big O >> O(N^2)
def is_palindrome(str):
  while len(str) > 1:
    if str[0] != str[-1]:
      return False
    str = str[1:-1]
  return True 

# A more efficient version: Linear - O(N)
def is_palindrome1(str):
  str_length = len(str)
  middle_index = str_length // 2
  for index in range(0, middle_index):
    opposite_character_index = str_length - index - 1
    if str[index] != str[opposite_character_index]:
      return False  
  return True

# using recursive calls
def is_palindrome3(str):
  if len(str) < 2:
    return True
  if str[0] != str[-1]:
    return False
  return is_palindrome(str[1:-1])

# iterative 
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result

# recursive
def multiplication1(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0
  return num_a + multiplication1(num_a, num_b - 1)

# O(N)
def factorial(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n <= 1:
    return 1
  return n*factorial(n-1)


# lets rewrite factorial iteratively
def factorial_iter(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n <= 1:
    return 1
  
  result = 1
  while n != 1:
     result *= n
     n -= 1
  return result



def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [[my_list[0]] + rest for rest in power_set_without_first]
    # return combination of the two
    return with_first + power_set_without_first
  


def flatten(my_list):
  result = []
  for i in my_list:
    if isinstance(i, list):
      print('List found!')
      flat_list = flatten(i)
      result += flat_list
    else:
      result.append(i)
  return result




# Multiple recursive calls
# runtime: Exponential - O(2^N)
def fibonacci(n):
  # base cases
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n < 2:
    return n
  
  # recursive step
  # note there are quite a bit of repeated function calls with the same input. This contributes to the expensive runtime
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci the iterative way
def fibonacci1(n):
  if n < 0:
    ValueError("Input 0 or greater only!")

  fibs = [0, 1]
  
  if n <= len(fibs) - 1:
    return fibs[n]
  
  while n > len(fibs) - 1:
    fibs.append(fibs[-1] + fibs[-2])
    
  return fibs[-1]





# Since the problem is that we re-compute values we have already computed, 
# we can instead choose to save the values we have already computed in a dict, 
# This is called memoization.
# Python 3 includes a decorator to do this - automatic memoization!
import functools
@functools.lru_cache(None)
def fibonacci2(n):
  if n < 0:
    ValueError('Inputs 0 or greater only.')
  if n < 2:
      return n
  print("Recursive call with {0} as input".format(n))
  return fibonacci2(n-1) + fibonacci2(n-2)

# dynamic programming - memorization
memo = {}
def fibonacci_mem(num):
  if num in memo:
    return memo[num]
  elif num <= 1:
    return num
  else:
    memo[num] = fibonacci_mem(num - 1) + fibonacci_mem(num - 2)
  return memo[num]


# another memorization example
def knapsack(loot, weight_limit):
  grid = [[0 for col in range(weight_limit + 1)] for row in range(len(loot) + 1)]
  for row, item in enumerate(loot):
    row = row + 1
    for col in range(weight_limit + 1):
      weight_capacity = col
      if item.weight <= weight_capacity:
        item_value = item.value        
        item_weight = item.weight
        previous_best_less_item_weight = grid[row - 1][weight_capacity - item_weight]
        capacity_value_with_item = item_value + previous_best_less_item_weight
        capacity_value_without_item = grid[row - 1][col]
        grid[row][col] = max(capacity_value_with_item, capacity_value_without_item)
      else:
        grid[row][col] = grid[row - 1][col]
   
  return grid[-1][-1]

def recursive_knapsack(weight_cap, weights, values, i):
  # base condition
  if weight_cap == 0 or i == 0:
    return 0
  elif weights[i - 1] > weight_cap:
    return recursive_knapsack(weight_cap, weights, values, i - 1)
  else:
    include_item = values[i - 1] + recursive_knapsack(weight_cap - weights[i - 1], weights, values, i - 1);

    exclude_item = recursive_knapsack(weight_cap, weights, values, i - 1);

    return max(include_item, exclude_item)

def dynamic_knapsack(weight_cap, weights, values):
  rows = len(weights) + 1
  cols = weight_cap + 1
  # Set up 2D array
  matrix = [ [] for x in range(rows) ]

  # Iterate through every row
  for index in range(rows):
    # Initialize columns for this row
    matrix[index] = [ -1 for y in range(cols) ]

    # Iterate through every column
    for weight in range(cols):
      if index == 0 or weight == 0:
        matrix[index][weight] = 0
      # If weight at previous row is less than or equal to current weight
      elif weights[index - 1] <= weight:
        # Calculate item to include
        include_item = values[index - 1] + matrix[index - 1][weight - weights[index - 1]]
        # Calculate item to exclude
        exclude_item = matrix[index - 1][weight]
        # Calculate the value of current cell
        matrix[index][weight] = max(include_item, exclude_item)
      else:
        # Calculate the value of current cell
        matrix[index][weight] = matrix[index - 1][weight]
  # Return the value of the bottom right of matrix
  return matrix[rows-1][weight_cap]

# longest common subsequence is the series of letters from left to right two strings share
# e.g. longest sequence is "ABAD" given "ABAZDC" and "BACBAD"
def longest_common_subsequence(string_1, string_2):
  print("Finding longest common subsequence of {0} and {1}".format(string_1, string_2))
  # For the longest common subsequence, we’ll need a grid where the columns are 
  # each character from one string, and the rows are each character from the other string. 
  # We’ll add an extra column and row to represent an empty string or “no character”.
  grid = [[0 for col in range(len(string_1)+1)] for row in range(len(string_2)+1)]
  
  for row in range(1, len(string_2)+1):
    print("Comparing: {0}".format(string_2[row - 1]))
    for col in range(1, len(string_1) + 1):
      print("Against: {0}".format(string_1[col - 1]))
      if string_1[col - 1] == string_2[row - 1]:
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])
  
  for row_line in grid:
    print(row_line)

  # construct subsequence value
  result = []
  while row > 0 and col > 0:
    if string_1[col - 1] == string_2[row - 1]:
      result.append(string_1[col - 1])
      row -= 1
      col -= 1
    elif grid[row - 1][col] > grid[row][col - 1]:
      row -= 1
    else:
      col -= 1
  result.reverse()
  return "".join(result)


# a function to recursively build binary tree
def build_bst(my_list):
  # base case
  if len(my_list) == 0:
    # return 'No Child'
    return None
  # recursive step
  middle_idx = len(my_list)//2
  middle_value = my_list[middle_idx]
  # my_list.pop()
  print('Middle index: {}'.format(middle_idx))
  print('Middle value: {}'.format(middle_value))
  # this tree should sprawl across all elements of the list
  tree_node = {'data': middle_value}
  # since data key will store the middle value, we shall exclude it in the branches
  tree_node['right_child'] = build_bst(my_list[middle_idx+1:])
  tree_node['left_child'] = build_bst(my_list[:middle_idx])
  # As the recursive calls resolve and pop off the call stack, the final return value 
  # will be the root or “top” tree_node which contains a reference to every other tree_node
  return tree_node


# find depth of tree iteratively
# This algorithm will visit each node in the tree once, which makes it a linear runtime, O(N), 
# where N is the number of nodes in the tree.
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if "left_child" in child:
        queue.append(child["left_child"])
      if "right_child" in child:
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result

def depth2(tree):
  if not tree:
    return 0

  left_depth = depth2(tree["left_child"])
  right_depth = depth2(tree["right_child"])

  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1

class BinarySearchTree:
  def __init__(self, value, depth=1):
    self.value = value
    self.depth = depth
    self.left = None
    self.right = None
    
  # If a new value is less than the current (root) node’s value, we want to insert it to its left subtree.
  # If the new value is less than the root node's value
  #   If a left child node does not exist
  #     Create a new BinarySearchTree with the new value and updated depth and assign it to the left pointer
  #   Else
  #     Recursively call .insert() on the left child node  
  # Else
  #   If a right child node does not exist
  #     Create a new BinarySearchTree with the new value and updated depth and assign it to the right pointer
  #   Else
  #     Recursively call .insert() on the right child node
  def insert(self, value):
    if value < self.value:
      if self.left == None:
        self.left = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
      else:
        self.left.insert(value)
    else:
      if self.right == None:
        self.right = BinarySearchTree(value, self.depth + 1)
        print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
      else:
        self.right.insert(value)

  def get_node_by_value(self, value):
    if value == self.value:
      return self
    elif self.left != None and value < self.value:
      return self.left.get_node_by_value(value)
    elif self.right != None and value >= self.value:
      return self.right.get_node_by_value(value)
    else:
      return None

  # this is inorder traversal
  def depth_first_traversal(self):
    if (self.left is not None):
      self.left.depth_first_traversal()
    print(f'Depth={self.depth}, Value={self.value}')
    if (self.right is not None):
      self.right.depth_first_traversal()

      
# recursive binary search
# this solution reduce the sorted input list by making a smaller copy of the list.
# this is wasteful, we can do better by using pointers instead of copying the list.
def binary_search(sorted_list, target):
  if not sorted_list:
    return 'value not found'
  mid_idx = len(sorted_list)//2
  mid_val = sorted_list[mid_idx]
  if mid_val == target:
    return mid_idx
  if mid_val > target:
    left_half = sorted_list[:mid_idx]
    return binary_search(left_half, target)
  if mid_val < target:
    right_half = sorted_list[mid_idx+1:]
    result = binary_search(right_half, target)
    if result == "value not found":
      return result
    else:
      return result + mid_idx + 1
    
def binary_search_pointer(sorted_list, left_pointer, right_pointer, target):
  # this condition indicates we've reached an empty "sub-list"
  if left_pointer >= right_pointer:
    return "value not found"

  # We calculate the middle index from the pointers now
  mid_idx = (left_pointer + right_pointer) // 2
  mid_val = sorted_list[mid_idx]

  if mid_val == target:
    return mid_idx
  if mid_val > target:
    # we reduce the sub-list by passing in a new right_pointer
    return binary_search_pointer(sorted_list, left_pointer, mid_idx, target)
  if mid_val < target:
    # we reduce the sub-list by passing in a new left_pointer
    return binary_search_pointer(sorted_list, mid_idx + 1, right_pointer, target)
  
# binary search the iterative way
def binary_search_iter(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  
  # fill in the condition for the while loop
  while left_pointer < right_pointer:
    # calculate the middle index using the two pointers
    mid_idx = (left_pointer + right_pointer)//2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val:
      right_pointer = mid_idx
    if target > mid_val:
      left_pointer = mid_idx + 1
  
  return "Value not in list"