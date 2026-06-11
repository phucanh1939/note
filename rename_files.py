#!/usr/bin/env python3
import os
import re
from pathlib import Path

def camel_to_kebab(name):
    """Convert CamelCase to kebab-case"""
    name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name)
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', name)
    return name.lower()

def normalize_name(name):
    """Normalize a file name to lowercase-kebab-case"""
    name = camel_to_kebab(name)
    return name

def rename_files(root_dir):
    """Rename all markdown files to lowercase-kebab-case"""
    docs_dir = Path(root_dir)
    
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        # Skip images directories
        if 'images' in dirpath:
            continue
        
        for filename in filenames:
            if filename.endswith('.md'):
                old_path = os.path.join(dirpath, filename)
                new_filename = normalize_name(filename)
                
                if new_filename != filename:
                    new_path = os.path.join(dirpath, new_filename)
                    
                    # Check if target already exists
                    if os.path.exists(new_path):
                        print(f"Skipping: {new_path} already exists")
                    else:
                        os.rename(old_path, new_path)
                        print(f"Renamed: {filename} → {new_filename}")
    
    print("\n✓ File renaming complete!")

if __name__ == '__main__':
    rename_files('/Users/user/personal/note/docs')
