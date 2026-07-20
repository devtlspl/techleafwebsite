from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link', 'col', 'base', 'param', 'source', 'track', 'area', 'rect', 'circle', 'path', 'ellipse', 'line', 'polyline', 'polygon']:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if not self.stack:
            print(f"Error: Closing tag </{tag}> at line {self.getpos()[0]} without an opening tag.")
            return

        # Find the matching opening tag
        for i in range(len(self.stack)-1, -1, -1):
            if self.stack[i][0] == tag:
                # Pop all tags up to the matching one
                unclosed = self.stack[i+1:]
                if unclosed:
                    pass
                    # print(f"Warning: Unclosed tags before </{tag}> at line {self.getpos()[0]}: {unclosed}")
                self.stack = self.stack[:i]
                return
        
        print(f"Error: Closing tag </{tag}> at line {self.getpos()[0]} has no opening tag.")

parser = MyHTMLParser()
with open('index.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())

if parser.stack:
    print("Unclosed tags at end of document:")
    for tag, pos in parser.stack:
        print(f"<{tag}> opened at line {pos[0]}")
