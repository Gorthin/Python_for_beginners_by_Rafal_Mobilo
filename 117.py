import math

degree = 360
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))

degree = 45
radian = degree * math.pi / 180
print("%d degree is %f radians" % (degree, radian))
print('')

print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))

print("============")

small_r = 0.22
big_r = 0.27
family_r = 0.38

small_price = 11.5
big_price = 15.6
family_price = 22.0

small_area = math.pi * small_r**2
big_area = math.pi * big_r**2
family_area = math.pi * family_r**2

print('small', small_r, small_price, small_area)
print('big', big_r, big_price, big_area)
print('family', family_r, family_price, family_area)
print('')
print('small', small_price / small_area)
print('big', big_price / big_area)
print('family', family_price / family_area)
print('')

math_ls = dir(math)
print(math_ls)