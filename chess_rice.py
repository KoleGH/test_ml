vt = 0
for i in range(64):
    v = pow(2, i)
    print('field:', i, 'grains', v)
    vt = vt+v
print('total grains:', vt)
print('kgs of rice:', vt/30000)
print('millions of tons of rice:', vt/30000000000000)
