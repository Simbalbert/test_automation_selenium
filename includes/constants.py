# In this file, we shall declare all the contants and variables that do not change. 
TEST_URL = "file:///C:/Users/CTRL-SHIFT%20Ltd/Documents/Portfolio/albert.github.com-main/albert.github.com-main/"
DYNAMIC_DEFAULT_URL = "file:///C:/Users/CTRL-SHIFT%20Ltd/Documents/Portfolio/albert.github.com-main/albert.github.com-main/"
ABOUT_TEXT = "ABOUT"
PORTFOLIO_DETAILS_TEXT = "Portfolio Details"
PORTFOLIO_TEXT = "PORTFOLIO"
SERVICES_TEXT = "SERVICES"
CONTACT_TEXT = "CONTACT"
MISSING_TEXT = "NonExistentPage"  # NEGATIVE TEST

ABOUT_URL = DYNAMIC_DEFAULT_URL + "about.html"
PORTFOLIO_DETAILS_URL = DYNAMIC_DEFAULT_URL + "portfolio-details.html"
PORTFOLIO_URL = DYNAMIC_DEFAULT_URL + "portfolio.html"
SERVICES_URL = DYNAMIC_DEFAULT_URL + "services.html"
CONTACT_URL = DYNAMIC_DEFAULT_URL +"contact.html"
HOME_URL = TEST_URL
MISSING_URL = "#does-not-exist"


# Mapping each test name to a unique Test ID (TC-01, TC-02, ...)
TEST_IDS = {
   # HOME_TEXT: "TC-01",
    ABOUT_TEXT: "TC-02",
    PORTFOLIO_TEXT: "TC-03",
    SERVICES_TEXT: "TC-04",
    CONTACT_TEXT: "TC-05",
    MISSING_TEXT: "TC-06"  # Negative Test ID
}