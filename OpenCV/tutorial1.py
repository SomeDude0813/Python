import cv2 as cv
import numpy as np

haystack_img = cv.imread('OpenCV/albion_farm.jpg', cv.IMREAD_UNCHANGED)
needle_img = cv.imread('OpenCV/albion_cabbage.jpg', cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED) # search the img for all match values

#cv.imshow('Result', result)
#cv.waitKey()

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result) # get the best match position

print('Best match confidence: %s' % str(max_loc))

threshold = 0.8
if max_val >= threshold:
    print("found")
    
    needle_w = needle_img.shape[0]
    needle_h = needle_img.shape[1] # get width and height of target img
    
    top_left = max_loc
    bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
    
    cv.rectangle(haystack_img, top_left, bottom_right,
                    color=(0, 255, 0), thickness=2, lineType=cv.LINE_4) # outline the best match
    
    cv.imshow('Result', haystack_img)
    cv.waitKey(5000)
else:
    print("not found")