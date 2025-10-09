from pages.drag_and_drop_page import DragAndDrop

def test_drug_and_drop_page(page):
    base = DragAndDrop(page)

    base.open_home_page()
    base.click_single_ui_elements()
    base.click_drug_and_drop_in_ui_elements()

    base.click_images_button()
    base.drug_and_drop_a_image()
    base.verification_image_result()

    base.click_boxes_button()
    base.drug_and_drop_a_box()
    base.verification_box_result()