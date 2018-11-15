# UMASS RTEC Image Classification

## Task 1: Loading image

The idea is that we have a root folder (data). Inside we hace a list of folders
and each contains a list of images with arbitrary names. We can get the names of
the folders dynamically using one of python's built-in function (TBD). The following is the pseudocode to do this:

```python
  data_folder = python_function('./data')
  for folder in data_folder
    for img in folder
      # load image into a numpy array
      # using panadas.DataFrame, create an instance per image
```
