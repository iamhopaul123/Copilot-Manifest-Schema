import json
from schema_node import schema_node

def generate_schema(parsed_docs):
    schema = {
        "description": "A schema that validates Copilot manifest",
        "anyOf": [],
        "$defs": {}
    }
    docs = json.loads(parsed_docs)

    for main in docs["main"]:
        node = schema_node()
        for item in main["properties"]:
            node.insert(item)
        schema["$defs"][main["name"]] = node.content
        schema["anyOf"].append({"$ref": "#/$defs/%s" % main["name"]})
        
    for main in docs["partial"]:
        node = schema_node()
        for item in main["properties"]:
            node.insert(item)
        schema["$defs"][main["name"]] = node.content

    return json.dumps(schema)

# For testing purpose.
if __name__ == "__main__":
   f = open("./mocks/mock_generator_input.txt", 'r') 
   realInput = f.read()
   print(generate_schema(realInput))