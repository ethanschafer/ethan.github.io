from string import *

def cipher( x, dist ):
  #alpha = ascii_lowercase
  #shift = alpha[ : ]

  alpha = "abcdefghijklemnopqrstuvwxyz"

  backAlpha = ""
  for let in range(len(alpha)-dist):
    backAlpha +=alpha[let]

  frontAlpha = ""
  for let in range(len(alpha)-dist,len(alpha)):
    frontAlpha += alpha[let]

  shift = ""
  shift = frontAlpha + backAlpha

  ans = ""
  for c in x:
    ans +=shift[alpha.find(c)]
  return ans;

print ( cipher("abcdef", 1) )
print ( cipher("abcdef", 2) )
print ( cipher("abcdef", 3) )
print ( cipher("dogcatpig", 1) )
print ( cipher("dogcatpig", 2) )
print ( cipher("dogcatpig", 3) )
