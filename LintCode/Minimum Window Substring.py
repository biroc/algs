class Solution:
    """
    @param source: A string
    @param target: A string
    @return: A string denote the minimum window
             Return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if not source or not target: return ""
        target_chars = {}
        target_length = len(target)
        for c in target:
            if c in target_chars: target_chars[c] += 1
            else: target_chars[c] = 1

        window_size = len(source) + 1
        start = previous = 0
        character_count = 0
        for i in range(len(source)):
            if source[i] not in target_chars: continue

            target_chars[source[i]] -= 1
            if target_chars[source[i]] >= 0:
                character_count += 1

            while character_count == target_length:
                if i - previous + 1 < window_size:
                    start = previous
                    window_size = i - previous + 1

                char_at_previous = source[previous]
                if char_at_previous in target_chars:
                    target_chars[char_at_previous] += 1
                    if target_chars[char_at_previous] > 0:
                        character_count -= 1

                previous += 1

        if window_size > len(source):
            return ""

        return source[start:start+window_size]