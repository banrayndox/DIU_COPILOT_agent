
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import re

# def get_attendance():
#     """
#     Fetch attendance using hardcoded credentials (from original script).
    
#     Returns:
#         List of attendance percentages (strings like "75.5", "N/A", "Error")
#     """
#     # ========== STATIC VALUES (as in original) ==========
#     USERNAME = "251-15-445"
#     PASSWORD = "banRayndox@1"
#     SEMESTER_INDEX = 1      # 1 = second option (Summer 2026, 262)
#     HEADLESS = False        # Set True to hide browser window
    
#     # Chrome options
#     options = Options()
#     if HEADLESS:
#         options.add_argument("--headless")
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option('useAutomationExtension', False)
    
#     driver = webdriver.Chrome(options=options)
#     driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#     wait = WebDriverWait(driver, 10)
    
#     attendance_list = []
    
#     try:
#         # Open website
#         driver.get("https://studentportal.diu.edu.bd/")
#         print("Loading page...")
#         time.sleep(5)
        
#         # Click Login button (from first page)
#         try:
#             login_btn = driver.find_element(By.CSS_SELECTOR, "a.btn_1")
#             login_btn.click()
#             time.sleep(3)
#         except:
#             print("Login button might not exist, going directly to login page")
        
#         # Type username
#         username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
#         username_field.clear()
#         username_field.send_keys(USERNAME)
#         print("✓ Username entered")
        
#         # Type password
#         password_field = driver.find_element(By.ID, "password")
#         password_field.clear()
#         password_field.send_keys(PASSWORD)
#         print("✓ Password entered")
        
#         # Click Sign In button
#         driver.find_element(By.ID, "kc-login").click()
#         print("✓ Sign In button clicked")
        
#         # Go to live result page
#         driver.get("https://studentportal.diu.edu.bd/live-result")
#         time.sleep(5)
        
#         # Select semester
#         try:
#             semester_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "semesterId")))
#             semester_dropdown.click()
#             time.sleep(1)
            
#             # Use hardcoded semester index
#             options = driver.find_elements(By.CSS_SELECTOR, ".ng-option")
#             if SEMESTER_INDEX < len(options):
#                 options[SEMESTER_INDEX].click()
#                 print(f"✓ Selected semester index {SEMESTER_INDEX}")
#             else:
#                 print(f"⚠ Semester index {SEMESTER_INDEX} not available, using first")
#                 options[0].click()
#         except Exception as e:
#             print(f"Failed to select semester: {e}")
#             # Fallback: try JavaScript
#             driver.execute_script("""
#                 const dropdown = document.querySelector('ng-select#semesterId');
#                 if (dropdown) {
#                     const opts = dropdown.querySelectorAll('.ng-option');
#                     if (opts.length > 1) opts[1].click();
#                 }
#             """)
        
#         # Click Search button
#         driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.w-100").click()
#         print("✓ Search clicked")
#         time.sleep(8)
        
#         # Find all View Result buttons
#         view_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'View Result')]")
#         print(f"\nTotal {len(view_buttons)} View Result buttons found\n")
#         original_tab = driver.current_window_handle
        
#         for idx, button in enumerate(view_buttons):
#             try:
#                 print(f"Processing {idx+1}/{len(view_buttons)}:")
#                 # Open in new tab
#                 driver.execute_script("arguments[0].target = '_blank';", button)
#                 driver.execute_script("arguments[0].click();", button)
#                 time.sleep(2)
                
#                 # Switch to new tab
#                 new_tab = [tab for tab in driver.window_handles if tab != original_tab][0]
#                 driver.switch_to.window(new_tab)
#                 time.sleep(2)
                
#                 # Extract attendance
#                 page_text = driver.find_element(By.TAG_NAME, "body").text
#                 attendance = "N/A"
                
#                 # Method 1: Attendance Percentage label
#                 match = re.search(r'Attendance Percentage\s*[:.\n]*\s*(\d+(?:\.\d+)?)%', page_text, re.I)
#                 if match:
#                     attendance = match.group(1)
#                     print(f"  ✓ Found: {attendance}%")
#                 else:
#                     # Method 2: Find any 50-100% value
#                     percentages = re.findall(r'\b(\d+(?:\.\d+)?)%', page_text)
#                     for p in percentages:
#                         try:
#                             if 50 <= float(p) <= 100:
#                                 attendance = p
#                                 print(f"  ✓ Found plausible: {attendance}%")
#                                 break
#                         except:
#                             pass
#                     if attendance == "N/A":
#                         print(f"  ✗ Could not extract attendance")
#                         driver.save_screenshot(f"debug_course_{idx+1}.png")
                
#                 attendance_list.append(attendance)
                
#                 # Close tab and go back
#                 driver.close()
#                 driver.switch_to.window(original_tab)
#                 time.sleep(1)
                
#             except Exception as e:
#                 print(f"  ✗ Error: {str(e)[:100]}")
#                 attendance_list.append("Error")
#                 # Recovery
#                 if len(driver.window_handles) > 1:
#                     driver.close()
#                     driver.switch_to.window(original_tab)
        
#     except Exception as e:
#         print(f"Fatal error: {e}")
#     finally:
#         driver.quit()
    
#     return attendance_list

# # If you run this file directly, it will execute and print result
# if __name__ == "__main__":
#     result = get_attendance()
#     print("\n" + "="*60)
#     print("ATTENDANCE ARRAY:", result)
#     print("="*60)

import asyncio

# -----------------------------
# (OPTIONAL) SELENIUM PART HERE LATER
# -----------------------------
def scrape_attendance():
    # TODO: put selenium code here (blocking)
    return "88%"


# -----------------------------
# SIMPLE FUNCTION (NO STREAMER)
# -----------------------------
async def get_attendance():
    print("📊 Fetching attendance...")
    
    # 🔥 safe blocking execution
    attendance = await asyncio.to_thread(scrape_attendance)
    
    print(f"✅ Attendance fetched: {attendance}")
    
    return {
        "attendance": attendance
    }