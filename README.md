# vqsort
Sort arrays with SIMD vqsort in Python

VQSort supports 16,32,64 bit numeric types (signed/unsigned integer and floats).

```python
import vqsort
import numpy as np

arr = np.random.randint(0, 1000, size=[100000], dtype=np.uint32)

 # still need to assign in case type is not supported by vqsort such as 8-bit
arr = vqsort.sort(arr, in_place=True)
```

After testing on Apple Silicon M3, floats show an advantage, integers do not.