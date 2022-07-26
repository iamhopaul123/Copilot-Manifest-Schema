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

### __If you encounter this exception:__
```
Exception: API rate limit exceeded for 54.240.196.168. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)
```

This means that you've reached the [GitHub API rate limit](https://docs.github.com/en/rest/rate-limit). To get around this, all you need to do is to generate a [GitHub Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token), and pass your GitHub username and token as arguments like this:

> ```python3 main.py [username] [ghp-access-token]```

Doing so will allow you to make the API request under your personal account, increasing the [GitHub API Rate Limit](https://docs.github.com/en/rest/rate-limit).

---

## __Note__

A known limitation of the __Copilot Manifest Schema__ tool is that we generate the schema from the Copilot docs. As the docs are built and sustained to be a human readable source of information, they are not always consistent, and as such the schema that this tool generates may not always be helpful. Regardless, we've provided a useful tool for Copilot users, which allows you to maintain manifests without constantly moving between the Copilot docs and your IDE.
