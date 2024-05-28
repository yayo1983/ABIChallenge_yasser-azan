from app.schemas.item import Item, ItemResponse
from app.views.item_view import ItemView
from app.views.rfm_metrics_view import RFMMetricView
from app.views.clean_data_view import CleanDataView
from sqlalchemy.orm import Session


class ItemPresenter:

    def default(self):
        example_item = Item(
            id=1, name="Presentation", description="Yasser LOps Challenge v7", price=0.0
        )
        return ItemView.display_item(example_item)

    def load_data(self, db: Session):
        clean_data_view = CleanDataView()
        df = clean_data_view.preparation_df()
        item = ItemResponse(message="Proccesing data", type="Info")
        if df is False:
            item = ItemResponse(message="Error loading file data", type="Error")
        item_view = ItemView(db)
        result = item_view.save_items(df)
        if result:
            ItemResponse(
                message="File uploaded successfully and data saved to the database.",
                type="Info",
            )
        if result is False:
            item = ItemResponse(
                message="Error saving data set in database", type="Error"
            )

        return ItemView.display_item(item)

    def unique_variables(self, db: Session):
        item_view = ItemView(db)
        result = item_view.unique_variables()
        item = ItemResponse(message="Proccesing data", type="Info")
        if result is False:
            item = ItemResponse(
                message="Error loading data from database", type="Error"
            )
        item = ItemResponse(message=result.to_string(), type="Info")
        return ItemView.display_item(item)

    def count_by_product(self, db: Session):
        item_view = ItemView(db)
        result = item_view.count_by_product()
        item = ItemResponse(message="Proccesing data", type="Info")
        if result is False:
            item = ItemResponse(
                message="Error loading data from database", type="Error"
            )
        item = ItemResponse(message=result.to_string(), type="Info")
        return ItemView.display_item(item)

    def interpreting_data(self, db: Session):
        item_view = ItemView(db)
        df = item_view.get_data()
        item = ItemResponse(message="Proccesing data", type="Info")
        if df is False:
            item = ItemResponse(
                message="Error loading data from database", type="Error"
            )
        rfm_view = RFMMetricView()
        result = rfm_view.interpreting_data(df)
        print(result)
        item = ItemResponse(message=result.to_string(), type="Info")
        return ItemView.display_item(item)
