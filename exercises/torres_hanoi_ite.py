def hanoi(n, a, b, c):
  for i in range(n):
      move(a, b)
      move(c, a)
      move(b, c)

def move(from_rod, to_rod):
  print(f"Moving disk from rod {from_rod} to rod {to_rod}")

n = 3
a = "A"
b = "B"
c = "C"

hanoi(n, a, b, c)