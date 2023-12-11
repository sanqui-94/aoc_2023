# each line originally contained a specific calibration value that the Elves now need to recover
# first digit + last digit(in that order)
# -- part one --
# import re

# total = 0

# while True:
#   try:
#     line = input()
#     nums = re.findall(r'\d', line)
#     total = total + (10 * int(nums[0])) + int(nums[len(nums) - 1])
#   except EOFError:
#     print(total)
#     break

# -- part two --
import re

total = 0
dicc = {
  "one": 1,
   "two": 2,
   "three": 3,
  "four": 4,
   "five": 5,
   "six": 6,
   "seven": 7,
   "eight": 8,
   "nine": 9,
   "1": 1,
   "2": 2,
   "3": 3,
  "4": 4,
   "5": 5,
   "6": 6,
   "7": 7,
   "8": 8,
   "9":9,
   "0":0
}

pattern = r'(?:\d|one|two|three|four|five|six|seven|eight|nine)'
while True:
  try:
    line = input()
    # pattern = '(?:' + '|'.join(map(re.escape, matches)) + ')'
    # buildingBlock = "zero|one|two|three|four|five|six|seven|eight|nine"
    # p1 = "(?:\d|"
    # p3 = ")"
    
    # pattern2 = r'(?:\d|enin|thgie|neves|xis|evif|ruof|eerht|owt|eno)'
    # pattern = r'p1 + buildingBlock + p3'
    first = ""
    last = ""
    for x in range(len(line)):
      slice = line[x:]
      num1 = re.match(pattern, slice)
      if num1:
        if first == "":
          first = num1.group(0)
        else:
          last = num1.group(0)
 
    if last == "":
      last = first
    total = total + (10 * dicc[first]) + dicc[last]
  except EOFError:
    print(total)
    break

# try going over the string, creating slices for every char until the end of string
