def answer(document, searchTerms):
    """
    The approach here is to run a sliding window that scans through the
    document while maintaining the constraint that we need to satisfy.
    (All words we are searching for present in the sliding window)

    When the constraint is met we try to reduce the sliding window size,
    until the constraint breaks. We compare that size to the smallest we've
    found so far and if necessary update.
    """
    target = {}

    # store all words that we need to find
    for word in searchTerms:
        target[word] = target.get(word, 0) + 1

    # Store indices to measure snippet size
    prev = start = 0

    # Initialize snippet size as entire document size
    snippet_size, snippet_wordsize = len(document), len(document.split(' ')) + 1

    # buffer used to store characters forming a word.
    # term_count used to determine the number of words found
    buffer, term_count = '', 0
    for i in range(len(document)):
        if document[i] != ' ' and i < len(document) - 1:
            # Add characters to buffer until we form a word (space found)
            buffer += document[i]
        else:
            # If we are at the last character, add it to the buffer.
            if i == len(document) - 1:
                    buffer += document[i]
                    i += 1
            # If the word in buffer is a word we are searching for
            # Reduce it's count and increment term_count
            if buffer in target:
                target[buffer] -= 1
                if target[buffer] >= 0:
                    term_count += 1
            buffer = ''

            # While constraint is satisifed, try popping words to find
            # smallest snippet
            while term_count == len(searchTerms):
                if len(document[prev:i].split(' ')) < snippet_wordsize:
                    snippet_size = i - prev + 1
                    snippet_wordsize = len(document[prev:i].split(' '))
                    start = prev

                j = prev
                prev_word = ''
                while j < len(document) and document[j] != ' ':
                    prev_word += document[j]
                    j += 1

                if prev_word in target:
                    target[prev_word] += 1
                    if target[prev_word] > 0:
                        term_count -= 1

                prev = j+1

    return document[start:start + snippet_size - 1]