"""
Simply execute this file with python. Best use pipenv for the requirements,
 i.e., pipenv run python3 compile.py
"""


import jinja2 as jinja2

from folder_compiler import FolderCompiler
from folder_compiler.processors import FileCopyProcessor, DevNullProcessor

from folder_compiler_static_website import HtmlProcessor, MarkdownProcessor, \
    BibtexProcessor

# Create jinja2 environment as powerful template engine
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
)

# templates
html_template = jinja.get_template("html_default.html")
md_template = jinja.get_template("markdown_default.html")
bibtex_template = jinja.get_template("bibtex_default.html")

# Processors
processors = [
    DevNullProcessor().include_hidden_files_and_folders(),  # Skip all hidden files
    HtmlProcessor(html_template).add_include(".*\.html"),  # apply to all *.html files
    MarkdownProcessor(md_template).add_include(".*.md"),  # apply to all *.md files
    BibtexProcessor(bibtex_template).add_include(".*\.bib"),  # apply to all *.bib files
    FileCopyProcessor().add_exclude(".*/\..*")  # copy the rest (except hidden files)
]

# Compile
swp = FolderCompiler(input="./content", output="./output").compile(processors)
for file, owner in swp._context.file_ownership_manager.iterate_owned_files():
    print(file, owner)
swp.remove_orphaned_files()
