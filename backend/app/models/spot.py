from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.config.database import Base

class Spot(Base):
    __tablename__ = "spots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
