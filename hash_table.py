from linkedlist import TuplesLinkedList

class HashTable:
    def __init__(self, buckets):
        self.buckets = [TuplesLinkedList() for i in range(buckets)]

    def get(self, key):
        return (self.buckets[self.calc_hash_code(key)].find(key))

    def put(self, key, value):
        self.buckets[self.calc_hash_code(key)].add(key, value)

    def calc_hash_code(self, key):
        hash_code = 0
        for i in range(0,len(key)):
            hash_code += ord(key[i])
        return hash_code