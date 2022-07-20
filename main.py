import json
from doc_parser import doc_parser
from doc_retriever import retrieve_docs
from generator import generate_schema

def main():
    docs = retrieve_docs()
    parser = doc_parser()
    for k, v in sorted(docs["main"].items()):
        parser.appendToMain(k, v)
    for k, v in sorted(docs["partial"].items()):
        parser.appendToPartial(k, v)
    print(generate_schema(parser.parsed_doc()))

if __name__ == "__main__":
    main()