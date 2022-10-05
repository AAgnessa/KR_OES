import part1
input = '00000002_000000003F3A9543.bmp'
#a = part1.find_rgb_pixels(input)
a = part1.colored_spot(input)
#for i in range(3):
#    print(*a[i])
part1.show(a, input)