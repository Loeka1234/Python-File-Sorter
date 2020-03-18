# Loeka Lievens
import os
from glob import glob
import shutil

while True:
    try:
        path = input("Give the directory you want to organize files: ").replace("\\", "/")
        if path[len(path)-1] != "/": # Adds slash at the end if the last char is not a slash
            path += "/"
        if not os.path.isdir(path):
            raise Exception
        break
    except:
        print("This is not a valid folder path!")

input("\033[91mRunning this script can cause problems with certain files. Press enter to continue...\033[0m")

extensions = [".aif", ".cda", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl",
              ".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip",
              ".bin", ".dmg", ".iso", ".toast", ".vcd",
              ".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml",
              ".email", ".eml", ".emlx", ".msg", ".oft", ".ost", ".pst", ".vcf",
              ".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".py", ".wsf",
              ".fnt", ".fon", ".otf", ".ttf",
              ".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff",
              ".asp", ".aspx", ".cfm", ".cgi", ".pl", ".css", ".htm", ".html", ".js", ".jsp", ".part", ".php", ".rss", ".xthml",
              ".key", ".odp", ".pps", ".ppt", ".pptx",
              ".ods", ".xls", ".xlsm", ".xlsx",
              ".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf", ".vob", ".wmv",
              ".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"]

folders = 0
filesCopied = 0

for e in extensions:
    search = path + "*" + e
    if (not os.path.exists(path + e)) and len(glob(search)) != 0:
        folders += 1
        os.makedirs(path + e)
    for file in glob(search): # Searches all files with the extension
        shutil.copy(file, path + e)
        os.remove(file)
        filesCopied += 1
        print("Copied " + os.path.basename(file) + " to the folder \"" + e + "\"")

print("\033[92mMoved " + str(filesCopied) + " files to " + str(folders) + " folders.")