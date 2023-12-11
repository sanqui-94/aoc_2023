#12 red
#13 green
#14 blue
# -- part one --
# import re
# counter = 1
# total = 0
# validity = {
#   "red": 12,
#   "green": 13,
#   "blue": 14
# }

# while True:
#   try:
#     line = input()
#     games = line.split(":")[1].split(";")
#     valid = True
#     for game in games:
#         colors = game.split(",")
#         for color in colors:
#            color = color.strip()
#            [a, b] = color.split(" ")
#            if validity[b] < int(a):
#               valid = False
        
#     if valid:
#         total = total + counter
#     counter = counter + 1
#   except EOFError:
#     print(total)
#     break

# -- part two --
total = 0

while True:
  try:
    line = input()
    games = line.split(":")[1].split(";")
    mr = 1
    mb = 1
    mg = 1
  
    for game in games:
      colors = game.split(",")
      for color in colors:
        color = color.strip()
        [a, b] = color.split(" ")
        a = int(a)
        if b == "red" and a > mr:
          mr = a
        elif b == "green" and a > mg:
            mg = a
        elif b == "blue" and a > mb:
            mb = a


    total = total + (mb * mg * mr)
  except EOFError:
    print(total)
    break
