from ellar.common import Module, exception_handler, JSONResponse, Response, IApplicationStartup, IExecutionContext
from ellar.core import ModuleBase
from ellar.samples.modules import HomeModule
from todo.routine.module import TodoModule
from todo.user.module import UserModule


@Module(modules=[HomeModule, TodoModule, UserModule])
class ApplicationModule(ModuleBase, IApplicationStartup):
    @exception_handler(404)
    def exception_404_handler(cls, context: IExecutionContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))