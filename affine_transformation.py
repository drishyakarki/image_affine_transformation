from PIL import Image
import numpy as np
import math


def matrix_multiplication(matrix, vector):
    
    result = [0, 0, 0]
    
    for i in range(3):
        for j in range(3):
            result[i] += matrix[i][j] * vector[j]
    
    return result


def new_arr(array):
    
    shape = array.shape
    dtype = array.dtype
    
    zeros_array = np.zeros(shape, dtype)
    
    return zeros_array


def apply_translation(image, tx, ty):
    
    image_array = np.array(image)
    
    rows, cols, channels = image_array.shape
    
    translated_image = new_arr(image_array)
    translation_matrix = np.array([[1, 0, tx],
                                   [0, 1, ty],
                                   [0, 0, 1]])

    for i in range(rows):
        for j in range(cols):
            translated_coords = matrix_multiplication(translation_matrix, [j, i, 1])

            translated_x = int(translated_coords[0])
            translated_y = int(translated_coords[1])

            if 0 <= translated_x < cols and 0 <= translated_y < rows:
                translated_image[translated_y, translated_x] = image_array[i, j]

    return translated_image


def apply_rotation(image, angle_degree):
    
    rads = math.radians(angle_degree)
    cx, cy = (image.width // 2, image.height // 2)
    
    height_rot_img = round(abs(image.height * math.sin(rads))) + round(abs(image.width * math.cos(rads)))
    width_rot_img = round(abs(image.width * math.cos(rads))) + round(abs(image.height * math.sin(rads)))
    
    rot_img = Image.new("RGB", (width_rot_img, height_rot_img))
    
    midx, midy = (width_rot_img // 2, height_rot_img // 2)
    
    for i in range(rot_img.height):
        for j in range(rot_img.width):
            
            x = (i - midx) * math.cos(rads) + (j - midy) * math.sin(rads)
            y = -(i - midx) * math.sin(rads) + (j - midy) * math.cos(rads)
            x = round(x) + cy
            y = round(y) + cx
    
            if 0 <= x < image.height and 0 <= y < image.width:
                rot_img.putpixel((j, i), image.getpixel((y, x)))
    
    return rot_img


def apply_shearing(image, shear_x, shear_y):
    
    image = np.array(image)
    
    rows, cols, channels = image.shape
    
    new_cols = int(cols + abs(shear_x) * rows)
    new_rows = int(rows + abs(shear_y) * cols)
    
    sheared_image = np.zeros((new_rows, new_cols, channels), dtype = np.uint8)
    
    for i in range(rows):
        for j in range(cols):
            sheared_x = int(j + shear_x * i)
            sheared_y = int(i + shear_y * j)
            
            if 0 <= sheared_x < new_cols and 0 <= sheared_y < new_rows:
                sheared_image[sheared_y, sheared_x] = image[i, j]
                
    return sheared_image


def apply_vertical_reflection(image):
    
    width, height = image.size
    reflected_image = Image.new("RGB", (width, height))
    
    for y in range(height):
        for x in range(width):
            original_pixel = image.getpixel((x, y))
            reflected_x = x
            reflected_y = height - y - 1
            reflected_image.putpixel((reflected_x, reflected_y), original_pixel)
            
    return reflected_image


def apply_horizontal_reflection(image):
    
    width, height = image.size
    reflected_image = Image.new("RGB", (width, height))
    
    for y in range(height):
        for x in range(width):
            original_pixel = image.getpixel((x, y))
            reflected_x = width - x - 1
            reflected_y = y
            reflected_image.putpixel((reflected_x, reflected_y), original_pixel)
            
    return reflected_image


image = Image.open("check.png")

rotated_image = apply_rotation(image, 45)
rotated_image.show()

translated_image = apply_translation(image, 100, 100)
translated_image = Image.fromarray(translated_image)
translated_image.show()

sheared_image = Image.fromarray(apply_shearing(image, 0.3, 0.5))
sheared_image.show()

vertical_reflected_image = apply_vertical_reflection(image)
vertical_reflected_image.show()

horizontal_reflected_image = apply_horizontal_reflection(image)
horizontal_reflected_image.show()
