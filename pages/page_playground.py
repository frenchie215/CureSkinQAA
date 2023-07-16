class Page:
    
    def __init__(self):
        self.url = 'www.amazon.com'

    def open(self):
        print('Url opening', self.url)

    def close(self):
        print('CLosing the page', self.url)


class LoginPage(Page):
    def open_login(self):
        print('Login page opens')

    def close(self):
        print('CLosing the page', self.url)

print(LoginPage().url)
login_page = LoginPage()

login_page.close()
print(login_page.url)


login_page.open_login()

# p = Page()
# # p.open_url()
# # p.close()

# print(p.url)