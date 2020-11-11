import cv2

def main():
    imgpath = "C:\\Users\koza\Documents\GitHub\moocs\youtube\opencv_3_with_python_3_tutorial\standard_test_images\lena_color_256.tif"
    img = cv2.imread(imgpath)
    cv2.imshow("Lena", img)
    cv2.waitKey(0)
    cv2.destoryAllWindows()

if __name__ == "__main__":
    main()