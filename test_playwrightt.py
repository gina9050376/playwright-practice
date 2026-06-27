import pytest
import logging
from playwright.sync_api import Page, expect

# 修改這裡：設定 force=True 可以確保設定生效
logging.basicConfig(
    filename='test_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    force=True 
)

# 為了確保寫入，我們定義一個 helper function
def log_and_print(message):
    logging.info(message)
    print(message) # 同時顯示在終端機，讓你一眼看到進度

def test_login_error_logging(page: Page):
    log_and_print("測試開始：前往 SauceDemo")
    page.goto("https://www.saucedemo.com/")

    log_and_print("輸入正確帳號與錯誤密碼")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password_123")
    
    log_and_print("點擊登入")
    page.click("#login-button")

    error_locator = page.locator('[data-test="error"]')
    
    if error_locator.is_visible():
        log_and_print("成功偵測到錯誤訊息，測試通過")
        expect(error_locator).to_contain_text("Username and password do not match")
    else:
        log_and_print("未發現錯誤訊息，測試邏輯異常")
        pytest.fail("沒有出現錯誤訊息！")

    log_and_print("測試結束")