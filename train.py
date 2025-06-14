from ultralytics import YOLO


def main():
    # Inicijaliziraj YOLO model (koristi pretrenirani model kao bazu)
    model = YOLO("yolo8n.pt")  # možeš koristiti yolo8n.pt, yolo8s.pt, yolo8m.pt, itd.

    # Treniraj model na svom datasetu
    results = model.train(
        data="african-wildlife.yaml",  # YAML konfiguracija
        epochs=50,  # broj epoha, prilagodi po potrebi
        imgsz=640,  # veličina slike
        batch=8,  # batch size, prilagodi prema RAM-u/GPU-u
    )


if __name__ == "__main__":
    main()
