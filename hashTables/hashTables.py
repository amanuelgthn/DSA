#!/usr/bin/env python3

class hashTable:
    def __init__(self, size=100):
        #initializing the hashTable to hold the key values in a list of list
        self.size = size
        self.buckets = [[] for _ in range(size)]
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        #accessing the bucket list at an index of the key in buckets list
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key,value)
                return
        bucket.append((key, value))
    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        for i , (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
    # def print_table(self):
    #     print(self.buckets)
        return False