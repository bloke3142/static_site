from textnode import TextNode, TextType

def main():
    #create new Textnode object
    test = TextNode("Some text", TextType.BOLD, "www.chipshop.com")
    print(test)

if __name__ == "__main__":
    main()
