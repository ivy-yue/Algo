# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # Adds an element to the bloom filter using three hash functions.
  def add_elem(self, elem):
    self.array.set(cs5112_hash1(elem) % self.size, True)
    self.array.set(cs5112_hash2(elem) % self.size, True)
    self.array.set(cs5112_hash3(elem) % self.size, True)
    # raise NotImplementedError

  # Returns False if the given element is was definitely not added to the
  # filter. Returns True if it's possible that the element was added to the
  # filter (but not necessarily certain).
  def check_membership(self, elem):
    return self.array.get(cs5112_hash1(elem) % self.size) & self.array.get(cs5112_hash2(elem) % self.size) & self.array.get(cs5112_hash3(elem) % self.size)
    # raise NotImplementedError
