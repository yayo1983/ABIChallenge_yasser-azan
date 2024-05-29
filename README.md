# ABIChallenge_yasser-azan

# FastAPI Project with MVP Pattern for challenge

This is a FastAPI project structured using the MVP (Model-View-Presenter) pattern.

## Project Structure
```sh
api ML /
├── app/
│ ├── init.py
│ ├── main.py
│ ├── database.py
├── schemas/
│ │ └── init.py
│ │ └── item.py
│ ├── models/
│ │ └── init.py
│ │ └── item.py
│ ├── views/
│ │ └── init.py
│ │ └── item_view.py
│ ├── presenters/
│ │ └── init.py
│ │ └── item_presenter.py
│ ├── routes/
│ │ └── init.py
│ │ └── item_route.py
│ ├── tests/
│ │ └── init.py
│ │ └── unit/
│ │ ── └── test_item_presenter.py/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
## Solution architecture
View of the solution by components
![View of the solution by components](diag_arq.png)

You can access to edit the UML online in the following link
[You can access to edit the UML online in the following link](https://app.diagrams.net/?libs=general;uml#G1JxFIrjq3AOS-7ThH6TevdW00CMWJ6ZdC#%7B%22pageId%22%3A%22b5b7bab2-c9e2-2cf4-8b2a-24fd1a2a6d21%22%7D)


## Running the Project

### Using Docker Compose

1. Build and start the containers:

```sh
   docker-compose up --build
```

### Alternatieve to run local project

```sh
uvicorn app.main:app --reload
```

## Documentation

2. The API will be available at http://localhost:8000.

   Swagger UI: http://localhost:8000/docs
   ReDoc: http://localhost:8000/redoc

3. Using endpoints
   API Endpoints
   ```sh
   GET /: Presentation of project.
   GET /loaddata/: Load data from excel and clean and save in sqlite database 
   GET /unique_variables/: unique_variables  Get the number of unique values ​​per column
   GET /count_by_product/: Examining how many of each product are
   GET /interpreting_data/ data to analize the results
   ```

## Running the tests

To run all the tests you only need
```sh
pytest
```

If you want to run only one test file, you can put the file name as follows:

```sh
pytest tests/unit/test_item_presenter.py
```

Execute specific function test

```sh
pytest test_item_view.py::test_load_data_success
```
