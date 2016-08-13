target={{output_file_name}}
project_root={{project_root}}
sources={% for file in source_files %}{{ file }} {% endfor %}
object_root=./obj

c_objects_tmp= \
	$(addsuffix .o,$(filter %.c, $(sources)))
c_objects= \
	$(c_objects_tmp:%=$(object_root)/%)
cxx_objects= \
	$(addsuffix .o,$(filter %.cpp, $(sources))) \
	$(addsuffix .o,$(filter %.cxx, $(sources))) \
	$(addsuffix .o,$(filter %.cc, $(sources)))
cxx_objects_tmp= \
	$(cxx_objects_tmp:%=$(object_root)/%)

