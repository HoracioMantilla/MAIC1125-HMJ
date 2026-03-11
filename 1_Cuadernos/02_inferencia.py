import cv2
from ultralytics import YOLO
import supervision as sv
import argparse

def main(weights_path, source_path):
    # 1. Cargar el modelo entrenado
    model = YOLO(weights_path)

    # 2. Configurar el anotador (usando supervision para una estética limpia)
    box_annotator = sv.BoxAnnotator()
    label_annotator = sv.LabelAnnotator()

    # 3. Realizar inferencia
    results = model(source_path)[0]
    
    # Convertir resultados de Ultralytics a Supervision
    detections = sv.Detections.from_ultralytics(results)

    # 4. Anotar la imagen
    image = cv2.imread(source_path)
    annotated_image = box_annotator.annotate(scene=image, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

    # 5. Guardar y mostrar
    output_path = "result.jpg"
    cv2.imwrite(output_path, annotated_image)
    print(f"✅ Inferencia completada. Resultado guardado en: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inferencia de EPP en Construcción")
    parser.add_argument("--weights", type=str, default="weights/best.pt", help="Ruta al archivo .pt")
    parser.add_argument("--source", type=str, required=True, help="Ruta a la imagen o video")
    
    args = parser.parse_args()
    main(args.weights, args.source)
