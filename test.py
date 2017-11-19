from PIL import Image
from PIL import ImageStat , ImageEnhance
import multiprocessing
from multiprocessing import Process
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


import math
# global brigthness add the new ones
global brigthness

# just backwards
def find_brightness(i):
    i = int(i)
    global brightness
    si = ''
    if (i < 10):
        si = '00' + str(i)
    elif (i < 100):
        si = '0' + str(i)
    else:
        si = str(i)

    img = Image.open('To_balance/frame-000' + si + '.jpg').convert('RGBA')
    stat = ImageStat.Stat(img)


    return (stat.mean[0])



def find_eigth_range_brigtness(i):
    global brigthness
    low = 0
    high = i
    i = int(i)
    if(i -50 >0):
        low = i-50
        high = i+1
    eigth_range = []
    eigth_range_average = 0
    for j in range(low,high):

        eigth_range.append(brigthness[j])
    for e in eigth_range:
        eigth_range_average += e
    eigth_range_average = eigth_range_average / len(eigth_range)
    return eigth_range_average

def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)


def fix_brigthness(i):
    global brigthness
    i_1 = int(i)
    i_2 = i_1 -1
    si1 = ''
    si2 = ''
    if (i_1 < 10):
        si1 = '00' + str(i_1)
    elif (i_1 < 100):
        si1 = '0' + str(i_1)
    else:
        si1 = str(i_1)
    if (i_2 < 10):
        si2 = '00' + str(i_2)
    elif (i_2 < 100):
        si2 = '0' + str(i_2)
    else:
        si2 = str(i_2)


    img2 = Image.open('To_balance/frame-000' + si1 + '.jpg').convert('RGBA')
    img1 = Image.open('To_balance/frame-000' + si2 + '.jpg').convert('RGBA')

    # matches difference
    # print('Difference in eighh ' + str(find_eigth_range_brigtness(i)))
    # print('Current Brigthness ' + str(ImageStat.Stat(img2).mean[0]))

    if((brigthness[i_1] >= 1.09*find_eigth_range_brigtness(i))):
        print(i)
        print('to match ' + str(ImageStat.Stat(img1).mean[0]))
        print('from match ' + str(ImageStat.Stat(img2).mean[0]))

        # enhancer = ImageEnhance.Brightness(img2)
        # img2 = enhancer.enhance((1+(((ImageStat.Stat(img1).mean[0] /ImageStat.Stat(img2).mean[0]))*15))/16 )
        # print('changed image brigthness to ' + str(ImageStat.Stat(img2).mean[0]))
        # enhancer = ImageEnhance.Contrast(img2)
        # tmpstac = ImageStat.Stat(img2)
        # # print(tmpstac._getextrema()[0][1])
        #
        # value = ((255  / tmpstac._getextrema()[0][1] ))
        # img2 = enhancer.enhance((1+value)/2)

        original = cv2.imread('To_balance/frame-000' + si1 + '.jpg')
        adjusted = adjust_gamma(original, gamma=((1.0+(((ImageStat.Stat(img1).mean[0] /ImageStat.Stat(img2).mean[0]))))/2))
        cv2.imwrite('To_balance/frame-000' + si1 + '.jpg', adjusted)
        time.sleep(2.5)
        img2 = Image.open('To_balance/frame-000' + si1 + '.jpg').convert('RGBA')
        brigthness[i] = ImageStat.Stat(img2).mean[0]
        print('check if changed the brigtness array ' + str(brigthness[i]))


        # statc = ImageStat.Stat(img2)
        # print(statc._getextrema()[0])
        # stat = ImageStat.Stat(img2)
        # print(stat.mean[0])
#
# def find_parts(img):
#     a = np.array(img.convert('L'))
#     b = a.sum(0)
#
#
#     plt.plot(b)
#     return b
#



# multi threading
if __name__ == '__main__':
    # img = Image.open('To_balance/frame-000023.jpg')
    # img1_array = find_parts(img1)
    # img2_array =find_parts(img2)
    global brigthness

    pool = multiprocessing.Pool(processes=8)
    result = pool.map(find_brightness, (('%d' % i) for i in range(600)))
    brigthness = result


    for e in range(1,600):

        fix_brigthness(e)
    # result2 = pool.map(fix_brigthness , (('%d' % e) for e in range(600)))

    # print(result)

    #
    # average_brigthness =0
    # #
    # for e in result:
    #     average_brigthness += e
    #
    #
    # average_brigthness = average_brigthness / len(result)
    #
    # print(average_brigthness)


# histogram


