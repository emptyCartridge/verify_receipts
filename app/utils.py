#якорь и центральная точка

def anchor_sum(img, data, anchor_text:str, offset_x_perc=0.0, offset_y_perc=0.0, roi_width_perc=0.3, roi_height_perc=0.1):
    height, width = img.shape[:2]

    x = y = w = h = None

    for i, word in enumerate(data['text']):
        if word.lower() == anchor_text.lower():
            x = data['left'][i]
            y = data['top'][i]
            w = data['width'][i]
            h = data['height'][i]



    x_anchor_percent = (x + w / 2) / width
    y_anchor_percent = (y + h / 2) / height

    x1 = int(width * (x_anchor_percent + offset_x_perc))
    y1 = int(height * (y_anchor_percent + offset_y_perc))

    x2 = int(x1 + width * roi_width_perc)
    y2 = int(y1 + height * roi_height_perc)

    roi = img[y1:y2, x1:x2]

    return roi