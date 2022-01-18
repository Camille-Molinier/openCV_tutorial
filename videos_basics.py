import cv2
import os
import matplotlib.pyplot as plt

os.system('cls')

save_path = os.path.join('data', 'output', 'Lesson_2')

################## Setup a capture #################
cap = cv2.VideoCapture('./data/videos/PIZZA.mp4')

ret, frame = cap.read()

plt.figure()
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.savefig(f'{save_path}/frame.jpg')

# realease capture
# cap.release()

################ Capture properties ################
# Heigth
heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Width
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# Number of Frames
nb_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# FPS
fps = cap.get(cv2.CAP_PROP_FPS)

print(f'Number of frames  : {nb_frames}')
print(f'Frames per second : {fps}')
print(f'Duration          : {round((nb_frames/fps) ,4)}')
print(f'Height of frames  : {heigth}')
print(f'Width of frames   : {width}')

################ Working with videos ###############
# for frame_idx in range(int(nb_frames)) :
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow(f'{save_path}/Video_player', gray)

#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

################ Writing out videos ################
# see : https://www.fourcc.org/pim1/
videoWriter = cv2.VideoWriter(f'{save_path}/output.avi', cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), fps, (width, heigth))

for frame_idx in range(int(nb_frames)) :
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow(f'{save_path}/Video_player', gray)
    videoWriter.write(frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
videoWriter.release()
