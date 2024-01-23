# file reading and writing
input_file = "readme.txt"
with open (input_file,'w') as f:
    f.write("hello world!")
with open (input_file,'r') as f:
    text = f.read()
    print(text)
modified_text = text.strip() + "\nmodified!"
output_file = "writeme.txt"
with open (output_file,'w') as f:
    f.write(modified_text)
print("data modified")
with open (output_file,'r') as f:
    print(f.read())