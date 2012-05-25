<<<<<<< HEAD
files=$(ls ./thrift | grep '.thrift$')
for file in $files
do
    thrift --gen py thrift/$file
    thrift --gen cocoa thrift/$file
    echo "$file"
done
=======
thrift --gen py -out . thrift/service.thrift 
>>>>>>> b6ce1d283c99fc80def77dc42383ceaf9d821da4
