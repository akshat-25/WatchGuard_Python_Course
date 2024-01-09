from utils.file_operations import save_to_file, read_file
from utils.find import find_in

save_to_file('Hello',"import_projects/data.txt")
print(read_file('import_projects/data.txt'))
# When we import something that is a module
# When we run something that is a script

print(__name__)