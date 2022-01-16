from classes.Images.ImageBelt import ImageBelt
from classes.Images.ImageWrapper import ImageWrapper


class ImageBeltFactory:
    @staticmethod
    def getImageBelt(img_path: str, img_num: int, x: int, y: int, velocity: int, edge: int, horizontal: bool = True):
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
        return ImageBelt(image_w_list, velocity, edge, horizontal)
