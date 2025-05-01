#!/usr/bin/env python3

from hashTables import hashTable


hp = hashTable(10)
print(hp.buckets)
# hp.print_table()
hp.put("Amanuel", "Bikora")
hp.put("Getahun", "Bikora")
hp.put("Kidist", "Bikora")
hp.put("Tsige", "Zeleke")
print(hp.buckets)
print(hp.get("Tsige"))