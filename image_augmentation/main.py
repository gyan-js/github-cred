from matplotlib import pyplot
from matplotlib.image import imread

sample_images = 'D:/Kunal Programming/Python/github-cred/image_augmentation/PRO-M3-Pneumothorax-Image-Dataset/training_dataset/infected/image_1.png'

image = imread(sample_images)

pyplot.title('Testing Image')

pyplot.imshow(image)

