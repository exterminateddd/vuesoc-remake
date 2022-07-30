from datetime import datetime


class APIResponse:
    def __init__(self, 
            success: bool = False,
            data: dict = {}):
        self.success = success
        self.data = data
        self.errors = []
        
        self.generated_at = datetime.utcnow
    
    def add_error(self, e_text):
        self.errors.append(e_text)

    def __dict__(self):
        return {
            "success": self.success,
            "data": self.data,
            "errors": self.errors
        }
    
    def to_dict(self):
        return self.__dict__();
