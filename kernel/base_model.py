from kernel.database import Database


class BaseModel:

    @classmethod
    def get_entries(cls, query: str) -> list:
        db = Database()
        data = db.run_query(query)
        db.close()
        return [cls(*item.values()) for item in data]
