import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

def get_survey_numbers(district, mandal, village):
    # Set up the Chrome driver with headless mode and additional options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")  # Linux-specific
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=1920,1080")

    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Error starting Chrome driver: {e}")
        return []

    # Navigate to the website
    url = 'https://dharani.telangana.gov.in/knowLandStatus'
    driver.get(url)

    # Wait for the page to load completely
    time.sleep(5)

    # Select the district
    district_dropdown = Select(driver.find_element_by_id('Districtcode'))
    district_dropdown.select_by_visible_text(district)

    # Wait for the mandal dropdown to populate
    time.sleep(5)

    # Select the mandal
    mandal_dropdown = Select(driver.find_element_by_id('Mandalcode'))
    mandal_dropdown.select_by_visible_text(mandal)

    # Wait for the village dropdown to populate
    time.sleep(5)

    # Select the village
    village_dropdown = Select(driver.find_element_by_id('Villagename'))
    village_dropdown.select_by_visible_text(village)

    # Submit the form
    submit_button = driver.find_element_by_id('btnSubmit')
    submit_button.click()

    # Wait for the new page to load
    time.sleep(5)

    # Get the survey numbers
    survey_numbers = []
    rows = driver.find_elements_by_xpath("//table[@class='table table-striped']/tbody/tr")
    for row in rows[1:]:
        cells = row.find_elements_by_tag_name('td')
        survey_numbers.append(cells[1].text.strip())

    # Close the browser
    driver.quit()

    return survey_numbers
