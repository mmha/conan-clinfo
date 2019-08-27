cmake_minimum_required(VERSION 3.7)
project(clinfo LANGUAGES C)

include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
conan_basic_setup()

set(THREADS_PREFER_PTHREAD_FLAG ON)

find_package(OpenCL REQUIRED)
find_package(Threads REQUIRED)

add_executable(clinfo source_subfolder/src/clinfo.c)
target_include_directories(clinfo PRIVATE src)
target_link_libraries(clinfo OpenCL::OpenCL Threads::Threads ${CMAKE_DL_LIBS})

install(TARGETS clinfo RUNTIME DESTINATION bin)
