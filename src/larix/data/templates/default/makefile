include project.mk

all: $(target)
	$(CC) $@ $^ $(LDFLAGS)

$(target): $(objects)

clean:
	rm -rf $(objects)

PHONY: all clean

