from htmlfromblocks import *
from files import walk_path
import os
from pathlib import Path

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        info_origem = file.read()
    with open(template_path) as file:
        template_origem = file.read()
    node = markdown_to_html_node(info_origem)
    html = node.to_html()
    try:
        title, info_origem = extract_title(info_origem)
    except Exception:
        title = "No Title"
    template_origem = template_origem.replace("{{ Title }}", title)
    template_origem = template_origem.replace("{{ Content }}", html)
    template_origem = template_origem.replace('href="/', f'href="{basepath}')
    template_origem = template_origem.replace('src="/', f'src="{basepath}')
    if not os.path.exists(os.path.dirname(Path(dest_path))):
        os.makedirs(os.path.dirname(Path(dest_path)))
    with open(dest_path, 'a') as file:
        file.write(template_origem)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files, _ = walk_path(dir_path_content)
    for file in files:
        arq = str(file)
        dest_path = arq.replace(dir_path_content[2:], dest_dir_path[2:])
        dest_path = dest_path.replace("md", "html")
        generate_page(file, template_path, dest_path, basepath)
    
    
    

