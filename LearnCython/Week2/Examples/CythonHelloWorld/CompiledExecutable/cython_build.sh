#!/bin/bash

CYTHON=$(which cython)
if [ "${CYTHON}" == "" ]; then
    echo "Cython command not found."
    exit 1
fi

GCC=$(which gcc)
if [ "${GCC}" == "" ]; then
    echo "Gcc command not found."
    exit 1
fi

INCLUDES=/usr/include/python3.4m
if [ ! -d ${INCLUDES} ]; then
    echo "${INCLUDES} headers can not be found."
    exit 1
fi

if [ ${#} -lt 1 ]; then
    echo "Usage: $(basename ${0}) <cython_files>"
    exit 1
fi

for cython_file in ${@}; do
    cython_file_basename=${cython_file%.*}
    c_file=${cython_file_basename}.c

    echo "Compiling ${cython_file} into ${c_file}"
    ${CYTHON} -a --embed ${cython_file} -o ${c_file}

    echo "Compiling ${c_file} into ${cython_file_basename}"
    ${GCC} -I${INCLUDES} ${c_file} -o ${cython_file_basename} -lpython3.4m
done
