# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# An implementation of a hash table that uses linear probing to handle collisions.
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
    hash_key = cs5112_hash1(key) % self.size
    while self.array.get(hash_key) != None:
      hash_key = (hash_key + 1) % self.size
    self.array.set(hash_key, (key, value))
    self.item_count += 1
    if(self.item_count / self.array_size > self.load_factor):
      self._resize_array()
    # YOUR CODE HERE

    raise NotImplementedError()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    # YOUR CODE HERE
    hash_key = cs5112_hash1(key) % self.size
    start = hash_key
    while self.array.get(hash_key)[0] != key:
      hash_key += 1
      if hash_key == start:
        return None
    return self.array.get(hash_key)[1]



  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    # YOUR CODE HERE
    self.item_count -= 1
    hash_key = cs5112_hash1(key) % self.size
    start = hash_key
    while self.array.get(hash_key)[0] != key:
      hash_key += 1
      if hash_key == start:
        return None
    self.array.set(hash_key, None)
    return self.array.get(hash_key)[1]


  # Returns the number of elements in the hash table.
  def size(self):
    # YOUR CODE HERE
    return self.item_count


  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
      new_array_size = 2 * self.array_size
      new_array = FixedSizeArray(new_array_size)
      for i in self.array_size:
          new_hash_index = self.array.get(i)[0] % new_array_size
          while new_array.get(new_hash_index) != None:
              new_hash_index += 1


    # YOUR CODE HERE

    raise NotImplementedError()

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array