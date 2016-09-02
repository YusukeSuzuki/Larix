include project.mk

all: LARIX_postbuild

LARIX_prebuild:
	@echo [pre build]

LARIX_mainbuild: LARIX_prebuild
	@echo [build]
	@make $(static_target)
	@make $(shared_target)

LARIX_postbuild: LARIX_mainbuild
	@echo [post build]

$(static_target): $(c_objects) $(cxx_objects)
	$(AR) rcs $@ $^

$(shared_target): $(c_objects) $(cxx_objects)
	$(CC) -o $@ $^ $(LDFLAGS)

$(c_objects) : $(object_root)/%.o: $(project_root)/%
	@mkdir -p $(dir $@)
	$(CC) -c -o $@ $< $(CFLAGS)

$(cxx_objects) : $(object_root)/%.o: $(project_root)/%
	@mkdir -p $(dir $@)
	$(CXX) -c -o $@ $< $(CXXFLAGS)

%.cxx %.cpp %.cc:
%.c:

clean:
	rm -rf $(static_target)
	rm -rf $(shared_target)
	rm -rf $(c_objects)
	rm -rf $(cxx_objects)

PHONY: all clean run LARIX_prebuild LARIX_mainbuild LARIX_postbuild

