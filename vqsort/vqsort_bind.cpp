#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

#include "hwy/contrib/sort/vqsort.h"

namespace py = pybind11;

template <typename T>
void sort_array(
    py::array_t<T, py::array::c_style | py::array::forcecast> arr,
    const bool reverse
) {
    py::buffer_info buf = arr.request();

    if (buf.ndim != 1) {
        throw py::value_error("Only 1-D arrays are supported");
    }

    T* data = static_cast<T*>(buf.ptr);
    const size_t data_size = static_cast<size_t>(buf.shape[0]);

    py::gil_scoped_release release;

    if (reverse) {
        void (*vqsort_fn)(T*, size_t, hwy::SortDescending) = &hwy::VQSort;
        vqsort_fn(data, data_size, hwy::SortDescending{});
    }
    else {
        void (*vqsort_fn)(T*, size_t, hwy::SortAscending) = &hwy::VQSort;
        vqsort_fn(data, data_size, hwy::SortAscending{});
    }
}

void sort_array_f16(
    py::array_t<uint16_t, py::array::c_style> arr,
    const bool reverse
) {
    py::buffer_info buf = arr.request();

    if (buf.ndim != 1) {
        throw py::value_error("Only 1-D arrays are supported");
    }

    hwy::float16_t* data = reinterpret_cast<hwy::float16_t*>(buf.ptr);
    const size_t data_size = static_cast<size_t>(buf.shape[0]);

    py::gil_scoped_release release;

    if (reverse) {
        hwy::VQSort(data, data_size, hwy::SortDescending{});
    }
    else {
        hwy::VQSort(data, data_size, hwy::SortAscending{});
    }
}

PYBIND11_MODULE(vqsort_bind, m) {
    // int8/uint8 are not supported for SIMD architectural reasons
    // see vqsort.h inside of highway
    m.def("sort_i16",  &sort_array<int16_t>);
    m.def("sort_u16",  &sort_array<uint16_t>);
    m.def("sort_i32",  &sort_array<int32_t>);
    m.def("sort_i64",  &sort_array<int64_t>);
    m.def("sort_u32", &sort_array<uint32_t>);
    m.def("sort_u64", &sort_array<uint64_t>);
    m.def("sort_f16", &sort_array_f16);
    m.def("sort_f32", &sort_array<float>);
    m.def("sort_f64", &sort_array<double>);
}