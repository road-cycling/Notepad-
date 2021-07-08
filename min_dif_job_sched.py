  def minDifficulty(jobDifficulty: List[int], d: int) -> int:

      memo = {}

      def recurse(tab, currIndex, jobsLeft):

          memoKey = (tab, currIndex, jobsLeft)

          if memoKey in memo:
              return memo[memoKey]

          jobsLeft -= 1

          maximum = -float('inf')
          minimum = float('inf')

          for i in range(currIndex, len(jobDifficulty) - jobsLeft):

              maximum = max(maximum, jobDifficulty[i])

              if jobsLeft >= 1:
                  minimum = min(maximum + recurse(tab + '\t', i + 1, jobsLeft), minimum)


          if jobsLeft == 0:
              memo[memoKey] = maximum
          else:
              memo[memoKey] = minimum

          return memo[memoKey]

      result = recurse('', 0, d)
      if result == float('inf'):
          return -1
      return result
