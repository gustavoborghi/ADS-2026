file = input("File name: ")
file = file.lower().strip()

parts = file.split(".")[-1]

if parts == "gif":
    print("image/gif")
elif parts == "jpg":
    print("image/jpeg")
elif parts == "jpeg":
    print("image/jpeg")
elif parts == "png":
    print("image/png")
elif parts == "txt":
    print("text/plain")
elif parts == "zip":
    print("application/zip")
else:
    print("application/octet-stream")