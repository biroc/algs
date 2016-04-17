def answer(document, searchTerms):
    target = {}
    for word in searchTerms:
        target[word] = target.get(word, 0) + 1

    prev = start = 0
    snippet_size, snippet_wordsize = len(document), len(document.split(' ')) + 1
    buffer, term_count = '', 0
    for i in range(len(document)):
        if document[i] != ' ' and i < len(document) - 1:
            buffer += document[i]
        else:
            if i == len(document) - 1:
                    buffer += document[i]
                    i += 1
                
            if buffer in target:
                target[buffer] -= 1
                if target[buffer] >= 0:
                    term_count += 1
            buffer = ''
            
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