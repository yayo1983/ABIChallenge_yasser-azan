import pytest
from app.views.item_view import ItemView
from pandas import DataFrame

# Mock database session to use in testing
class MockSession:
    def add(self, item):
        pass

    def commit(self):
        pass

    def rollback(self):
        pass

    def close(self):
        pass

# Fixture to provide an ItemView instance with a mock database session
@pytest.fixture
def item_view():
    return ItemView(MockSession())

def test_save_items(item_view):
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

    assert item_view.save_items(df)

def test_get_data(item_view):
    assert isinstance(item_view.get_data(), DataFrame)

def test_unique_variables(item_view):
    result = item_view.unique_variables()
    assert result is not False

def test_count_by_product(item_view):
    result = item_view.count_by_product()
    assert result is not False
