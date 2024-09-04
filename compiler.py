import sys
import os
if len(sys.argv) < 2:
    print("Usage: python compiler.py <input_file.belgasem>")
    sys.exit(1)
program_file_path = sys.argv[1]
print("[cmd] parsing")
program_lines = []
with open(program_file_path, 'r') as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]
types=[{"bl":"ENTIER","c":"int"},{"bl":"NOMBRE","c":"float"}]
def inter(line):
    parts = line.split(" ")
    opcode = parts[0]
    ch=""
    if opcode == "ECRIRE":
        ch += 'printf("'
        ch+=parts[1]
        for i in range(2, len(parts)):
            ch += " "+parts[i]
        ch += '");'
    elif opcode=="LIRE":
        ch+="scanf("
        ch+='"%f"'if parts[1]=="NOMBRE"else ""
        ch+=",&"+parts[2]+");"
    elif opcode=="NOMBRE":
        ch+="float "+parts[1]+";"
    elif opcode=="ENTIER":
        ch+="int "+parts[1]+";"
    elif opcode=="ECHO":
        ch+="printf("
        ch+='"%f"'if parts[1]=="NOMBRE"else ""
        ch+='"%d"'if parts[1]=="ENTIER"else ""
        ch+=","+parts[2]+");"
    elif opcode=="SI":
        ch+="if("+parts[1]+"){\n"
    elif opcode=="POUR":
        ch+="for(int "+parts[1]+"="+parts[3]+"; i<="+parts[5]+";"+parts[1]+"++"+"){"
    elif opcode =="FIN":
        ch+="}\n"
    return ch
    



program = []
for line in program_lines:
    cd=inter(line)
    program.append(cd)
c_file_path = os.path.splitext(program_file_path)[0] + ".c"
with open(c_file_path, "w") as out:
    out.write("#include <stdio.h>\nint main() {\n")
    for line in program:
        out.write("    " + line + "\n")
    out.write("    return 0;\n}")
print("compile")
return_code = os.system(f"gcc {c_file_path} -o {os.path.splitext(program_file_path)[0]}")
if return_code != 0:
    print("Compilation failed.")
    sys.exit(1)
print("run")
os.system(f"{os.path.splitext(program_file_path)[0]}")