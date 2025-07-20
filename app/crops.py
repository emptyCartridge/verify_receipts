from .utils import anchor_sum
from .ocr_reader import get_ocr_data

img, data = get_ocr_data('C:/checkreader/static/check_sample2.jpg')


def crop_by_coords_top(image):
    height, width = image.shape[:2]

    x1 = int(width * 0.0)
    x2 = int(width * 1.0)
    y1 = int(height * 0.0)
    y2 = int(height * 0.2)

    roi = image[y1:y2 , x1:x2]
    return roi


def crop_by_coords_mid(image):
    height, width = image.shape[:2]

    x1 = int(width * 0.0)
    x2 = int(width * 1.0)
    y1 = int(height * 0.3)
    y2 = int(height * 0.55)

    roi = image[y1:y2, x1:x2]
    return roi

roi_sum = anchor_sum(
    img,
    data,
    anchor_text="сумма",
    offset_x_perc=-0.3,
    offset_y_perc=0.1,
    roi_width_perc=0.36,
    roi_height_perc=0.25
)

# roi_total_sum = anchor_sum(
#     img,
#     data,
#     anchor_text="итого:",
#     offset_x_perc=0.5,
#     offset_y_perc=0.0,
#     roi_width_perc=0.5,
#     roi_height_perc=0.35
# )


def crop_by_coords_bot(image):
    height, width = image.shape[:2]

    x1 = int(width * 0.0)
    x2 = int(width * 1.0)
    y1 = int(height * 0.7)
    y2 = int(height * 0.8)

    roi = image[y1:y2, x1:x2]
    return roi