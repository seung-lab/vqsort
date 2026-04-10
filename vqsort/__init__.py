import numpy as np
import numpy.typing as npt

import vqsort_bind


def sort(
	arr:npt.NDArray[np.number],
	reverse:bool = False,
	in_place:bool = True,
) -> npt.NDArray[np.number]:
	"""
	Sort a 1D array of numbers using vqsort if possible.
	"""
	if arr.ndim != 1:
		raise TypeError(f"Only 1D arrays can be sorted.")
	elif arr.dtype.kind not in ('i', 'u', 'f'):
		raise TypeError("Only integers and floating point numbers can be sorted.")

	if not in_place:
		arr = np.copy(arr)

	if arr.dtype == np.int16:
		vqsort_bind.sort_i16(arr, reverse)
	elif arr.dtype == np.uint16:
		vqsort_bind.sort_u16(arr, reverse)
	elif arr.dtype == np.int32:
		vqsort_bind.sort_i32(arr, reverse)
	elif arr.dtype == np.int64:
		vqsort_bind.sort_i64(arr, reverse)
	elif arr.dtype == np.uint32:
		vqsort_bind.sort_u32(arr, reverse)
	elif arr.dtype == np.uint64:
		vqsort_bind.sort_u64(arr, reverse)
	elif arr.dtype == np.float16:
		vqsort_bind.sort_f16(arr.view(np.uint16), reverse)
	elif arr.dtype == np.float32:
		vqsort_bind.sort_f32(arr, reverse)
	elif arr.dtype == np.float64:
		vqsort_bind.sort_f64(arr, reverse)
	else:
		arr.sort()
		if reverse:
			arr = np.flip(arr)

	return arr

