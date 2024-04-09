#!/usr/bin/env python3

LRUCache = __import__("3-lru_cache").LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.get("B")
my_cache.get("B")
my_cache.get("B")
my_cache.get("C")
my_cache.get("C")
