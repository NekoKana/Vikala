from .config import session
from .models.city import City

class CityProvider:
    @classmethod
    def insert(cls, model):
        session.add(model)
        session.commit()

    @classmethod
    def get_cities_by_pref_id(cls, pref_id):
        return session.query(City).filter(City.pref_id == pref_id).all()

        