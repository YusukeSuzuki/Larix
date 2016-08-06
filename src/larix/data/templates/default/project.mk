target={{output_file_name}}
sources={% for file in source_files %}{{ file }} {% endfor %}
objects={{object_files}}

