class LightNode:
    def inner_html(self):
        pass

    def outer_html(self):
        pass


class LightTextNode(LightNode):
    def __init__(self, text):
        self.text = text

    def inner_html(self):
        return self.text

    def outer_html(self):
        return self.text


class LightElementNode(LightNode):
    def __init__(self, tag, display_type, closure_type, css_classes=None):
        self.tag = tag
        self.display_type = display_type
        self.closure_type = closure_type
        self.css_classes = css_classes if css_classes else []
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def inner_html(self):
        result = ""
        for child in self.children:
            result += child.outer_html()
        return result

    def outer_html(self):
        classes_str = ""
        if self.css_classes:
            classes_str = ' class="' + " ".join(self.css_classes) + '"'

        if self.closure_type == "single":
            return "<" + self.tag + classes_str + "/>"

        start_tag = "<" + self.tag + classes_str + ">"
        end_tag = "</" + self.tag + ">"

        if self.display_type == "block":
            inner = ""
            for child in self.children:
                inner += "\n  " + child.outer_html().replace("\n", "\n  ")
            return start_tag + inner + "\n" + end_tag

        return start_tag + self.inner_html() + end_tag


if __name__ == "__main__":
    ul = LightElementNode("ul", "block", "pair", ["main-list"])

    li1 = LightElementNode("li", "block", "pair", ["list-item"])
    li1.add_child(LightTextNode("First item"))

    li2 = LightElementNode("li", "block", "pair", ["list-item", "active"])
    li2.add_child(LightTextNode("Second item"))

    ul.add_child(li1)
    ul.add_child(li2)

    print("--- Outer HTML ---")
    print(ul.outer_html())

    print("\n--- Inner HTML ---")
    print(ul.inner_html())