  def isMatch(self, s: str, p: str) -> bool:

      def search(regex, matcher):
          if len(regex) == 0:
              return len(matcher) == 0
          elif len(matcher) == 0:
              return len(regex) == 0

          else:

              if len(regex) >= 2 and regex[1] == "*":
                  return search(regex[2:], matcher[1:]) or search(regex, matcher[1:])

              else:

                  if regex[0] == matcher[0] or regex[0] == ".":
                      return search(regex[1:], matcher[1:])
                  elif regex[0] != matcher[0]:
                      return False
                  else:
                      return False

      return search(p, s)
