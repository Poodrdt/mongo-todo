deploy:

on windows:
  docker-compose up

if "web_1  | python: can't open file 'src/manage.py': [Errno 2] No such file or directory":
  reset docker share drive

on linux:
 line 14 of docker-compose.yml:
  remove backslash like:
          - .\:/code" > - .:/code
  docker-compose up