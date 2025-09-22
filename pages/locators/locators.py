class MainPageLocators:
    BASE_URL = 'https://www.qa-practice.com/'
    Homepage = '#sidebar li.active span'
    Single_UI_Elements = '#sidebar li.has-sub.expand span'
    TITLE_TEXT = '#content h1'
    DESCRIPTION_TEXT = '#content p:nth-child(2)'
    SELECT_Text_input = '#content li:nth-child(1) > a'
    SELECT_Simple_button = '#content li:nth-child(2) > a'
    SELECT_Single_checkbox = '#content li:nth-child(3) > a'
    SELECT_Text_area = '#content li:nth-child(4) > a'
    SELECT_Select_input = '#content li:nth-child(5) a'

class TextInputPageLocators:
    TITLE_TEXT = '#content h1'
    Text_input_BUTTON = 'a[href="/elements/input/simple"]'
    Email_field_BUTTON = 'a[href="/elements/input/email"]'
    Password_field_BUTTON = 'a[href="/elements/input/passwd"]'
    Text_FIELD = '#id_text_string'
    Email_FIELD = '#id_email'
    Password_FIELD = '#id_password'
    INPUT_RESULT = '#result-text'

class SimplePageLocators:
    SUBMIT_BUTTON = "#submit-id-submit"
    RESULT_TEXT = "#result-text"