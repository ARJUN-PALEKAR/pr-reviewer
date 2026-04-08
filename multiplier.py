def store_multiplier(number, memory=[]):
    memory.append(number * 2)
    return memory

print(store_multiplier(5))
print(store_multiplier(10))