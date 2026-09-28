class Solution(object):

  def numberOfSpecialChars(self, word):
    last_lower = {}
    first_upper = {}

    # Single pass to record required positions
    for i, ch in enumerate(word):
      if ch.islower():
        last_lower[ch] = i  # Overwrites to keep the last occurrence
      elif ch.isupper() and ch not in first_upper:
        first_upper[ch] = i  # Saves only the first occurrence

    # Count valid special characters
    special_count = 0
    for ch in last_lower:
      upper_ch = ch.upper()
      if upper_ch in first_upper and last_lower[ch] < first_upper[upper_ch]:
        special_count += 1

    return special_count