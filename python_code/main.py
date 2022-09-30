import part1
input = 'photo_2022-09-26_16-26-14.jpg'
#a = part1.find_rgb_pixels(input)
part1.colored_spot(input)
for i in range(3):
    print(*a[i])
part1.show(a, input)