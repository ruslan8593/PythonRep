immutable_var = 1, 2, 3, True, "String", 0.5, [2, 3, 45]
print(immutable_var)
immutable_var[6][0] = 13
print(immutable_var)
mutable_var = [1, 2, 3, 4, 5, "mouse"]
print(mutable_var)
mutable_var[0] = "String"
print(mutable_var)