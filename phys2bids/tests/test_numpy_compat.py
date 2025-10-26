import numpy as np
from phys2bids import some_module  # replace with actual module if needed

def test_array_creation_dtype():
    arr = np.array([1,2,3], dtype=int)
    assert arr.dtype == np.int64 or np.issubdtype(arr.dtype, np.integer)
