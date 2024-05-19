import numpy as np
import matplotlib.pyplot as plt


def read_binary_image(file_path):
    # Read binary image from file
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Convert binary data to NumPy array
    image_array = np.frombuffer(binary_data, dtype=np.uint8)

    return image_array


def apply_neighbouring_padding(image_array, width, height):
    # Reshape the 1D array to 2D array with the specified width and height
    original_image = image_array.reshape((height, width))

    # Create a new padded image with one-pixel padding using neighbouring pixel values
    padded_image = np.pad(original_image, 1, mode="edge")

    return padded_image


def draw_histogram(image_array):
    # Flatten the image array for histogram calculation
    flattened_image = image_array.flatten()

    # Plot histogram
    plt.hist(flattened_image, bins=range(256), color="gray", alpha=0.7)
    plt.title("Image Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.show()


def main():
    # Replace 'path/to/your/image.bin' with the path to your binary image file
    image_file_path = "path/to/your/image.bin"

    # Replace with the width and height of your image
    image_width = 256
    image_height = 256

    # Read binary image
    image_data = read_binary_image(image_file_path)

    # Apply neighbouring pixel value padding
    padded_image = apply_neighbouring_padding(image_data, image_width, image_height)

    # Draw histogram of the padded image
    draw_histogram(padded_image)


if __name__ == "__main__":
    main()
