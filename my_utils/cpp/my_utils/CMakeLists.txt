cmake_minimum_required(VERSION 3.10)
project(MyUtils)
include_directories(src)
file(GLOB SOURCES "src/*.cpp")
add_executable(my_program ${SOURCES})
