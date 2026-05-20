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

class ImageLoadStrategy:
    def load(self, href):
        pass

class NetworkImageLoadStrategy(ImageLoadStrategy):
    def load(self, href):
        print("Strategy: Downloading image from network URL: " + href)
        return "Network bytes data"

class FileSystemImageLoadStrategy(ImageLoadStrategy):
    def load(self, href):
        print("Strategy: Reading image from local path: " + href)
        return "Local storage bytes data"

class LightImageNode(LightNode):
    def __init__(self, href, load_strategy):
        self.tag = "img"
        self.href = href
        self.load_strategy = load_strategy

    def set_strategy(self, load_strategy):
        self.load_strategy = load_strategy

    def inner_html(self):
        return ""

    def outer_html(self):
        data = self.load_strategy.load(self.href)
        return '<img src="' + self.href + '" data-bytes="' + data + '"/>'

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
    net_strategy = NetworkImageLoadStrategy()
    fs_strategy = FileSystemImageLoadStrategy()

    div = LightElementNode("div", "block", "pair", ["gallery"])

    img_web = LightImageNode("https://example.com/logo.png", net_strategy)
    img_local = LightImageNode("/images/avatar.jpg", fs_strategy)

    div.add_child(img_web)
    div.add_child(img_local)

    print("--- Executing Render with Strategies ---")
    print(div.outer_html())