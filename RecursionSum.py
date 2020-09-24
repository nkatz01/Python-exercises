

Houses = [1, 2, 3, 4]

def IterativeSum(i):
  Total = 0
  while (i<4):
    Total += Houses[i]
    i = i+1
  return Total;
#print(Houses[0])
#print(IterativeSum(0))

def SumRecursive(i):
  if (i==0):
   return Houses[i];
  else:
#the sum of A[0],...,A[i]
#is the sum of elements A[0],...,A[i-1] and A[i]
    return SumRecursive(i-1)  +Houses[i];
#the computation of A[0]+...+A[n-1]


Total =  SumRecursive(len(Houses)-1);
#print(Total)

def SumAccum(i, acc):
  if (i==0):
    return acc + Houses[i];
  else:
    return SumAccum(i-1, Houses[i]+acc);

Total = SumAccum(len(Houses)-1,0);
#print(Total);
  

ispalindrome1 =  "Able was I ere I saw Elba";
ispalindrome2 = "racecar"
isntpalindrome = "raccar"
ispalindrome = ispalindrome1.replace(" ","").lower();

def CheckPalindrome(scentence):
  if (len(scentence)>1 and scentence[0] == scentence[-1]):
    return CheckPalindrome(scentence[1:-1]);
  elif len(scentence)==1: 
    return 1;
  else: 
    return 0

#print(CheckPalindrome(ispalindrome));

ispalindrome = ispalindrome2.replace(" ","").lower();
#print(CheckPalindrome(ispalindrome));
#print(CheckPalindrome(isntpalindrome));
 