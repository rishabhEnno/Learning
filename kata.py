def func_wardrobe():
#  50a + 75b + 100c + 120d = 250
# # 120 not possible
#  25(2a + 3b + 4c) = 250
#  2a + 3b + 4c = 10
#  2(a + 2c) + 3b = 10
# 3b --> even and 3b<10 --> b = 0, 2
# if b = 0
#   a + 2c = 5
#   a,c = (5, 0), (3, 1), (1, 2)
#  ((5,0, 0), (3, 0, 1), (1, 0, 2)
# if b = 2
#   a + 2c = 2
#   a,c = 0, 1   a,c = 2,0
# (0, 2, 1), (2, 2, 0)
# 
    possibilities = [(5,0, 0), (3, 0, 1), (1, 0, 2), (0, 2, 1), (2, 2, 0)]
    out = []
    for p in possibilities:
        a = [50]*p[0]
        b = [75]*p[1]
        c = [100]*p[2]
        out.append(a+b+c)
    return out


if __name__ == "__main__":
    print(func_wardrobe())