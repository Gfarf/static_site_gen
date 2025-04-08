from files import walk_path, clear_dir, copy_files
import os
from pathlib import Path
from pagemake import generate_page_recursive



ROOT = os.getcwd()
SOURCE = ROOT + "/static"
DESTINATION = ROOT + "/public"

def main():

    if os.path.exists(Path(DESTINATION)):
        clear_dir(DESTINATION)
    copy_files(SOURCE, DESTINATION)
    generate_page_recursive("./content", "./template.html", "./public")



if __name__ == "__main__":
    main()

