class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        target_counter = Counter(t)
        window_counter = Counter()  # This will keep a count of characters in the current window
        valid_char_count = 0       # Number of characters that meet the target criteria
        left = 0                   # Left pointer to shrink the window
        min_left = -1              # Left boundary index of the minimum window
        min_size = inf             # Initialize min_size to positive infinity

        # Iterate over each character in the source string
        for right, char in enumerate(s):
            # Include current character in the window
            window_counter[char] += 1
            # If the current character is needed and the window contains enough of this character
            if target_counter[char] >= window_counter[char]:
                valid_char_count += 1
          
            # If the window has all the characters needed
            while valid_char_count == len(t):
                # If this window is smaller than the minimum so far, update minimum size and index
                if right - left + 1 < min_size:
                    min_size = right - left + 1
                    min_left = left
              
                # If the character at the left pointer is less frequent in the window than in the target,
                # reducing it further would break the window condition
                if target_counter[s[left]] >= window_counter[s[left]]:
                    valid_char_count -= 1
              
                # Shrink the window from the left
                window_counter[s[left]] -= 1
                left += 1
      
        # If no window meets the criteria, return an empty string
        return '' if min_left < 0 else s[min_left:min_left + min_size]
