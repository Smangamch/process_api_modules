from process_api import ProcessAPI
from measures import MeasurementModules
from triggers import TriggersModules
import uuid

data = {
    "measurements": [
        {
            "code": uuid.uuid4(),
            "description": "Temperature",
            "triggers": [
                {
                    "code": "T1",
                    "description": "Temperature is too high",
                },
                {
                    "code": "T2",
                    "description": "Temperature is too low",
                }
            ]
        },
        {
            "code": uuid.uuid4(),
            "description": "Humidity",
            "triggers": [
                {
                    "code": "H1",
                    "description": "Humidity is too high"
                },
                {
                    "code": "H2",
                    "description": "Humidity is too low"
                },
                {
                    "code": "H3",
                    "description": "Humidity is normal"
                }
            ]
        } 
    ]   
}


# Create an instance of a process APi
api = ProcessAPI()

# Register the modules
api.register("measurements", MeasurementModules)
api.register("triggers", TriggersModules)

# Perform the API call and print the results
print(api.call("measurements", "create", {"api": api, "data": data}))

