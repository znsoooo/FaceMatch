import glob
import cv2

for path in glob.glob('imgs/*'):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    cv2.imwrite(path, img)
