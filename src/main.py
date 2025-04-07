from htmlfromblocks import markdown_to_html_node


def main():
    print("Main here, still doing nothing")
    md = """
        > This is a
        > blockquote block

        this is paragraph text

        """
    no = markdown_to_html_node(md)
    html = no.to_html()
    print(html)

if __name__ == "__main__":
    main()

