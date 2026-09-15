from itertools import combinations

VARS = ['a', 'b', 'c', 'd', 'e']

ORDERS = {
  1: ["0","1"],
  2: ["00","01","10","11"],
  3: ["000","001","010","011","100","101","110","111"],
  4: ["0000","0001","0010","0011","0100","0101","0110","0111",
      "1000","1001","1010","1011","1100","1101","1110","1111"],
  5: ["00000","00001","00010","00011","00100","00101","00110","00111",
      "01000","01001","01010","01011","01100","01101","01110","01111",
      "10000","10001","10010","10011","10100","10101","10110","10111",
      "11000","11001","11010","11011","11100","11101","11110","11111"]
}

def read_input(n):
  minterms = []
  print("\nEnter value for each binary input:")
  for i, bits in enumerate(ORDERS[n]):
    if input(f"{bits}: ").strip() == "1":
      minterms.append(i)
  return minterms


def combine(a, b):
  diff = 0
  out = ""
  for x, y in zip(a, b):
    if x == y:
      out += x
    elif x != '-' and y != '-':
      diff += 1
      out += '-'
    else:
      return None
  return out if diff == 1 else None

def prime_implicants(minterms, n):
  current = {format(m, f'0{n}b'): {m} for m in minterms}
  primes = {}

  while current:
    used = set()
    nxt = {}

    pats = list(current.keys())

    for i in range(len(pats)):
      for j in range(i + 1, len(pats)):
        c = combine(pats[i], pats[j])
        if c:
          used.add(pats[i])
          used.add(pats[j])
          nxt.setdefault(c, set()).update(current[pats[i]] | current[pats[j]])

    for p in pats:
      if p not in used:
        primes[p] = current[p]

    current = nxt

  return primes

def term(p):
  s = ""
  for i, x in enumerate(p):
    if x == "1":
      s += VARS[i]
    elif x == "0":
      s += VARS[i] + "'"
  return s or "1"

def minimum_covers(primes, minterms):
  plist = list(primes.keys())

  for r in range(1, len(plist) + 1):
    ans = []
    best_lits = None

    for comb in combinations(range(len(plist)), r):
      cover = set()
      lits = 0

      for i in comb:
        cover |= primes[plist[i]]
        lits += plist[i].count("0") + plist[i].count("1")

      if cover >= set(minterms):
        if best_lits is None or lits < best_lits:
          best_lits = lits
          ans = [comb]
        elif lits == best_lits:
          ans.append(comb)

    if ans:
      return ans, plist

def main():
  n = int(input("Number of variables (1-5): "))

  if n not in ORDERS:
    print("Invalid input.")
    exit()

  minterms = read_input(n)

  if not minterms:
    print("\nF = 0")
    exit()

  if len(minterms) == 2**n:
    print("\nF = 1")
    exit()

  primes = prime_implicants(minterms, n)

  # print("\nPrime Implicants:")
  # for p in primes:
  #   print(f"{p} -> {term(p)}")

  covers, plist = minimum_covers(primes, minterms)

  print("Expression:")
  for i, c in enumerate(covers, 1):
    expr = " + ".join(term(plist[j]) for j in c)
    print(f"{i}. {expr}")

main()