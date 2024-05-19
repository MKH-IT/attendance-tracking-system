from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.inspectors import SwaggerAutoSchema


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema


class CustomAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        tags = self.overrides.get("tags", None) or getattr(self.view, "schema_tags", [])
        if not tags:
            tags = [operation_keys[0]]
        return tags
