# FLAC-Music-Metadata-Extractor

A simple Windows app to extract metadata and album art from FLAC music files.  

## **Features**  
✔ Select a folder with FLAC files  
✔ Extract metadata (Title, Artist, Album, Year, Genre)  
✔ Save metadata as JSON files  
✔ Save album art as JPG  

## **Usage**  
1. Run the app and select a folder.  
2. JSON files and album art will be saved in the same folder.  

## **Installation**  
- Install **Python 3.8+**  
- Install dependencies:  
  ```sh
  pip install mutagen Pillow PyQt6
  ```  
- Run:  
  ```sh
  python flac_metadata_gui.py
  ```  

## **Building a Windows Executable**  
```sh
pip install pyinstaller
pyinstaller --noconsole --onefile flac_metadata_gui.py
```

## **License**  
MIT License – Free to use and modify.  

---
