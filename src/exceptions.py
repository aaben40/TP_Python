class ThresholdExceededException(Exception):
    def __init__(self, message="Le temps d'exécution a dépassé le seuil défini"):
        self.message = message
        super().__init__(self.message)
