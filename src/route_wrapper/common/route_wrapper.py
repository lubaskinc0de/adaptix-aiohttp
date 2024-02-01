from route_wrapper.common import OutputModelT

from route_wrapper.common.route import Route
from route_wrapper.common.parser import ParamsGetter


class RouteWrapper:
    def __init__(
        self,
        route: Route,
        params_getter: ParamsGetter,
    ) -> None:
        self.view_obj = route.view_obj
        self.request = route.request
        self.view_signature = route.view_signature
        self.source_params = route.source_params
        self.view = route.view
        self.params_getter = params_getter
        self.additional_kwargs = route.additional_kwargs

    async def __call__(self) -> OutputModelT:
        if self.view_obj and len(self.view_signature.parameters) == 2:
            func_result: OutputModelT = await self.view(self.view_obj, self.request)
            return func_result

        if not self.view_obj and len(self.view_signature.parameters) == 1:
            func_result: OutputModelT = await self.view(self.request)
            return func_result

        params_getter = self.params_getter
        view_params = await params_getter.get_params()

        if self.view_obj:
            func_result: OutputModelT = await self.view(
                self.view_obj, self.request, **view_params, **self.additional_kwargs
            )
            return func_result

        func_result: OutputModelT = await self.view(
            self.request, **view_params, **self.additional_kwargs
        )
        return func_result
