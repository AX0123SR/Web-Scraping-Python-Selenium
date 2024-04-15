from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://github.com/collections/machine-learning")
projects = driver.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']")
project_list = {}
for proj in projects:
    proj_name = proj.text
    proj_url = proj.find_elements(By.XPATH,"a")[0].get_attribute("href")
    project_list[proj_name] = proj_url
project_df = pd.DataFrame.from_dict(project_list,orient='index')
project_df['project_name'] = project_df.index
project_df.columns = ['Project_URL','Project_Name']
project_df = project_df.reset_index(drop=True)
project_df.to_csv('project_list.csv')
print(project_df)
