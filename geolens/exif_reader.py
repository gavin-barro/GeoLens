from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image_path: str) -> dict:
    """
    Extracts EXIF metadata from an image file, including GPS info if present

    Args:
        image_path (str): Path to the image file

    Returns:
        dict: Dictionary containing EXIF metadata (including GPSInfo if available)
    """
    try:
        image = Image.open(image_path)
        exif_data_raw = image._getexif()
        if not exif_data_raw:
            return {}

        exif_data = {}
        for tag, value in exif_data_raw.items():
            decoded_tag = TAGS.get(tag, tag)
            if decoded_tag == "GPSInfo":
                gps_data = {}
                for gps_tag in value:
                    gps_name = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[gps_name] = value[gps_tag]
                exif_data["GPSInfo"] = gps_data
            else:
                exif_data[decoded_tag] = value

        return exif_data

    except Exception as e:
        print(f"Error reading EXIF data from {image_path}: {e}")
        return {}

