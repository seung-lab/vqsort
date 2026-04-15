import numpy as np
import time
import gc
import vqsort

def gbps(n, dtype, seconds, factor=2):
    bytes_moved = n * np.dtype(dtype).itemsize * factor
    return bytes_moved / seconds / 1e9

def bench_sort(fn, data):
    times = []
    for _ in range(3):
        arr = np.copy(data)
        t0 = time.perf_counter_ns()
        fn(arr)
        t1 = time.perf_counter_ns()
        times.append((t1 - t0) * 1e-9)
    return min(times)

gc.disable()

sizes = [
    100_000,
    300_000,
    1_000_000,
    3_000_000,
    10_000_000,
    30_000_000,
]

def run(dtype):
    print(np.dtype(dtype).name)
    print(f"{'N':>10} | {'numpy GB/s':>10} | {'vqsort GB/s':>10} | {'advantage':>10}")
    print("-" * 50)

    if np.issubdtype(dtype, np.floating):
        maximum = np.finfo(dtype).max
    else:
        maximum = np.iinfo(dtype).max

    for n in sizes:
        data = np.random.uniform(
            0, maximum, size=n,
        ).astype(dtype)

        # warm-up
        tmp = np.copy(data)
        tmp.sort()
        tmp = np.copy(data)
        vqsort.sort(tmp)

        t_np = bench_sort(lambda a: a.sort(), data)
        t_vq = bench_sort(lambda a: vqsort.sort(a), data)

        np_gb = gbps(n, np.uint64, t_np)
        vq_gb = gbps(n, np.uint64, t_vq)

        print(f"{n:10d} | {np_gb:10.2f} | {vq_gb:10.2f} | {vq_gb/np_gb:10.2f}x")

for dtype in [np.uint64, np.uint32, np.uint16, np.float64, np.float32, np.float16]:
    run(dtype)

gc.enable()