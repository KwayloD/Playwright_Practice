class MainPageLocators:
    Base_URL = 'https://www.qa-practice.com/'
    Homepage = '#sidebar li.active span'
    Single_UI_Elements = '#sidebar li.has-sub.expand span'
    Title_TEXT = '#content h1'
    Description_TEXT = '#content p:nth-child(2)'
    SELECT_Text_input = 'a[href="/elements/input/simple"]'
    SELECT_Simple_button = 'a[href="/elements/button/simple"]'
    SELECT_Single_checkbox = 'a[href="/elements/checkbox/single_checkbox"]'
    SELECT_Text_area = 'a[href="/elements/textarea/single"]'
    SELECT_Select_input = 'a[href="/elements/select/single_select"]'

class TextInputPageLocators:
    Title_TEXT = '#content h1'
    Text_input_BUTTON = 'a[href="/elements/input/simple"]'
    Email_field_BUTTON = 'a[href="/elements/input/email"]'
    Password_field_BUTTON = 'a[href="/elements/input/passwd"]'
    Text_FIELD = '#id_text_string'
    Email_FIELD = '#id_email'
    Password_FIELD = '#id_password'
    Input_RESULT = '#result-text'

class SimpleButtonPageLocators:
    Simple_BUTTON = 'a[href="/elements/button/simple"]'
    Looks_like_a_BUTTON = 'a[href="/elements/button/like_a_button"]'
    Disabled_BUTTON = 'a[href="/elements/button/disabled"]'
    Select_state_FIELD = '#id_select_state'
    Click_BUTTON = '#submit-id-submit'
    Click_looks_like_a_BUTTON = '#button-form > a'
    Submitted_TEXT = '#result-text'

class SingleCheckboxPageLocators:
    Single_checkbox_BUTTON = 'a[href="/elements/checkbox/single_checkbox"]'
    Checkboxes_BUTTON = 'a[href="/elements/checkbox/mult_checkbox"]'
    Single_CHECKBOX = '#id_checkbox_0'
    One_CHECKBOX = '#id_checkboxes_0'
    Two_CHECKBOX = '#id_checkboxes_1'
    Three_CHECKBOX = '#id_checkboxes_2'
    Submit_BUTTON = '#submit-id-submit'
    Selected_CHECKBOXES = '#result-text'

class TextAreaPageLocators:
    Textarea_BUTTON = 'a[href="/elements/textarea/single"]'
    Multiple_textareas_BUTTON = 'a[href="/elements/textarea/textareas"]'
    Text_area_FIELD = '#id_text_area'
    First_chapter_FIELD = '#id_first_chapter'
    Second_chapter_FIELD = '#id_second_chapter'
    Third_chapter_FIELD = '#id_third_chapter'
    Submit_BUTTON = '#submit-id-submit'
    Entered_TEXT = '#result-text'

#class SelectInputPageLocators: