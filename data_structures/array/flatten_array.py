# Input - [1,2,3,4,[5,6,7,8],[9,10]]
# Output - [1,2,3,4,5,6,7,8,9,10]

lst = [1,2,3,4,[5,6,7,8],[9,10]]

flat = []

for sub in lst:
  if isinstance(sub, list):
    flat.extend(sub)
  else:
    flat.append(sub)
  
