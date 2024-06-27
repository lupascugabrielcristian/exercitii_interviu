
# ENUMERATE
l = [5, 4, 6]
for (index, value) in enumerate(l):
    print(f"La {index} am {value}")

# LIST SHALOW COPY
l = [5, 4, 6]
dl = [e for e in l]
print(dl)