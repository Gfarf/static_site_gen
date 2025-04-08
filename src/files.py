import os
import shutil
from pathlib import Path

def walk_path(origin: str) -> list:
    directories = os.listdir(origin)
    files = []
    inside_dir = []
    for dir in directories:
        final = Path(os.path.join(origin, dir))
        if final.is_file():
            files.append(final)
        else:
            inside_dir.insert(0, str(final))
            files.extend(walk_path(final)[0])
            
    return files, inside_dir

def del_files(files: list):
    for file in files:
        os.remove(file)

def del_folders(inside: list):
    print(f"deleting - {inside}")
    for dir in inside:
        print(f"deleting - {dir}")
        os.rmdir(dir)

def clear_dir(dir: str):
    # files, inside = walk_path(dir)
    # del_files(files)
    # del_folders(inside)
    shutil.rmtree(dir)

def copy_files(f_dir: str, t_dir: str):
    if not os.path.exists(Path(t_dir)):
        os.mkdir(t_dir)

    directories = os.listdir(f_dir)
    c_files = []
    for dir in directories:
        final = Path(os.path.join(f_dir, dir))
        if final.is_file():
            c_files.append(final)
            shutil.copy(final, t_dir)
        else:
            os.mkdir(t_dir+f"/{dir}")
            c_files.extend(copy_files(final,t_dir+f"/{dir}"))
            
    return c_files
