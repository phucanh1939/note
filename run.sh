#!/bin/bash

# Define paths
SOURCE="./playground/main.cpp"
OUTPUT="./playground/main_exec"

# 1. Compile the code using clang++ (enabling C++20 and common warnings)
echo "Compiling $SOURCE with clang++..."
clang++ -std=c++20 -Wall "$SOURCE" -o "$OUTPUT"

# 2. Check if compilation succeeded before running
if [ $? -eq 0 ]; then
    echo -e "Compilation successful!\nRunning program...\n-------------------"
    
    # Execute the program
    "$OUTPUT"
    
    echo -e "\n-------------------"
else
    echo "Compilation failed. Fix the errors above and try again."
fi