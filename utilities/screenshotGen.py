import inspect


class Screenshot:
    @staticmethod
    def take_screenshot(driver):
        current_function_name = inspect.currentframe().f_back.f_code.co_name
        screenshot_filename = f".\\Screenshots\\{current_function_name}_screenshot.png"
        driver.save_screenshot(screenshot_filename)
