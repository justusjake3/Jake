from ellar.common import Module
from ellar.core import ModuleBase
from ellar.di import Container

from .controllers import TodoController
from .services import TodoServices


@Module(
    controllers=[TodoController],
    providers=[TodoServices],
    routers=[],
)
class TodoModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        pass










