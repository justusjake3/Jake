from ellar.common import Module, exception_handler, JSONResponse, Response, IApplicationStartup, IExecutionContext
from ellar.core import ModuleBase, App
from ellar.samples.modules import HomeModule
from .todo.module import TodoModule
from .user.module import UserModule

from .todo.database import get_engine
from .todo.models import Base


@Module(modules=[HomeModule, TodoModule, UserModule])
class ApplicationModule(ModuleBase, IApplicationStartup):
    @exception_handler(404)
    def exception_404_handler(cls, context: IExecutionContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))