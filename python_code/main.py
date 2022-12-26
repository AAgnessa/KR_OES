import part1
import calibration
import math
import numpy as np

def fun(X):
    f0 = X[0] ** 2 + X[1] ** 2 + X[2] ** 2
    f1 = X[3] ** 2 + X[4] ** 2 + X[5] ** 2
    f2 = X[6] ** 2 + X[7] ** 2 + X[8] ** 2
    f3 = P0[0] - X[9] - (P0[2] - X[11]) * ((X[0] * (-P01[0] + O11[0]) + X[1] * (P01[1] - O11[1]) - X[2] * f) /
                                           (X[6] * (-P01[0] + O11[0]) + X[7] * (P01[1] - O11[1]) - X[8] * f))
    f4 = P0[1] - X[10] - (P0[2] - X[11]) * ((X[3] * (-P01[0] + O11[0]) + X[4] * (P01[1] - O11[1]) - X[5] * f) /
                                            (X[6] * (-P01[0] + O11[0]) + X[7] * (P01[1] - O11[1]) - X[8] * f))
    f5 = P1[0] - X[9] - (P1[2] - X[11]) * ((X[0] * (-P11[0] + O11[0]) + X[1] * (P11[1] - O11[1]) - X[2] * f) /
                                           (X[6] * (-P11[0] + O11[0]) + X[7] * (P11[1] - O11[1]) - X[8] * f))
    f6 = P1[1] - X[10] - (P1[2] - X[11]) * ((X[3] * (-P11[0] + O11[0]) + X[4] * (P11[1] - O11[1]) - X[5] * f) /
                                            (X[6] * (-P11[0] + O11[0]) + X[7] * (P11[1] - O11[1]) - X[8] * f))
    f7 = P2[0] - X[9] - (P2[2] - X[11]) * ((X[0] * (-P21[0] + O11[0]) + X[1] * (P21[1] - O11[1]) - X[2] * f) /
                                           (X[6] * (-P21[0] + O11[0]) + X[7] * (P21[1] - O11[1]) - X[8] * f))
    f8 = P2[1] - X[10] - (P2[2] - X[11]) * ((X[3] * (-P21[0] + O11[0]) + X[4] * (P21[1] - O11[1]) - X[5] * f) /
                                            (X[6] * (-P21[0] + O11[0]) + X[7] * (P21[1] - O11[1]) - X[8] * f))
    return [f0, f1, f2, f3, f4, f5, f6, f7, f8]


def m_rot(a, b, g):
    m1 = np.array([math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1])
    m2 = np.array([math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)])
    m3 = np.array([1, 0, 0], [0, math.cos(g), -math.sin(g)], [0, math.sin(g), math.cos(g)])
    return np.dot(m1, np.dot(m2, m3))


def c_rot(yaw, roll, pitch):
    return np.array([math.cos(yaw) * math.cos(pitch),
                     -math.sin(pitch) * math.cos(yaw) * math.cos(roll) + math.sin(yaw) * math.sin(roll),
                     math.sin(pitch) * math.cos(yaw) * math.sin(roll) + math.sin(yaw) * math.cos(roll)],
                    [math.sin(pitch), math.cos(pitch) * math.cos(roll), -math.cos(pitch) * math.sin(roll)],
                    [math.cos(yaw) * math.cos(pitch),
                     -math.sin(pitch) * math.cos(yaw) * math.cos(roll) + math.sin(yaw) * math.sin(roll),
                     math.sin(pitch) * math.cos(yaw) * math.sin(roll) + math.sin(yaw) * math.cos(roll)])


# input = '00000002_0000000049F36E0C.bmp'
# a = part1.find_rgb_pixels(input)
# a = part1.colored_spot(input)
# for i in range(3):
#    print(*a[i])
path = './images/*.bmp'
cal_res = calibration.calibration(path)
path = 'forcalib.bmp'
newcameramatrix = calibration.undistortion(cal_res, path)
pass
# координаты на стенде
P0 = [-0.05, 0, -0.21]
P1 = [0, 0, 0]
P2 = [0.2, 0, 0.15]
# координаты на фото
P01 = [301, 843]
P11 = [914, 726]
P21 = [1278, 286]
f = (newcameramatrix[0][0] + newcameramatrix[1][1]) / 2
O11 = [newcameramatrix[0][2], newcameramatrix[1][2]]
a, b, g = [0, np.deg2rad(-90), np.deg2rad(90)]


M = m_rot(a, b, g)

pass


# part1.show(a, input)


