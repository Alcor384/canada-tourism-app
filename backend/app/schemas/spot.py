from pydantic import BaseModel

class SpotOut(BaseModel):
    id: int
    name: str
    description: str
    latitude: float
    longitude: float
    image_url: str | None

    class Config:
        orm_mode = True
