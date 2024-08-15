class TriggersModules:
    @staticmethod
    # This method will create a trigger for the
    def create(triggers, measurement_code):
        for trigger in triggers:
            trigger["measurement_code"] = measurement_code
        return triggers    
        
