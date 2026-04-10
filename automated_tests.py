import pytest

import numpy as np
import vqsort

DTYPES = [
	np.int8, np.int16, np.int32, np.int64,
	np.uint8, np.uint16, np.uint32, np.uint64,
	np.float16, np.float32, np.float64,
]

@pytest.mark.parametrize("size", [0, 1, 2, 10, 100, 1_000_000])
@pytest.mark.parametrize("dtype", DTYPES)
def test_sorting(size, dtype):
	if np.dtype(dtype).kind == 'f':
		maximum = int(1e10)
		data = np.random.randint(0, maximum, size=[size], dtype=np.uint64).astype(dtype)
	else:
		maximum = np.iinfo(dtype).max
		data = np.random.randint(0, maximum, size=[size], dtype=dtype)

	data = vqsort.sort(data)
	vqsorted = np.copy(data)
	data.sort()
	assert np.all(data == vqsorted)


