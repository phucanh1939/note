#!/usr/bin/env python3
import os
import re
import shutil
from pathlib import Path

def camel_to_kebab(name):
    """Convert CamelCase to kebab-case"""
    # Handle acronyms like HTTP, HTTPS, IP, TCP, UDP
    name = re.sub(r'([a-z])([A-Z])', r'\1-\2', name)
    # Handle sequences like HTTPSConnection → https-connection
    name = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', name)
    return name.lower()

def remove_numeric_prefix(name):
    """Remove numeric prefixes like 01_, 02_, 01., 02. etc"""
    # Remove patterns like 01_, 02_, 01., 02., etc.
    name = re.sub(r'^\d+[._\s]+', '', name)
    return name

def normalize_name(name):
    """Normalize a folder/file name to lowercase-kebab-case"""
    # First remove numeric prefix
    name = remove_numeric_prefix(name)
    # Then convert camel case to kebab case
    name = camel_to_kebab(name)
    return name

def extract_title(filepath):
    """Extract a nice title from the file path"""
    filename = Path(filepath).stem
    # Convert kebab-case to Title Case
    words = filename.split('-')
    title = ' '.join(word.capitalize() for word in words)
    return title

def add_frontmatter(filepath):
    """Add frontmatter to markdown file if it doesn't exist"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if frontmatter already exists
    if content.startswith('---'):
        return
    
    title = extract_title(filepath)
    frontmatter = f"---\ntitle: {title}\n---\n\n"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    print(f"Added frontmatter to: {filepath}")

def rename_path(old_path, new_path):
    """Safely rename a path"""
    if old_path != new_path:
        if os.path.exists(new_path):
            print(f"Warning: {new_path} already exists, skipping")
            return False
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} → {new_path}")
        return True
    return True

def process_directory(root_dir):
    """Process all directories and files"""
    docs_dir = Path(root_dir)
    
    # First pass: rename directories from deepest to shallowest
    all_dirs = []
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            all_dirs.append(full_path)
    
    # Sort by depth (deepest first)
    all_dirs.sort(key=lambda x: x.count(os.sep), reverse=True)
    
    # Rename directories
    for old_dir in all_dirs:
        if 'images' in old_dir:  # Skip images directories
            continue
        
        dir_name = os.path.basename(old_dir)
        parent_dir = os.path.dirname(old_dir)
        new_name = normalize_name(dir_name)
        
        if new_name != dir_name:
            new_dir = os.path.join(parent_dir, new_name)
            rename_path(old_dir, new_dir)
    
    # Second pass: rename files and add frontmatter
    for dirpath, dirnames, filenames in os.walk(docs_dir):
        # Skip images directories
        if 'images' in dirpath:
            continue
        
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            
            if filename.endswith('.md'):
                # Rename file
                new_filename = normalize_name(filename)
                if new_filename != filename:
                    new_path = os.path.join(dirpath, new_filename)
                    rename_path(old_path, new_path)
                    old_path = new_path
                
                # Add frontmatter
                add_frontmatter(old_path)
    
    print("\n✓ Refactoring complete!")

if __name__ == '__main__':
    docs_path = '/Users/user/personal/note/docs'
    process_directory(docs_path)
