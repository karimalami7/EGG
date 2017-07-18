#####check gcc compiler
if ! [ -x "$(command -v g++)" ]; then
	echo 'apt-get install gcc-5 g++-5'
	apt-get install gcc-5 g++-5
else 
	echo 'g++ exists'
fi


#####check python
if ! [ -x "$(command -v python)" ]; then
	echo 'apt-get install python2.7'
	apt-get  install python2.7
else 
	echo 'python exists'
fi

echo 'apt-get install python-tk'
apt-get install python-tk

#####clone gmark project branch gmark_for_egg
echo 'we clone gMark'
git clone -b gmark_for_egg  https://github.com/karimalami7/gmark.git
mv gmark ../../
#####compile it 
cd ../../gmark/src
echo 'we compile gMark'
make



####check pip
if ! [ -x "$(command -v pip)" ]; then
	echo 'we install pip'
	apt-get install python-pip python-dev build-essential
	pip install --upgrade pip
	pip install --upgrade virtualenv
else 
	echo 'pip exists'
fi
#### install python libraries

cd ../../demo/scripts

#pip install --user virtualenvwrapper
#export WORKON_HOME=~/.virtualenvs
#mkdir -p $WORKON_HOME
#source ~/.local/bin/virtualenvwrapper.sh
#mkvirtualenv egg
#workon egg
echo 'we install requirements of EGG'
pip install -r requirement.txt
