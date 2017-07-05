#####check gcc compiler
if ! [ -x "$(command -v g++)" ]; then
	apt-get install gcc-5 g++-5
else 
	echo 'g++ exists'
fi


#####check python
if ! [ -x "$(command -v python)" ]; then
	apt-get install sudo apt-get install python2.7
else 
	echo 'python exists'
fi


#####clone gmark project branch gmark_for_egg
git clone -b gmark_for_egg  https://github.com/karimalami7/gmark.git
mv gmark ../../
#####compile it 
cd ../../gmark/src
make

apt-get install python-tk

####check pip
if ! [ -x "$(command -v pip)" ]; then
	apt-get install python-pip python-dev build-essential
	pip install --upgrade pip
	pip install --upgrade virtualenv
else 
	echo 'pip kayn'
fi
#### install python libraries

cd ../../demo/scripts

#pip install --user virtualenvwrapper
#export WORKON_HOME=~/.virtualenvs
#mkdir -p $WORKON_HOME
#source ~/.local/bin/virtualenvwrapper.sh
#mkvirtualenv egg
#workon egg

pip install -r requirement.txt
