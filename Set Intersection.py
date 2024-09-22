setx = {"green", "blue"}
sety = {"blue", "yellow"}

print(f"Original set elements: \n{setx}\n(sety)")

print("\nIntersection of two sets:")
setz = setx.intersection(sety)
print(setz)

print("\nUnion of two sets:")
setz = setx.union(sety)
print(setz)

print("\nDifference of two sets:")
setz = setx.difference(sety)
print(setz)

print("\nSymmentric difference of two sets:")
setz = setx.symmentric_difference(sety)
print(setz)