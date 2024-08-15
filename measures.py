class MeasurementModules:

    @staticmethod
    # Method to create a measurement module with the parameters api and data
    def create(api, data):
        measures_dict = {}
        measurements = data.get("measurements", [])
        
        # Loop through each measurement and return the result in a dictioanary
        for measurement in measurements:
            measurement_code = measurement.get("code")
            if not measurement_code:
                continue
            triggers = measurement.pop("triggers", [])
            
            measures_dict[measurement_code] = measurement
            if api and "triggers" in api.modules:
                api.call("triggers", "create", {"triggers": triggers, "measurement_code": measurement_code})
            else:
                print("Error calling API!")
        return measures_dict
    
