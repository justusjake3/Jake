from ellar.common import Module, exception_handler, JSONResponse, Response, IHostContext
from ellar.core import ModuleBase
from ellar.samples.modules import HomeModule
from .todo.module import TodoModule
from .user.module import UserModule


@Module(modules=[HomeModule, TodoModule, UserModule])
class ApplicationModule(ModuleBase):
    @exception_handler(404)
    def exception_404_handler(cls, context: IHostContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))