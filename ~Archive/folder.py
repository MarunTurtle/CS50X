import os
import shutil

def write_directory_structure(base_path, output_file):
    ignore_dirs = {'static', 'templates'}
    
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(base_path):
            # Exclude hidden directories and specified directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
            level = root.replace(base_path, '').count(os.sep)
            indent = ' ' * 4 * (level)
            f.write('{}{}/\n'.format(indent, os.path.basename(root)))

def copy_readme_files(base_path, output_base_path):
    ignore_dirs = {'static', 'templates'}
    
    for root, dirs, files in os.walk(base_path):
        # Exclude hidden directories and specified directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ignore_dirs]
        for file in files:
            if file.lower() == 'readme.md':
                folder_name = os.path.basename(root)
                new_file_name = f"{folder_name}_README.md"
                new_file_path = os.path.join(output_base_path, new_file_name)
                shutil.copyfile(os.path.join(root, file), new_file_path)

def main():
    base_path = r'C:\Users\SSAFY\Desktop\CS50X'
    output_file = r'C:\Users\SSAFY\Desktop\CS50X_TableOfContents.md'
    output_base_path = r'C:\Users\SSAFY\Desktop'

    # Write the directory structure to the markdown file
    write_directory_structure(base_path, output_file)
    
    # Copy README.md files and rename them
    copy_readme_files(base_path, output_base_path)

if __name__ == "__main__":
    main()
