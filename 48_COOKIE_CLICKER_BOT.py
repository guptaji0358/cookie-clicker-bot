from selenium import webdriver
from selenium.webdriver.common.by import By
import time

Driver = webdriver.Chrome()

Driver.maximize_window()

# Open game
Driver.get("https://ozh.github.io/cookieclicker/")

# Let game load fully
time.sleep(15)

# Find big cookie directly
Cookie = Driver.find_element(By.ID, "bigCookie")

print("Game Loaded!")

# Timers
TimeOut = time.time() + 60 * 5
CheckTime = time.time() + 5

while True:

    # Click cookie
    Cookie.click()

    time.sleep(0.01)

    # Every 5 seconds
    if time.time() > CheckTime:

        # Buy upgrades
        Upgrades = Driver.find_elements(
            By.CSS_SELECTOR,
            ".upgrade.enabled"
        )

        if Upgrades:

            try:
                Upgrades[0].click()
                print("Upgrade Bought!")

            except:
                pass

        # Buy products
        Products = Driver.find_elements(
            By.CSS_SELECTOR,
            ".product.enabled"
        )

        if Products:

            try:
                Products[-1].click()

                print(
                    f"Bought: {Products[-1].text}"
                )

            except:
                pass

        # Reset timer
        CheckTime = time.time() + 5

    # Stop after 5 minutes
    if time.time() > TimeOut:

        try:
            cps = Driver.find_element(
                By.ID,
                "cookiesPerSecond"
            ).text

            print(f"\nFinal CPS: {cps}")

        except:
            print("Couldn't get CPS")

        break

Driver.quit()