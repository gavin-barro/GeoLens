from geolens.exif_reader import get_exif_data

exif = get_exif_data("data/online_example.jpg")
print(exif.keys())

if "GPSInfo" in exif:
    print(exif["GPSInfo"])
else:
    print("No GPS data found.")
