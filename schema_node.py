class schema_node:
    def __init__(self):
        self.content = {
            "allOf": [],
            "properties": {}
        }
    def insert(self, item):
        if "ref" in item:
            self.content["allOf"].append({"$ref": "#/$defs/" + item["ref"]})
            return
        node = self.content
        paths = item["field"].split(".")
        parents, new_content = paths[:-1], paths[-1]
        for parent in parents:
            if "properties" not in node:
                node["properties"] = {}
            if parent not in node["properties"]:
                node["properties"][parent] = {
                    "properties": {}
                }
            node = node["properties"][parent]
        if "properties" not in node:
                node["properties"] = {}
        if new_content not in node["properties"]:
            node["properties"][new_content] = {}
        node = node["properties"][new_content]
        node["description"] = item["description"]

