my_file = open('files_project/data.txt','r')

file_content = my_file.read()

my_file.close()

print(file_content)

company_name = input("Enter company name: ")

my_file_writing = open('files_project/data.txt','w')

my_file_writing.write(company_name + 'technologies')

my_file_writing.close()