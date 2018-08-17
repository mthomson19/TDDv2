from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new onli"ne to-do app.
# She goes to check out its homepage
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assertIn('To-Do', self.browser.title)

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box
# Edith's hobby is tying fly-fishing lures

# When she hits enter, the pages updates, and the page lists
# "1: Buy peacock feathers" as an item in the to-do list

# There is still a text box inviting her to add another item
# She enters "Use peacock feathers to make a fly (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list
# Then she sees that the site has generated a unique URL for her
# There is some expainatory text to that effect

# She visits that URL - her todo list is still there

# Satified, she goes back to sleep

browser.quit
