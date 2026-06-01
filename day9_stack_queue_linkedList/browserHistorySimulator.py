class BrowserHistory:
    def __init__(self):
        self.history = []

    # Visit a new page
    def visit_page(self, page):
        self.history.append(page)
        print(f"Visited: {page}")

    # Go back to previous page
    def go_back(self):
        if len(self.history) <= 1:
            print("No previous page available")
            return

        self.history.pop()
        print(f"Current Page: {self.history[-1]}")

    # Show current page
    def show_current_page(self):
        if not self.history:
            print("No page opened")
        else:
            print(f"Current Page: {self.history[-1]}")


# Driver Code
browser = BrowserHistory()

browser.visit_page("google.com")
browser.visit_page("youtube.com")
browser.visit_page("github.com")

browser.show_current_page()

browser.go_back()
browser.show_current_page()

browser.go_back()
browser.show_current_page()