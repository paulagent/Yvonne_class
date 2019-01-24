
for d in /run/media/maria/Seagate_Spectral_Fernanda/OLCI/2018/*;
do
   if [ -d ${d} ]; then
   cd "$d"   
for f in ./*;
do
  if [ -d ${f} ]; then
  cd "$f"
unzip -d /home/maria/Documents/OLCI_2.23/2018 "S3A*.zip"
cd ..
fi
done
cd ..
fi
done

