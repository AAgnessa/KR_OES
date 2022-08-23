import part1
a = part1.find_rgb_pixels('red_pixel.bmp')
for i in range(3):
    print(*a[i])
part1.show_rgb_pixels(a, 'red_pixel.bmp')