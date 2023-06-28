import subprocess

tok = "token"
exp_path = './DiscordChatExporter.Cli/DiscordChatExporter.Cli.exe'
finished = open("finished", "a")
try:
    finished_check = finished.readlines()
except:
    finished_check = []

command = [exp_path, 'guilds', '-t', tok]
result = subprocess.run(command, capture_output=True)
stdout_bytes = result.stdout
stdout = stdout_bytes.decode('utf-8', errors='replace')
servers = []
l = stdout.split(' | ')
for i in l:
    i = i.split('\n')
    for x in i:
        if x.isnumeric():
            servers.append(x)
        elif x[:-1].isnumeric():  # what the fuck
            servers.append(x[:-1])


for server in servers:
    if server in finished_check:
        print(f'{server} completed, passing...')
        continue
    print('continuing with' + server)
    command = [exp_path, 'exportguild', 
               '-t', tok, '-g', server, '-o', './dataset', '-f', 'Json', '--parallel', '9']
    result = subprocess.run(command, capture_output=True)
    print(result.stdout)  # debugging
    print(f'{server} data exported, saved...')
    finished.write(f"{server}\n")

finished.close() 