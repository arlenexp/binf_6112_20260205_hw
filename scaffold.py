#!/usr/bin/env python3 

from pathlib import Path
import sys 

def file_gen(x): 
  new_dir = Path(x)
  new_file = new_dir / f"{x}.py"

  sys.stdout.write(f"Checking to see if file or directory '{x}' exist.... \n")
  if new_file.exists() or new_dir.exists(): 
    sys.stderr.write("This file already exists, do you wish to replace it? Enter 'Y' or 'N': ")
    choice = input().strip().lower()

    if choice != "y": 
      sys.stderr.write("Changes canceled. \n")
      return
      
  sys.stderr.write("Creating directory and file... \n")
  new_dir.mkdir()
  fout = open(f"{new_file}","w")
  fout.write("#!/usr/bin/env python3 \n") 
  fout.write("import sys \n\n") 
  fout.write("def main():\n")
  fout.write("  sys.stderr.write(\"This is a practice file to generate a template file!\\n\")\n")
  fout.write("  sys.stdout.write(\"Enter the title of this file: \n"\n")
  fout.write("  title=input()\n")
  fout.write(  sys.stdout.write(f\"The title of this document is: {title}\")\n\n)
  fout.write("if __name__ == \"__main__\":\n")
  fout.write("  main()\n")     
  fout.close()

def main():
  sys.stdout.write("Enter a name for output file: ")
  user_input = input().strip()
  file_gen(user_input)

if __name__ == "__main__": 
  main()

