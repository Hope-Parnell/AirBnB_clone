import models.engine.file_storage as file_storage
from models.base_model import BaseModel
from models.user import User


storage = file_storage.FileStorage()
storage.reload()

dict_greyson = {
    "BaseModel": BaseModel,
    "User": User
    }
