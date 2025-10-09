from pages.base_page import BasePage
from pages.locators.locators import MainPageLocators, DragAndDropLocators

class DragAndDrop(BasePage):

    def open_home_page(self):
        self.open(MainPageLocators.Base_URL)

    def click_single_ui_elements(self):
        self.click(MainPageLocators.Single_UI_Elements)

    def click_drug_and_drop_in_ui_elements(self):
        self.click(MainPageLocators.SELECT_Drag_and_Drop)

    def click_boxes_button(self):
        self.click(DragAndDropLocators.Boxes_BUTTON)

    def drug_and_drop_a_box(self):
        self.drag_and_drop(DragAndDropLocators.Drag_BOX, DragAndDropLocators.Drop_BOX)

    def verification_box_result(self):
        self.get_text_content(DragAndDropLocators.Result_BOX, 'Dropped!')

    def click_images_button(self):
        self.click(DragAndDropLocators.Images_BUTTON)

    def drug_and_drop_a_image(self):
        self.drag_and_drop(DragAndDropLocators.Drag_Image, DragAndDropLocators.Drop_Image)

    def verification_image_result(self):
        self.get_text_content(DragAndDropLocators.Result_IMAGE, 'Dropped!')