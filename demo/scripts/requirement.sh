#####check gcc compiler

#####check python

#####clone gmark project branch gmark_for_egg
git clone -b gmark_for_egg  https://github.com/karimalami7/gmark.git
mv gmark ../../
####compile it 
cd ../../gmark/src
make
####check pip

#### install python libraries
cd ../../demo/scripts
pip install -r requirement.txt