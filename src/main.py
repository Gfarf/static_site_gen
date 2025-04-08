from files import walk_path, clear_dir, copy_files
import os
from pathlib import Path
from pagemake import generate_page_recursive
import sys

def main():
    global ROOT 

    if len(sys.argv) > 1:
        ROOT = sys.argv[1]
    else:
        ROOT = "/"
    SOURCE = os.path.join(ROOT, "static")
    DESTINATION = os.path.join(ROOT, "docs")

    if os.path.exists(Path(DESTINATION)):
        clear_dir(DESTINATION)
    copy_files(SOURCE, DESTINATION)
    generate_page_recursive("content", "template.html", "docs", ROOT)



if __name__ == "__main__":
    main()

