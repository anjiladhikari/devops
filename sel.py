from selenium import webdriver

driver = webdriver.Chrome()  # Make sure the ChromeDriver is installed and accessible
driver.get("http://localhost:8080")  # Your website's URL
assert "Jokes and Pictures" in driver.title
driver.quit()
