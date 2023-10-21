from ellar.common import Module, exception_handler, JSONResponse, Response, IHostContext
from ellar.core import ModuleBase
from ellar.samples.modules import HomeModule
from .todo.module import TodoModule


@Module(modules=[HomeModule, TodoModule])
class ApplicationModule(ModuleBase):
    @exception_handler(404)
    def exception_404_handler(cls, context: IHostContext, exc: Exception) -> Response:
        return JSONResponse(dict(detail="Resource not found."))