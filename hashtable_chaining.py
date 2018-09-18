# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    self.item_count += 1
    if (self.item_count * 1.0 / self.array_size) > self.load_factor:
      self._resize_array()
    index = cs5112_hash1(key) % self.array_size
    if self.array.get(index) is None:
      self.array.set(index, SLLNode((key, value)))
    else:
      node = self.array.get(index)
      prevNode = node
      while node is not None:
        if node.get_value()[0] == key:
          # overwrite
          node.set_value((key, value))
          self.item_count -= 1
          return
        prevNode = node
        node = node.get_next()
      prevNode.set_next(SLLNode)

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    index = cs5112_hash1(key)
    node = self.array.get(index)
    while node is not None:
      if node.get_value()[0] == key:
        return node.get_value()[1]
      node = node.get_next()
    return None


  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    index = cs5112_hash1(key)
    node = self.array.get(index)
    prevNode = None
    while node is not None:
      if node.get_value()[0] == key:
      # delete this node
        if prevNode is None:
          self.array.set(index, node.get_next())
        else:
          prevNode.set_next(node.get_next())
        self.item_count -= 1
        return node.get_value()[1]
      prevNode = node
      node = node.get_next()
    return None

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    new_array_size = 2 * self.array_size
    new_array = FixedSizeArray(new_array_size)
    for i in range(self.array_size):
      if self.array.get(i) is None:
        continue
      node = self.array.get(i)
      while node is not None:
        new_index = cs5112_hash1(node.get_value()[0]) % new_array_size
        new_node = new_array.get(new_index)
        if new_node is None:
          new_array.set(new_index, SLLNode(node.get_value()))
        else:
          while new_node.get_next() is not None:
            new_node = new_node.get_next()
          new_node.set_next(SLLNode(node.get_value()))
    self.array = new_array
    self.array_size = new_array_size

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array
