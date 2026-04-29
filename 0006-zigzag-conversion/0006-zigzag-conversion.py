class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        rows = ["" for _ in range(numRows)]
        j=0
        for ch in s:
          rows[j]+=ch
          if j==(numRows-1):
            step=-1
          elif j==0:
            step=1
          j=j+step
          
        return "".join(rows)