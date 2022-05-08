from classes.Images.ImageBelt import ImageBelt
from classes.Images.ImageWrapper import ImageWrapper


class ImageBeltFactory:
    @staticmethod
    def getImageBelt(img_path: str, img_num: int, x: int, y: int, velocity: int, edge: int, shift=0, shift_random=False, horizontal: bool = True):
        zero_image = ImageWrapper(img_path, 0)
        zero_image.set_position(x, y)
        image_w_list = [zero_image]
        for i in range(1, img_num):
            image_w_list.append(ImageWrapper(img_path, i))
            if horizontal:
                x_previous = image_w_list[i-1].image_rect.right
                image_w_list[i].set_position(x_previous, y)
            else:
                y_previous = image_w_list[i-1].image_rect.bottom
                image_w_list[i].set_position(x, y_previous)
        return ImageBelt(image_w_list, velocity, edge, shift, shift_random, horizontal=horizontal)

    @staticmethod
    def getManyImagesBelt(img_paths: list, x: int, y: int, velocity: int, edge: int, shift=0, shift_random=False, horizontal: bool = True, bottom_left=False):
        zero_image = ImageWrapper(img_paths[0], img_paths[0])
        zero_image.set_position(x, y, bottom_left)
        image_w_list = [zero_image]
        for i in range(1, len(img_paths)):
            image_w_list.append(ImageWrapper(img_paths[i], img_paths[i]))
            if horizontal:
                x_previous = image_w_list[i-1].image_rect.right
                image_w_list[i].set_position(x_previous-shift, y, bottom_left)
            else:
                y_previous = image_w_list[i-1].image_rect.bottom
                image_w_list[i].set_position(x, y_previous-shift, bottom_left)
        return ImageBelt(image_w_list, velocity, edge, shift, shift_random, horizontal=horizontal)
