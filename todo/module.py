"""
@Module(
    controllers=[MyController],
    providers=[
        YourService,
        ProviderConfig(IService, use_class=AService),
        ProviderConfig(IFoo, use_value=FooService()),
    ],
    routers=(routerA, routerB)
    statics='statics',
    template='template_folder',
    # base_directory -> default is the `todo` folder
)
class MyModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        # for more complicated provider registrations
        pass

"""
from ellar.common import Module
from ellar.core import ModuleBase
from ellar.di import Container

from .controllers import TodoController
from .services import TodoServices
from ..user.services import UserServices
from ..user.controllers import UserController



@Module(
    controllers=[TodoController, UserController],
    providers=[TodoServices, UserServices],
    routers=[],
)
class TodoModule(ModuleBase):
    def register_providers(self, container: Container) -> None:
        pass


class UserModule(ModuleBase):
    def register_services(self, container: Container) -> None:
        pass











