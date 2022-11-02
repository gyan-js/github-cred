from matplotlib import pyplot

from matplotlib.image import imread

infected_testing_image = 'D:/Kunal Programming/Python/github-cred/image_augmentation/PRO-M3-Pneumothorax-Image-Dataset/training_dataset/infected/image_1.png'

image = imread(infected_testing_image)

pyplot.title('Testing Image')

pyplot.imshow(image)

pyplot.show()

# Access images from : 'https://drive.google.com/drive/folders/1O867tnPsbCKBd-twqsYtTcykr-daAtns?usp=share_link'
