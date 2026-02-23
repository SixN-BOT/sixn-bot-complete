from pydantic import BaseModel
class UserProfile(BaseModel):
    hobbies: list
    mood: str