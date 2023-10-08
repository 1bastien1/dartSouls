#!/usr/bin/env python
 
import cv2
import sys

print( cv2.__version__ )


# Charger une image
image = cv2.imread('votre_image.jpg')

# Vérifier si l'image a été chargée correctement
if image is not None:
    # Convertir l'image en niveaux de gris
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Enregistrer l'image en niveaux de gris
    cv2.imwrite('image_grayscale.jpg', image_grayscale)

    # Afficher l'image en niveaux de gris
    cv2.imshow('Image en niveaux de gris', image_grayscale)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("L'image n'a pas pu être chargée.")
