from typing import Union


class Database:
    '''Simulação de uma conexão com banco de dados SQL (algumas linhas genéricas estão comentadas para não quebrar o código)'''

    def __init__(self, *args) -> None:
        # self._connection = method_from_some_lib(*args)
        pass

    def run_query(self, query: str) -> Union[dict, list, None]:
        # data = self._connection.run(query)
        data = [
            {"name": "Souza", "age": 35, "country": "Mexico"},
            {"name": "Andrade", "age": 35, "country": "Chile"},
            {"name": "Felipe", "age": 35, "country": "Colombia"},
            {"name": "Sérgio", "age": 35, "country": "Colombia"},
            {"name": "Lisboa", "age": 35, "country": "Colombia"},
            {"name": "Souza Lima", "age": 35, "country": "Brazil"},
            {"name": "Philip", "age": 35, "country": "USA"},
            {"name": "Antony", "age": 35, "country": "UK"},
        ]
        return data

    def close(self) -> None:
        # self._connection.close()
        pass
