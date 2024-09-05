import pyautogui
import time
from PIL import ImageGrab
import pytesseract
import pyperclip

# Path to tesseract.exe here
pytesseract.pytesseract.tesseract_cmd = r'F:\Program Files\Tesseract-OCR\tesseract.exe'


def AskChatGPT(question):
    # Customize as needed
    
    # Find the position of the new tab button (the '+' button) relative to the browser's tab area
    x_new_tab = 2355  # X-coordinate of the new tab button relative to the tab area
    y_new_tab = 20  # Y-coordinate of the new tab button relative to the tab area
    
    x_close_tab = 2319  # X-coordinate of the address bar
    y_close_tab = 20  # Y-coordinate of the address bar

    # Find the position of the address bar to type the website URL (adjust these coordinates according to your screen resolution and browser position)
    x_address_bar = 600  # X-coordinate of the address bar
    y_address_bar = 62  # Y-coordinate of the address bar

    # Find the position of the element you want to click on the website (you'll need to manually determine these coordinates)
    x_login = 1934  # X-coordinate of the element on the screen
    y_login = 704 # Y-coordinate of the element on the screen

    x_loginGoogle = 1267  # X-coordinate of the element on the screen
    y_loginGoogle = 835 # Y-coordinate of the element on the screen

    x_accountGoogle = 1284
    y_accountGoogle = 713

    x_nextGoogle = 1432
    y_nextGoogle = 916

    x_chat = 1139
    y_chat = 1331

    x1_textarea = 1072
    y1_textarea = 152
    x2_textarea = 1813
    y2_textarea = 1294

    # Open a new tab by clicking the '+' button
    pyautogui.click(x_new_tab, y_new_tab)

    # Give some time for the new tab to open
    time.sleep(1)

    # Move to the address bar and type the website URL
    pyautogui.click(x_address_bar, y_address_bar)
    pyautogui.write('https://chat.openai.com/')
    pyautogui.press('enter')

    # Give some time for the website to load
    time.sleep(4)

    ### Click on the element on the website
    ##pyautogui.click(x_login, y_login)
    ##time.sleep(4)
    ##
    ###Google Login
    ##pyautogui.click(x_loginGoogle, y_loginGoogle)
    ##
    ###Google Account Select
    ##time.sleep(3)
    ##pyautogui.click(x_accountGoogle, y_accountGoogle)
    ##
    ###Next
    ##time.sleep(3)
    ##pyautogui.click(x_nextGoogle, y_nextGoogle)
    ##
    ###Load
    ##time.sleep(10)

    ####GPT
    time.sleep(2)
    pyautogui.click(x_chat, y_chat)

    # Message ChatGpt
    pyautogui.write(question)
    pyautogui.press('enter')

    #Wait Response
    time.sleep(5)

    # Take a screenshot of the chat area
    chat_area = (x1_textarea, y1_textarea, x2_textarea, y2_textarea)  # Adjust the coordinates to capture the desired area
    screenshot = ImageGrab.grab(bbox=chat_area)

    # Save the screenshot temporarily (optional)
    screenshot.save("chat_area_screenshot.png")

    # Perform OCR on the screenshot to extract text
    extracted_text = pytesseract.image_to_string(screenshot)

    # Print the extracted text
    print(extracted_text)
    # Copy the extracted text to the clipboard (if needed)
    pyperclip.copy(extracted_text)
    
    # Close Tab after text is extracted
    pyautogui.click(x_close_tab, y_close_tab)


    return extracted_text



# Ask Chat GPT anything
AskChatGPT("hello")

