sources_root={{src_root}}
objects_root={{obj_root}}
target={{output_file_name}}
sources=
objects=

all: $(target)
	$(CC) $@ $^ $(LDFLAGS)

$(target): $(objects)

clean:
	rm -rf $(objects)

PHONY: all clean

