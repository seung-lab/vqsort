cmake_minimum_required(VERSION 3.21)
project(vqsort_bind CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# --- pybind11 ---
# scikit-build-core makes pybind11 available automatically
find_package(pybind11 CONFIG REQUIRED)

# --- Highway ---
# Disable Highway's tests/benchmarks — you only want the library
set(HWY_ENABLE_TESTS OFF CACHE BOOL "" FORCE)
set(HWY_ENABLE_EXAMPLES OFF CACHE BOOL "" FORCE)
set(HWY_ENABLE_CONTRIB ON CACHE BOOL "" FORCE)   # needed for vqsort

add_subdirectory(third_party/highway)

# --- Your extension ---
pybind11_add_module(vqsort_bind vqsort/vqsort_bind.cpp)

target_link_libraries(vqsort_bind PRIVATE hwy hwy_contrib)

target_compile_definitions(vqsort_bind PRIVATE
    "HWY_BASELINE_TARGETS=(HWY_SSE4|HWY_NEON)"
    "HWY_BROKEN_TARGETS=(HWY_SSE2|HWY_SSSE3)"
)

# Install the extension into the wheel
install(TARGETS vqsort_bind DESTINATION .)