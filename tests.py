import pytest
import unittest
import asyncio
from process_api import ProcessAPI
from measures import MeasurementModules
from triggers import TriggersModules
from main import data


api = ProcessAPI()

# Test the register method and adds the test into the module dictionary
@pytest.mark.asyncio
async def test_register_module_success():
    api.register("measurements", MeasurementModules)
    api.register("triggers", TriggersModules)
    assert "measurements" in api.modules
    assert "triggers" in api.modules

    # Check if modules are an instance of the Module
    assert isinstance(api.modules["measurements"], MeasurementModules)
    assert isinstance(api.modules["triggers", TriggersModules])


# Registers an empty value onto the module
@pytest.mark.ascyncio
async def test_register_module_fail():
    api.register("", MeasurementModules)
    assert ValueError in api.modules == False
    


# Test the api call module
@pytest.mark.asyncio
async def positive_test_call_module(self):
    api.register('measurements', MeasurementModules)
    api.call("measurements", "create", {"api": api, "data": data})
    self.assertIn("measurements", api.modules)

# Checks if the a correct module is parsed in to the api call
@pytest.mark.asyncio
async def negetive_test_call_module():
    api.register("measurements", MeasurementModules)
    with pytest.raises(ModuleNotFoundError):
        api.call("Measurements", "create", {"api": api, "data": "sample_data"})

# Test the measures module
@pytest.mark.asyncio
async def test_create_module_positive(self):
    #Executes the creaate method with valid data
    create_measure = MeasurementModules.create(api, data)

    expected_output_result = {
        str(data["measurements"][0]["code"]):{
            "description": "Temperature"
        },

        str(data["measurements"][1]["code"]):{
            "description": "Humididty"
        }
    }
    
    self.assertEquals(create_measure, expected_output_result)
    


@pytest.mark.asyncio
async def test_create_module_negetive(self):
    invalid_data = {"measurements": [
        {
            "code": 0000,
            "description": "Temp"
        } #Missing triggers and Humidity information
    ]}
    create_measure = MeasurementModules.create(api, invalid_data)

    expected_output_result = {
            str(invalid_data["measurements"][0]["code"]): {
                "description": "Temperature"
            },
            str(invalid_data["measurements"][1]["code"]): {
                "description": "Humidity"
            }
        }
    # Compares the create_measure and the expected output
    self.assertEqual(create_measure, expected_output_result)



@pytest.mark.asyncio
async def test_create_triggers_positive(self):
        
        # Expected result
        expected_triggers = [
            {"code": "T1", "description": "Temperature is too high", "measurement_code": self.measurement_code},
            {"code": "T2", "description": "Temperature is too low", "measurement_code": self.measurement_code}
        ]

        # Call the method
        result = TriggersModules.create(self.triggers, self.measurement_code)

        # Assert that the result matches the expected output
        self.assertEqual(result, expected_triggers)

@pytest.mark.asyncio
async def test_create_triggers_negetive(self):
     
     #Create an empty trigger
     empty_triggers = []
     expected_output = []
     #Call the method
     result = TriggersModules.create(empty_triggers, self.measurement_code)

     # Assert the result to compare

     self.assertEqual(result, expected_output)

     


    