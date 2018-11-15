from pathlib import Path
import numpy as np
import imageio
import math


def load_images_from(folder_path, verbose=False):
  """
    Load all images to a numpy.Array

    Return: An array of numpy.Array
  """
  p = Path(folder_path)

  dirs = [d for d in p.iterdir() if d.is_dir()]

  images = []

  if verbose:
    counter = 0
    total = len(dirs)

  for d in dirs:
    images.extend(
      # Maps image path to a numpy array using the imread function
      map(lambda img: imageio.imread(img), d.iterdir()))

    if verbose:
      counter += 1
      print("[{}%] Loaded folder {}".format(
        math.floor((counter/total) * 100), d))
  return images


if __name__ == '__main__':
  images = load_images_from('./data', verbose=True)

  # Print the shape of the first 10 images
  for i in range(0, 10):
    print(images[i].shape)
