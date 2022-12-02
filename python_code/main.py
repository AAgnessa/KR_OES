import part1
import calibration
#input = '00000002_0000000049F36E0C.bmp'
#a = part1.find_rgb_pixels(input)
#a = part1.colored_spot(input)
#for i in range(3):
#    print(*a[i])
path = './images/*.bmp'
cal_res = calibration.calibration(path)
path = 'forcalib.bmp'
newcameramatrix = calibration.undistortion(cal_res, path)
pass
#part1.show(a, input)