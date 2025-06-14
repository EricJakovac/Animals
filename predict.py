from ultralytics import YOLO


def main():
    # Učitaj najbolji istrenirani model
    model = YOLO("runs/detect/train/weights/best.pt")

    # Predikcija na testnim slikama
    results = model.predict(
        source="datasets/african-wildlife/test/images",  # putanja do test slika
        save=True,  # spremi slike s predikcijama u runs/predict
        imgsz=640,  # veličina slike
        conf=0.25,  # prag pouzdanosti
    )


if __name__ == "__main__":
    main()
