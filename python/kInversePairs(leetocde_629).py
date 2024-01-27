class Solution:
  def kInversePairs(self, n: int, k: int) -> int:
      MOD = 1000_000_007

      prev = [0] * (k+1);
      prev[0] = 1;

      for N in range(1,n+1):
          cur = [0]*(k+1)
          total = 0
          for K in range(0,k+1):
              if K>N:
                  total -= prev[K - N]
              total += prev[K]
              cur[K] = total%MOD
          prev = cur
      return prev[k] 
