import zipfile


class Zipper:
    @staticmethod
    def zip_up(filename="report.txt", archive_name="archive.zip"):
        with zipfile.ZipFile(archive_name, "w") as z:
            z.write(filename)
        print(f"File {filename} zipped into {archive_name}")

    def zip_list(archive_name="archive.zip"):
        try:
            with zipfile.ZipFile(archive_name, "r") as z:
                for info in z.infolist():
                    print(f"File: {info.filename}, Size: {info.file_size} bytes, Modified: {info.date_time}")
        except FileNotFoundError:
            print("Archive not found.")
