from the_directory_scanner import prettify_structure, scan_directory

scan_result = scan_directory(directory=".",
                             output_file_name="directory_structure.txt",
                             ignored_items=('.git', '.idea', 'venv', '__pycache__',))

prettify_structure(output_file=scan_result, spaces_to_trim=4, lines_to_trim=1)
