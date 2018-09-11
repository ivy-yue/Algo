# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

for (name, HashTable) in [("linear probing", HashTableProbing)]:
    table = HashTable()
    # table.insert("example_key", "example_value")
    # table.insert("example_key1", "examplewfw_value")
    # table.insert("example_key2", "example_1v12alue")
    # table.insert("example_key3", "example_v331alue")
    # table.insert("example_key5", "example_va13214lue")
    for i in range(20):
        name = "example" + str(i)
        val = "value" + str(i)
        table.insert(name, val)
    print table.get("example5")
    print table.get("example11")
    # if table.get("example_key") != "example_value":
    #     print("%s hash table did not return example value"%name)
    for i in range(10):
        name = "example" + str(i)
        table.remove(name)
    print table.size()
