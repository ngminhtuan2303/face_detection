from deepface import DeepFace
import matplotlib.pyplot as plt
detected_face = DeepFace.detectFace("data/img11.jpg")
plt.imshow(detected_face)