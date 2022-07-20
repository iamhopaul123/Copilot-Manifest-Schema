# __Copilot Manifest Schema__
Copilot Manifest Schema is a tool for generating json parsed outputs for yaml Intellisense of the [AWS Copilot-CLI](https://aws.github.io/copilot-cli/) manifest docs.

---

## __Dependencies__
The tool requires installing the following python packages on your local machine:
- marko
- bs4
- html5lib
- requests

This can be done with `pip install`

The tool also requires YAML language support through [JSON Schemas](https://json-schema.org/). We'll be showcasing this with the VSCode Extension [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

---

## __Using the Tool__
Run the program by executing `main.py`. This will pull content from the Copilot-CLI GitHub repository, and output a string with the .json string format.

You can pipe this output into a file like this:

> ```python3 main.py > copilot-schema.json```

To add this schema to the YAML extension, go into the YAML extension settings and scroll to `Yaml: Schemas` and click `Edit in settings.json`. And then add your file to the dictionary:

<img src="assets/config.gif" width="738" height="420"/>

Now when editing a Copilot manifest, the __Copilot Manifest Schema__ will assist you in creating your manifest!

<img src="assets/demo.gif" width="738" height="420"/>

---

## __Note__

A known limitation of the __Copilot Manifest Schema__ tool is that we generate the schema from the Copilot docs. As the docs are built and sustained to be a human readable source of information, they are not always consistent, and as such the schema that this tool generates may be inconsistent. Regardless, we've provided a useful tool for Copilot users, which allows you to maintain manifests without constantly moving between the Copilot docs and your IDE.
