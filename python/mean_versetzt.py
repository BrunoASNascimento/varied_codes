b = -10.6
c = -10.9


def versetzt(b, c):
    num_1 = 1/(3*c)
    num_2 = 2/(3*b)
    media = 2 / (num_1+num_2)
    return media


f = versetzt(c, b)

print("f = {:.2f}".format(f))
