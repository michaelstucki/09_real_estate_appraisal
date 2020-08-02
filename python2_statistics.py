
def mean(data):
    total = 0
    count = 0
    for x in data:
        count += 1
        total += x

    return total / count if count > 0 else 0
