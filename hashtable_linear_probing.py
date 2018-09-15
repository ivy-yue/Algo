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

  # ============ We mark a flag for DELETION ============

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    # first search
    self.item_count += 1
    if (self.item_count * 1.0 / self.array_size) > self.load_factor:
      self._resize_array()
    hash_key = cs5112_hash1(key) % self.array_size
    while self.array.get(hash_key) is not None\
            and self.array.get(hash_key)[0] != key\
            and not self.array.get(hash_key)[2]:  # not deleted
      hash_key = (hash_key + 1) % self.array_size
    # if there is an vacant array in the middle, just reset it
    # if previously key is associated, just replace it
    self.array.set(hash_key, (key, value, False))
    # Delete previously entry with the same key
    hash_key += 1
    while self.array.get(hash_key) is not None:
      if self.array.get(hash_key)[0] == key:
        self.array.set(hash_key, (key, value, True))
      hash_key = (hash_key + 1) % self.array_size



  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    hash_key = cs5112_hash1(key) % self.array_size
    while self.array.get(hash_key) is not None:
        if not self.array.get(hash_key)[2] and self.array.get(hash_key)[0] == key:
            return self.array.get(hash_key)[1]
        hash_key += 1
    return None
    # Removed start var since we will not search the whole array
    # for the worst case hash(value) = constant:
    # since the load factor < 1, there must be some None in the array [never has elements]
    # start = hash_key
    # while self.array.get(hash_key)[0] != key:  # TODO: if the entry is None, it will cause Exception
    #   hash_key += 1
    #   if hash_key == start:
    #     return None
    # return self.array.get(hash_key)[1]



  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    if self.item_count == 0:
        return None  # add a corner case to accelerate
    # self.item_count -= 1  # TODO: if non-exist, count should not -1
    # search for the entry first
    hash_key = cs5112_hash1(key) % self.array_size
    while self.array.get(hash_key) is not None:
        if not self.array.get(hash_key)[2] and self.array.get(hash_key)[0] == key:
            value = self.array.get(hash_key)[1]
            # mark the entry as deleted
            self.array.set(hash_key, (key, value, True))
            self.item_count -= 1
            return value
    return None
    # start = hash_key
    # while self.array.get(hash_key) is None or self.array.get(hash_key)[0] != key:
    #   # TODO: time complexity is O(array_size) which could be optimized at least to O(array_size * load_factor)
    #   hash_key = (hash_key + 1) % self.array_size
    #   if hash_key == start:
    #     return None
    # return_val = self.array.get(hash_key)[1]
    # self.array.set(hash_key, None)
    # return return_val


  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count


  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    new_array_size = 2 * self.array_size
    new_array = FixedSizeArray(new_array_size)
    for i in range(self.array_size):
        if self.array.get(i) is None or not self.array.get(i)[2]:
            continue
        new_hash_index = cs5112_hash1(self.array.get(i)[0]) % new_array_size
        while new_array.get(new_hash_index) is not None: # for a new array, we do not consider deleted case
          new_hash_index = (new_hash_index + 1) % new_array_size
        new_array.set(new_hash_index, self.array.get(i))
    self.array = new_array
    self.array_size = new_array_size


  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array
