from pathlib import Path
import numpy as np
import imageio
import math
import pandas as pd
import itertools
import re


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


def load_defect_info(path):
  """
    Load the defect info file

    Return: pandas.DataFrame
  """
  p = Path(path)

  if not p.is_file():
    raise RuntimeError("The path provided isn't a file")

  # id (x_die, y_die) x_loc y_loc x_size y_size d_size n_size
  regex = r"^(\d+) *\((\d+) *, *(-?\d+)\) *\((-?\d+.\d+) *, *(-?\d+.\d+)\) *(\d+.\d+) *(\d+.\d+) *(\d+.\d+) *(\d+.\d+)"

  data = []
  with open(path, "r") as file:
    for idx, line in enumerate(itertools.islice(file, 3, None)):

      matches = re.match(regex, line)

      # Check if the regex matching function worked
      if not matches:
        print("Couldn't match line {}".format(idx))
        continue

      num_of_groups = len(matches.groups())

      if num_of_groups < 9:
        print("Couldn't match line {}".format(idx))
        continue

      data.append(list(map(lambda it: float(it), matches.groups())))

  return pd.DataFrame(data=data, columns=[
    "site_id", "x_die", "y_die", "x_loc", "y_loc", "x_size", "y_size", "d_size",
    "n_size"])


if __name__ == '__main__':
  # images = load_images_from('./data', verbose=True)

  # # Print the shape of the first 10 images
  # for i in range(0, 10):
  #   print(images[i].shape)

  df = load_defect_info("./DefectsINfo.txt")
