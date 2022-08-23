def find_rgb_pixels(path):
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

def show_rgb_pixels(coord, path):
    image = cv2.imread(path)
    #найденные пиксели обводятся кругами для ручной проверки изображения
    #красный:
    cv2.circle(image, (coord[0][1][0], coord[0][1][1]), len(I)//80, (0, 0, 255), 3)
    #синий:
    cv2.circle(image, (coord[1][1][0], coord[1][1][1])), len(I)//80, (255, 0, 0), 3)
    # желтый:
    cv2.circle(image, (coord[2][1][0], coord[2][1][1])), len(I)//80, (0, 255, 255), 3)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
