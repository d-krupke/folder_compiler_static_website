# Some processors for FolderCompiler to compile a static website

This static website generator is meant to generate simple webpages as simple as possible 
by mainly applying a markdown generator and jinjer templates in an organized way.
The general assumption is, that every output file only requires a single input file (+template).
You just specify which Processor is applied for which files (e.g., the MarkdownProcessor for all files ending with ".md" in the input directory).

See also the base project [folder_compiler](https://github.com/d-krupke/folder_compiler).

## Principles

* The primary focus is to apply a template to content files (e.g. a navigation bar).
* Keep it super simple (I update my webpage maybe every year and don't want it to take much knowledge that I immediately forget afterwards)
* Keep it open (especially do not hide jinja)
* Allow more complex behavior where possible without increasing the complexity of the generator (actually, this is included in the previous point).

## Processors

A processor gets an input file (e.g., a markdown file) and compiles it to an arbitrary amount of output files.

It is very simple to create your own processor (e.g., for automatically compressing every jpg into _small, _medium, and _large).
For the cases I need myself, a set of processors is already provided:
* HtmlProcessor: Simply passes the content to a jinjer template (thus, file content must already be html readable)
* MarkdownProcessor: Parses a markdown file including metadata and lets a jinjer template render it.
* BibtexProcessor: Parses a bibtex file and lets a jinjer template create a nice bibliography.
* FileCopyProcessor: Simply copies a file (Part of FolderCompiler)
* DevNullProcessor: Ignores files (Part of FolderCompiler)

## Example

See in the following example, how simple it is to configure:
```python
import jinja2 as jinja2

from folder_compiler import FolderCompiler
from folder_compiler.processors import FileCopyProcessor
from static_webpage_folder_compiler import MarkdownProcessor

# Create jinja2 environment as powerful template engine
# ./template holds the template files in this case
jinja = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./templates'),
)

# jinja templates (see example folder)
md_template = jinja.get_template("markdown_default.html")

# Processors
processors = [
    MarkdownProcessor(md_template).add_include(".*.md"),  # apply to all *.md files
    FileCopyProcessor().add_exclude(".*/\..*")  # copy the rest (except hidden files)
]

# Compile the files in the folder ./content to ./output
FolderCompiler(input="./content", output="./output").compile(processors).remove_orphaned_files()
```
A complete example can be found in [./example/simple_researcher_profile](./example/simple_researcher_profile).

But if you want to do something complex like a blog, try something more advanced like [Hyde](https://github.com/hyde/hyde).
