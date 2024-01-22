from fastapi import FastAPI
import uvicorn

from .routers import api_router


class App:
    """
    FastAPI app initializer.
    """

    def __init__(self):
        self.app = FastAPI()


    def init_app(self):
        """
        Run all initializations.
        """
        self.init_routers()
        return self.app


    def init_routers(self):
        """
        Initialize routers.
        """
        self.app.include_router(api_router)


app = App().init_app()


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host="localhost",
        port=1607
    )
