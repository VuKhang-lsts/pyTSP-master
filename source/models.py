from database import Base
from sqlalchemy import Column, Integer, String, Float


class City(Base):
    __tablename__ = 'City'
    id         = Column(Integer, primary_key=True, autoincrement=True)
    name       = Column(String,  unique=True, nullable=False)
    latitude   = Column(Float,   nullable=False)
    longitude  = Column(Float,   nullable=False)
    population = Column(Integer)

    properties = ['id', 'name', 'latitude', 'longitude', 'population']

    def __init__(self, **data):
        # Nếu import_cities() truyền id, name, latitude, longitude, population
        # data sẽ chứa những keys trên
        self.id        = data.get('id')
        # Với key name (theo JSON đã sửa)
        self.name      = data.get('name') or data.get('city')
        self.latitude  = data.get('latitude') or data.get('lat')
        self.longitude = data.get('longitude') or data.get('lng')
        # population có thể là string hoặc int
        pop = data.get('population') or data.get('population_proper') or 0
        # ép kiểu int
        self.population = int(pop) if pop is not None else 0

    def __repr__(self):
        return self.name
