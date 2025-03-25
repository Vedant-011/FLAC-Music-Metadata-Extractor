import os
import json
from PyQt6.QtWidgets import QApplication, QFileDialog, QPushButton, QLabel, QWidget, QVBoxLayout
from mutagen.flac import FLAC
from mutagen.id3 import PictureType

class FLACMetadataExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("FLAC Metadata Extractor")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select a folder containing FLAC files:")
        layout.addWidget(self.label)

        self.button = QPushButton("Choose Folder")
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.extract_metadata(folder_path)

    def extract_metadata(self, folder_path):
        output_folder = os.path.join(folder_path, "Metadata_Output")
        os.makedirs(output_folder, exist_ok=True)

        for file in os.listdir(folder_path):
            if file.endswith(".flac"):
                file_path = os.path.join(folder_path, file)
                metadata = self.get_metadata(file_path)
                json_path = os.path.join(output_folder, file.replace('.flac', '.json'))
                with open(json_path, "w", encoding="utf-8") as json_file:
                    json.dump(metadata, json_file, indent=4)
                
                self.extract_album_art(file_path, output_folder)

        self.label.setText(f"Metadata saved in {output_folder}")

    def get_metadata(self, flac_file):
        audio = FLAC(flac_file)
        return {
            "Title": audio.get("title", ["Unknown"])[0],
            "Artist": audio.get("artist", ["Unknown"])[0],
            "Album": audio.get("album", ["Unknown"])[0],
            "Year": audio.get("date", ["Unknown"])[0],
            "Genre": audio.get("genre", ["Unknown"])[0]
        }

    def extract_album_art(self, flac_file, output_folder):
        audio = FLAC(flac_file)
        for picture in audio.pictures:
            if picture.type == PictureType.COVER_FRONT:
                image_path = os.path.join(output_folder, os.path.basename(flac_file).replace('.flac', '.jpg'))
                with open(image_path, "wb") as img_file:
                    img_file.write(picture.data)

if __name__ == '__main__':
    app = QApplication([])
    window = FLACMetadataExtractor()
    window.show()
    app.exec()
