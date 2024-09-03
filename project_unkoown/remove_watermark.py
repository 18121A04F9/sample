import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/kalya/Downloads/tiling.jpg')

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold to identify watermark (adjust threshold values as needed)
_, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Invert the mask to get the watermark area (if needed)
mask = cv2.bitwise_not(mask)

# Display the mask to check the detected area
cv2.imshow('Watermark Mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Function to replace watermark pixels with average surrounding color
def remove_watermark(image, mask):
    result = image.copy()
    height, width = mask.shape

    for i in range(1, height-1):
        for j in range(1, width-1):
            if mask[i, j] == 255:  # Watermark pixel
                # Get the neighboring pixels
                neighbors = image[i-1:i+2, j-1:j+2]
                # Compute the average color of neighboring pixels
                avg_color = np.mean(neighbors, axis=(0, 1))
                # Replace the watermark pixel with the average color
                result[i, j] = avg_color

    return result

res = remove_watermark(image, mask)

# Apply the function to remove watermark
for i in range(10):
    res = remove_watermark(res, mask)

# Display the final result
cv2.imshow('Watermark Removed', res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Save the result if needed
cv2.imwrite(r"C:\Users\kalya\Downloads\image_without_watermark.jpg", res)
