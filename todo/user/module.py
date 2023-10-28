from ellar.common import Module
from ellar.core import ModuleBase
from ellar.di import Container

from ..user.services import UserServices
from ..user.controllers import UserController

@Module(
    controllers=[UserController],
    providers=[UserServices],
    routers=[],
)
class UserModule(ModuleBase):
    def register_services(self, container: Container) -> None:
        pass
