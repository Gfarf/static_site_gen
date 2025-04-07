from files import walk_path, clear_dir, copy_files
import os




ROOT = os.getcwd()
SOURCE = ROOT + "/static"
DESTINATION = ROOT + "/public"

def main():
    
    clear_dir(DESTINATION)
    os.rmdir(DESTINATION)
    os.mkdir(DESTINATION)
    copied_files = copy_files(SOURCE, DESTINATION)
    print(copied_files)



if __name__ == "__main__":
    main()

