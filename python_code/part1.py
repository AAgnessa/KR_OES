def find_rgb_pixels(path):
    #эта функция используется для нахождения координат трех самых цветных пикселя на фотографии
    #заданные цвета: красный, синий, желтный
    import cv2; import numpy as np
    image = cv2.imread(path)
    intensity = [0, 0, 0]
    #opencv читает изображения в формате BGR. Для обработки изображения создадим массив I путем перевода image в RGB
    #можно работать и так, но RGB привычнее
    I = np.array(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), dtype = float, copy = True)
    for i in range(len(I)):
        for j in range(len(I[1])):
            #ищем координаты пикселя, который ближе всего подходит под красный цвет, путем сравнения соотношения цветов
            #в трех каналах по всем пикселям
            if (I[i][j][0] / (I[i][j][1] + I[i][j][2] + 255)) > intensity[0]:
                intensity[0] = I[i][j][0] / (I[i][j][1] + I[i][j][2] + 255)
                red_coord = [i, j]
            # аналогично для синего
            if (I[i][j][2] / (I[i][j][0] + I[i][j][1] + 255)) > intensity[1]:
                intensity[1] = I[i][j][2] / (I[i][j][0] + I[i][j][1] + 255)
                blue_coord = [i, j]
            # для желтого пикселя формула немного отличается, т.к. желтый в RGB  это смесь красного и зеленого
            if ((I[i][j][0] + I[i][j][1]) / (2 * I[i][j][2] + 510)) > intensity[2]:
                intensity[2] = (I[i][j][0] + I[i][j][1]) / (2 * I[i][j][2] + 510)
                yellow_coord = [i, j]

    output = [['"Самый красный" пиксель:', red_coord], ['"Самый синий" пиксель:', blue_coord],\
             ['"Самый желтый" пиксель:', yellow_coord]]
    return(output)

def colored_spot(path):
    import cv2
    import numpy as np
    output = {}
    xy = [0, 0]
    image = cv2.imread(path)
    I = np.array(cv2.cvtColor(image, cv2.COLOR_BGR2HSV), copy=True)

    lower_red = np.array([0, 85, 105])
    upper_red = np.array([8, 255, 255])
    lower_blue = np.array([150, 50, 50])
    upper_blue = np.array([175, 255, 255])
    lower_yellow = np.array([12, 100, 100])
    upper_yellow = np.array([17, 255, 255])


    image = cv2.inRange(I, lower_red, upper_red)
    moments = cv2.moments(image, 1)
    x_moment = moments['m01']
    y_moment = moments['m10']
    area = moments['m00']
    if area > 20:
        xy[0] = int(x_moment / area)
        xy[1] = int(y_moment / area)
    output['Красный'] = xy
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image = cv2.inRange(I, lower_blue, upper_blue)
    moments = cv2.moments(image, 1)
    x_moment = moments['m01']
    y_moment = moments['m10']
    area = moments['m00']
    xy[0] = int(x_moment / area)
    xy[1] = int(y_moment / area)
    output['Синий'] = xy
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    image = cv2.inRange(I, lower_yellow, upper_yellow)
    moments = cv2.moments(image, 1)
    x_moment = moments['m01']
    y_moment = moments['m10']
    area = moments['m00']
    xy[0] = int(x_moment / area)
    xy[1] = int(y_moment / area)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    output['Желтый'] = xy
    return output

    #cv2.imshow("Image", image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()



def show(coord, path):
    #функция выводит изображение на экран и обводит найденные find_rgb_pixels() пиксели
    #используется для проверки корректности работы find_rgb_pixels()
    import cv2
    image = cv2.imread(path)
    #найденные пиксели обводятся кругами для ручной проверки изображения
    #красный:
    cv2.circle(image, (coord['Красный'][1], coord['Красный'][0]), len(image)//80, (0, 0, 255), 3)
    #синий:
    cv2.circle(image, (coord['Синий'][1], coord['Синий'][0]), len(image)//80, (255, 0, 0), 3)
    # желтый:
    cv2.circle(image, (coord['Желтый'][1], coord['Желтый'][0]), len(image)//80, (0, 255, 255), 3)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
