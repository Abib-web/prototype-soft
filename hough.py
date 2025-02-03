import cv2
import numpy as np

# Charger l'image
image = cv2.imread('images/image1.jpg', cv2.IMREAD_GRAYSCALE)

# Appliquer un filtre de Canny pour détecter les bords
edges = cv2.Canny(image, 50, 150)

# Appliquer la transformée de Hough
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

# Dessiner les lignes détectées
for line in lines:
    rho, theta = line[0]
    x1 = int(rho * np.cos(theta) - 1000 * np.sin(theta))
    y1 = int(rho * np.sin(theta) + 1000 * np.cos(theta))
    x2 = int(rho * np.cos(theta) + 1000 * np.sin(theta))
    y2 = int(rho * np.sin(theta) - 1000 * np.cos(theta))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('Lignes détectées', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
