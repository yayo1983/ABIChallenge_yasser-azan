import pytest
from app.views.item_view import ItemView
from pandas import DataFrame

# Mock de la sesión de la base de datos para usar en las pruebas
class MockSession:
    def add(self, item):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass

# Fixture para proporcionar una instancia de ItemView con una sesión de base de datos simulada
@pytest.fixture
def item_view():
    return ItemView(MockSession())

# Prueba unitaria para el método save_items
def test_save_items(item_view):
    # Crear un DataFrame de ejemplo para usar en la prueba
    df = DataFrame({
        'Customer ID': [1, 2, 3],
        'Invoice': ['A', 'B', 'C'],
        'StockCode': ['X', 'Y', 'Z'],
        'Description': ['Product X', 'Product Y', 'Product Z'],
        'Quantity': [5, 10, 15],
        'InvoiceDate': ['2024-05-01', '2024-05-02', '2024-05-03'],
        'Price': [10.0, 20.0, 30.0],
        'Country': ['USA', 'UK', 'France']
    })

    # Llamar al método save_items y verificar que no lance excepciones
    assert item_view.save_items(df)

# Prueba unitaria para el método get_data
def test_get_data(item_view):
    # Llamar al método get_data y verificar que devuelva un DataFrame
    assert isinstance(item_view.get_data(), DataFrame)

# Prueba unitaria para el método unique_variables
def test_unique_variables(item_view):
    # Llamar al método unique_variables y verificar que devuelva un resultado
    result = item_view.unique_variables()
    assert result is not False

# Prueba unitaria para el método count_by_product
def test_count_by_product(item_view):
    # Llamar al método count_by_product y verificar que devuelva un resultado
    result = item_view.count_by_product()
    assert result is not False
