def hanoi(n, a, b, c):
  if n == 0:
      return
  hanoi(n-1, a, c, b)
  move(a, b)
  hanoi(n-1, c, b, a)
  move(b, a)
  hanoi(n-1, a, b, c)

def move(from_rod, to_rod):
  print(f"Moving disk from rod {from_rod} to rod {to_rod}")

n = 3
a = "A"
b = "B"
c = "C"

hanoi(n, a, b, c)