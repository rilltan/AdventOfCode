inputfile = open("day25.txt")
lines = [a.strip() for a in inputfile.readlines()]
inputfile.close()

vals = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}

def snafuToDec(snafu):
  dec = 0
  pos = 1
  for i in range(-1, -len(snafu) - 1, -1):
    dec += vals[snafu[i]] * pos
    pos *= 5
  return dec


def decToSnafu(dec):
  snafu = ""
  best = 0
  temp = 0
  size = 0
  while (5**size)*2 < dec:
    size += 1
  while size >= 0:
    best = abs(dec - (temp + (5**size) * 2))
    val = "2"
    for i in vals:
      if abs(dec - (temp + (5**size) * vals[i])) < best:
        best = abs(dec - (temp + (5**size) * vals[i]))
        val = i
    snafu += val
    temp += (5**size)*vals[val]
    size -= 1
  return snafu


result = sum([snafuToDec(a) for a in lines])
print(decToSnafu(result))
