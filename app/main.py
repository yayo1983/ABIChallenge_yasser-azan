from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.item_route import ItemRouter

class MainApp:
    """
    MyApp class encapsulates the setup and configuration of the FastAPI application.
    """
    def __init__(self):
        # Initialize FastAPI application
        self.app = FastAPI(
            title="MLOps Challenge v7",
            description="Yasser LOps Challenge v7",
            version="1.0.0",
        )
         # Set up CORS middleware
        self._setup_cors()

        self.setup_routes()

    def setup_routes(self):
        """
        Includes the routers in the FastAPI application
        """
        item_router = ItemRouter()
        self.app.include_router(item_router.router)
        
    def _setup_cors(self):
        """
        Configures Cross-Origin Resource Sharing (CORS) middleware for the FastAPI application.
        This allows the application to handle requests from different origins, which is useful
        for frontend-backend communication during development.

        Note:
            - In this setup, all origins, headers, and methods are allowed, which is convenient for development
            but should be restricted in a production environment for security reasons.
        """
        # Allow all origins, headers, and methods (be careful with this in production)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Allows all origins
            allow_credentials=True,
            allow_methods=["*"],  # Allows all methods
            allow_headers=["*"],  # Allows all headers
        )

        # Swagger documentation will be available at /docs by default
        # ReDoc documentation will be available at /redoc by default   

my_app = MainApp()
app = my_app.app


