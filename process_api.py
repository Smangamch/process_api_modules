
class ProcessAPI:
 # Defining methods to register and call the measurements and triggers module

    def __init__(self):
        self.modules = {}
        
    # Method to register
    def register(self, name, module):
        self.modules[name] = module
    
    # Method to define an api call process
    def call(self, module_name, method_name, params):
        name = self.modules[module_name]
        method = getattr(name, method_name)
        return method(**params)
