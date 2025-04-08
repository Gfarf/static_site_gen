from files import walk_path, clear_dir, copy_files
import os
from pathlib import Path
from pagemake import generate_page_recursive
import sys

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    SOURCE = "./static"
    DESTINATION = "./docs"

    if os.path.exists(Path(DESTINATION)):
        clear_dir(DESTINATION)
    copy_files(SOURCE, DESTINATION)
    generate_page_recursive("./content", "./template.html", "./docs", basepath)



if __name__ == "__main__":
    main()

