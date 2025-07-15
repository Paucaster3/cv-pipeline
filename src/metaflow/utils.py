from metaflow import FlowSpec, step


class VisionPipeline(FlowSpec):
    @step
    def start(self):
        # Ejemplo: descargar imágenes de MinIO (usa función previa)
        self.next(self.annotate)

    @step
    def annotate(self):
        # Llama a Label Studio para anotaciones
        self.next(self.train)

    @step
    def train(self):
        # Entrena modelo, guarda resultado
        self.next(self.mlflow_log)

    @step
    def mlflow_log(self):
        # Registra modelo y métricas en MLflow
        self.next(self.end)

    @step
    def end(self):
        print("Pipeline terminado.")


if __name__ == "__main__":
    VisionPipeline()
