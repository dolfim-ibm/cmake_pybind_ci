#!/usr/bin/env python

import os

import sys

import subprocess
from typing import List
import pybind11

ROOT_DIR = os.path.abspath("./")
BUILD_DIR = os.path.join(ROOT_DIR, "build")

def get_pybind11_cmake_args():
        pybind11_sys_path = os.getenv("PYBIND11_SYSPATH")
        if pybind11_sys_path:
            # pybind11_include_dir = os.path.join(pybind11_sys_path, "include")
            pybind11_cmake_dir = os.path.join(pybind11_sys_path, "share", "cmake", "pybind11")
        else:
            # pybind11_include_dir = pybind11.get_include()
            pybind11_cmake_dir = pybind11.get_cmake_dir()
        # print(f"{pybind11_include_dir=}")
        print(f"{pybind11_cmake_dir=}")
        return [f"-Dpybind11_DIR={pybind11_cmake_dir}"]

def run(cmd: List[str], cwd: str="./"):

    print_cmd = " ".join(cmd)
    print(f"\nlaunch: {print_cmd}")

    message = subprocess.run(cmd, cwd=cwd)

    if "returncode=0" in str(message):
        print(f" -> SUCCESS")
        return True

    print(f" -> ERROR with message: '{message}'\n")
    return False


def build_local(num_threads: int):

    print("python prefix: ", sys.exec_prefix)
    print("python executable: ", sys.executable)
    config_cmd = [
        "cmake",
        "-B", f"{BUILD_DIR}",
        f"-DPython3_ROOT_DIR={sys.exec_prefix}",
        f"-DPython3_FIND_STRATEGY=LOCATION",
    ]
    config_cmd.extend(get_pybind11_cmake_args())
    success = run(config_cmd, cwd=ROOT_DIR)
    if not success:
        raise RuntimeError("Error building.")


if "__main__" == __name__:
    num_threads = int(os.getenv("BUILD_THREADS", "4"))
    build_local(num_threads=num_threads)
