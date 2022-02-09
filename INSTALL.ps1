echo "Installing Python"
$url = "https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe"
$outpath = "$PSScriptRoot/myexe.exe"
Invoke-WebRequest -uri $url -OutFile $outpath
$argsList = @('/quiet', 'DefaultAllUsersTargetDir=1', 'AssociateFiles=1')
Start-Process -Filepath "$PSScriptRoot/myexe.exe"

echo "Installing Libraries"
pip install pygame
pip install tk
pip install matplotlib
pip install pygubu
pip install tkfontchooser

echo "Setup Complete!"