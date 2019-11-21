#/bin/sh
#data_path=/home/kishgau/Downloads/2019jan-june
data_path=/home/kishgau/devops/projects/asx-eod-turnover/week20191101


for f in $(ls $data_path/*.txt); 
do
echo "$f"
psql -c "copy marketdata from '$f' csv" asx_eod;
done


