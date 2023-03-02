import os


def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}")


if __name__ == "__main__":

    files = os.listdir()
    files.remove("main.py")

    createIfNotExists('Images')
    createIfNotExists('Videos')
    createIfNotExists('Audios')
    createIfNotExists('Docs')
    createIfNotExists('Zipped')
    createIfNotExists('Others')
    createIfNotExists('Codes')

    imgExts = [".jpeg", ".png", ".jpg", ".tiff", ".gif", ".bmp", ".bpg", ".svg", ".heif", ".psd"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

    vidExts = [".avi", ".mkv", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt",
               ".mpg", ".mpeg", ".3gp", ".hevc"]
    videos = [file for file in files if os.path.splitext(file)[1].lower() in vidExts]

    audExts = [".aac", ".aa", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3", ".msv", ".ogg", ".oga", ".raw",
               ".vox", ".wav", ".wma"]
    audios = [file for file in files if os.path.splitext(file)[1].lower() in audExts]

    codExts = [".py", ".java"]
    codes = [file for file in files if os.path.splitext(file)[1].lower() in codExts]

    compressedExts = [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z", ".dmg",
                      ".rar", ".xar", ".zip"]
    compressed = [file for file in files if os.path.splitext(file)[1].lower() in compressedExts]

    docExts = [".oxps", ".epub", ".pages", ".docx", ".txt", ".pdf", ".doc", ".fdf", ".ods", ".odt",
               ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox", ".rvg", ".rtf", ".rtfd", ".wpd",
               ".xls", ".xlsx", ".ppt", ".pptx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in audExts) and (ext not in vidExts) and (ext not in docExts) and (
                ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Videos", videos)
    move("Audios", audios)
    move("Zipped", compressed)
    move("Docs", docs)
    move("Others", others)
    move("Codes", codes)

print("Operation completed!")
print("Thanks for using FileOrganiser Plus. have a good day")
