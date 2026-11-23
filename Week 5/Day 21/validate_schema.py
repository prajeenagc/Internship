
from pathlib import Path

from graphql import build_schema, parse, validate

# Load the GraphQL schema
schema_text = Path("schema.graphql").read_text(
    encoding="utf-8"
)

schema = build_schema(schema_text)

# Load example operations
operations_text = Path("operations.graphql").read_text(
    encoding="utf-8"
)

document = parse(operations_text)

# Validate operations against the schema
errors = validate(schema, document)

if errors:
    print("Validation failed:")

    for error in errors:
        print(error.message)
else:
    print("All operations are valid!")
