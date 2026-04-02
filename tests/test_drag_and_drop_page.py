from pages.drag_and_drop_page import DragAndDropPage

class TestDragAndDropPage:
    def test_images_button(self, page):
        base = DragAndDropPage(page)
        base.open_home_page()
        base.click_single_ui_elements()
        base.click_drag_and_drop_in_ui_elements()
        base.click_images_button()
        base.drag_and_drop_a_image()
        base.verification_image_result()

    def test_boxes_button(self, page):
        base = DragAndDropPage(page)
        base.open_drag_n_drop_page()
        base.click_boxes_button()
        base.drag_and_drop_a_box()
        base.verification_box_result()