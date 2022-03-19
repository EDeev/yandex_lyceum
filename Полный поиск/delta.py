def delta(org, adr):
    first = "0.0001"
    adr = list(map(float, adr.split(',')))

    k1 = float(first)
    while True:
        k = adr[0] + k1
        if org[0] + 0.001 >= k:
            k1 *= 10
        else:
            break

    k2 = float(first)
    while True:
        k = adr[1] + k2
        if org[1] + 0.001 >= k:
            k2 *= 10
        else:
            break

    return str(max(k1, k2))