from textnode import TextNode, TextType


def main():
    test_node = TextNode("primeiro teste", TextType.CODE, "www.testando.com" )
    print(test_node)


if __name__ == "__main__":
    main()

