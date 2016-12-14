export xAuth='hdntl=exp=1481739342~acl=%2f*~hmac=45014ce0c725ac44ec7c4b96bb10510cb6ed4bebaf6e58e3bf5d097aa5c93cdc'

xF4M='http://olystreamwest.nbcolympics.com/vod/d000bd55-d8fc-4702-b19d-3690f708eaf0/nbc-olympics0803085230.ism/manifest(format=f4m-f4f,filtername=vodcut).f4m'
xComp=MPT


php ../AdobeHDS.php --manifest $xF4M?$xAuth --auth $xAuth --quality 56

python ./toCSV.py AQAQAQ BQBQBQ > xlist.csv 

# sed s%AQAQAQ%$xF4M% < xlist.csv > ylist.csv
# sed s%BQBQBQ%$xComp% < ylist.csv > zlist.csv


prodqual=7000

python fromCSV.py $prodqual manifest < xlist.csv > temp.sh 2> join.sh
chmod 777 temp.sh
xF4M='http://olystreamwest.nbcolympics.com/vod/d000bd55-d8fc-4702-b19d-3690f708eaf0/nbc-olympics0803085230.ism/manifest(format=f4m-f4f,filtername=vodcut).f4m'   xComp=MPT ./temp.sh > 300.sh 
chmod 777 300.sh
./300.sh 




python fromCSV.py 56 fragments < xlist.csv > temp.sh 
xComp=MPT ./temp.sh > 56.sh 
chmod 777 56.sh
./56.sh 




chmod 777 join.sh
xComp=MPT ./join.sh > temp.sh
./temp.sh	



# Available: 7001 7000 4001 4000 2201 2200 1401 1400 901 900 601 600 301 300 56
