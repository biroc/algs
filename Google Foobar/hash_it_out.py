def find_message(digest, previous_message):
    """
    digest[i] = ((129 * message[i]) ^ message[i-1]) % 256
    x = ((129 * message[i]) ^ message[i-1])
    so digest[i] = x % 256 or x = 256 * q + digest[i]
    which means 129 * message[i] = 256 * some_value + digest[i] ^ message[i-1]
    ( because XOR is its own inverse)
    => message[i] = 256 * some_value + digest[i] ^ message[i-1] / 129. We need to find
    'some_value' that makes the numerator a multiple of 129. or numerator % 129 = 0
    let's call some_value = multiple
    """
    multiple = 0
    while True:
        if ((256 * multiple) + (digest ^ previous_message)) % 129 == 0:
            return ((256 * multiple) + (digest ^ previous_message)) / 129
        else:
            multiple += 1


def answer(digest):
    messages = []
    for index, value in enumerate(digest):
        # first message always 0
        previous_message = 0
        # otherwise take previous message
        if index > 0:
            previous_message = messages[index-1]
        messages.append(find_message(value,previous_message))

    return messages
