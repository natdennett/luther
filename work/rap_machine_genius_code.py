import os
import pickle
from collections import namedtuple

Song = namedtuple('Song', ['header', 'verified', 'metadata', 'lyrics'])

def read_pickle(path):

    """Loads an object that was pickled at the given path.
    If there's nothing at that path, the function will not proceed.

    Args:
      path (string): the path to the pickle file.

    Returns:
      The pickled object."""

    if os.path.isfile(path):
        with open(path, 'rb') as file:
            return pickle.load(file)
    else:
        print(f"{path} is not a valid path. Try again.")

def write_pickle(obj, path):

    """Pickles an object to the given path. If there's already a pickle at that
    path, the function won't overwrite it.

    Args:
      obj: the object we want to pickle.
      path (string): the path where we want to pickle obj.

    Returns:
      Nothing."""

    if not os.path.isfile(path):
        with open(path, 'wb') as file:
            pickle.dump(obj, file)
    else:
        print(f"Pickling aborted because {path} is already a file.")
