import marko
import html
import re
from bs4 import BeautifulSoup as bs, NavigableString, Tag
import os
import json

class doc_parser:
    def __init__(self):
        self._weblink = "https://aws.github.io/copilot-cli/docs"
        self._json_dic = {
            "main": [],
            "partial": []
        }
    
    def parsed_doc(self):
        return json.dumps(self._json_dic)

    def appendToMain(self, file_name, content):
        return self._appendToJsonDict("main", content, file_name, os.path.join(self._weblink, "manifest"))
    
    def appendToPartial(self, file_name, content):
        return self._appendToJsonDict("partial", content, file_name, os.path.join(self._weblink, "include"))
        
    def _appendToJsonDict(self, key, content, file_name, _weblink):
        struct = parseMdToJson(content, file_name, _weblink)
        if len(struct["properties"]) != 0:
            self._json_dic[key].append(struct)

def preProcess(inStream: str):
    regexQuery = '`{1,3}[^`]+`{1,3}'
    match = re.search(regexQuery, inStream)
    while match:
        word = inStream[match.span()[0]:match.span()[1]]
        word = html.escape(word)
        word = word.replace("`", "")
        inStream = inStream[:match.span()[0]] + word + inStream[match.span()[1]:]
        match = re.search(regexQuery, inStream)

    outStream = marko.convert(inStream)
    return outStream

def parseMdToJson(inStream: str, fileName: str, weblink: str):
    inStream = preProcess(inStream)
    soup = bs(inStream, 'html5lib')
    
    fileStruct = {
        "name": fileName.split('.')[0] + "." + fileName.split('.')[1],
        "properties" : [],
    }
    
    for tag in soup.find_all("p"):
        ancestors = ""
        href = ""
        field = ""
        type = ""
        description = ""
        
        for children in tag.contents:
            if isinstance(children, Tag):
                if "class" in children.attrs:
                    if "parent-field" in children.attrs["class"]:
                        ancestors = str(children.string)
                    if "field" in children.attrs["class"]:
                        field = str(children.string)
                        href = children.attrs["href"]
                    if "type" in children.attrs["class"]:
                        type = str(children.string)
                else:
                    if "href" in children.attrs:
                        description = description + str(children.string).replace("\n", " ")
            if isinstance(children, NavigableString):
                description = description + str(children).replace("\n", " ")
        description = description.strip()
        
        #
        #   If 'desc' matches '% include' then include as ref
        #   If 'type' is not "" then include as field
        #
        
        ancestors = html.unescape(ancestors)
        field = html.unescape(field)
        type = html.unescape(type)
        description = html.unescape(description)

        if type != "":
            fileStruct["properties"].append(
                {
                    "field": ancestors + field,
                    "type": type,
                    "description": "Type: " + type + "\n" + description + "\nMore info: " + os.path.join(weblink, fileName.split('.')[0], href)
                }
            )
        if "% include" in description:
            description = description.replace("{% include \'", "")
            description = description.replace(".md\' %}", "")
            fileStruct["properties"].append({"ref": description})

    return fileStruct