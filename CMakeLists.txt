cmake_minimum_required(VERSION 3.12..3.26)

project(cmake_ci VERSION 1.0.0 LANGUAGES CXX C)
#set(CMAKE_VERBOSE_MAKEFILE off)

# ************************
# ***  cxx-flags       ***
# ************************

set(CMAKE_CXX_STANDARD          20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
# Python3_FIND_STRATEGY LOCATION

message(STATUS "Python executable: " ${Python3_EXECUTABLE})

