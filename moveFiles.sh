for f in *.html
 do
   filename="${f##*/}" 
 echo ${filename}        
         echo "moving files..."
         mv "${f}" docs/
done

for f1 in *.css 
 do
   filename2="${f1##*/}" 
 echo ${filename2}        
      if [[ "${f1}" == *c* ]]
         then 
         echo "moving files..."
         mv "${f1}" docs/
       fi
done

cp Diagrams/*.svg #docs/Diagrams
#cp -R Images docs/
#cp -R lateximages docs/