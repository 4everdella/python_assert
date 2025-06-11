batch = [40, 26, 39, 30, 25, 21]

cut = 26

for i in batch:
    assert i >= 26, "Batch is Rejected"
    print(str(i) + " is O.K")