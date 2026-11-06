from linkedlist import TuplesLinkedList

class HashTable:
    def __init__(self, num_buckets):
        self.buckets = [TuplesLinkedList() for i in range(num_buckets)]
        self.num_buckets = num_buckets

    def get(self, key):
        return (self.buckets[self.calc_hash_code(key) % len(self.buckets)].find(key))

    def put(self, key, value):
        hash_code = self.calc_hash_code(key)

        # 68/17 = 4
        # 68%17 = 0 (no remainder)
        # 69%17 = 1 (remainder of 1)
        # 70%17 = 2 (remainder of 2)

        bucket_index = hash_code % self.num_buckets
        print(bucket_index)
        print(f"hash code is {hash_code}, nbuckets = {self.num_buckets}")
        self.buckets[bucket_index].add(key, value)

    def calc_hash_code(self, key):
        hash_code = 0
        for i in range(0,len(key)):
            hash_code += ord(key[i])
        return hash_code