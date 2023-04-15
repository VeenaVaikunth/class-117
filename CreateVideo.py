import os
import cv2

# vid = cv2.VideoCapture(0)

# if(vid.isOpened() == False):
 #   print("Unable to read the feed")

# height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(height)
# width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(width)
# fps = int(vid.get(cv2.CAP_PROP_FRAME_FPS))
# print(fps)

# while (True):
  #  read, frame = vid.read()
  # cv2.imshow("web cam", frame)
# if cv2.waitKey == 32:
  #   break
# vid.release()

path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path + "/" + file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter('project.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)