files=$(ls ./thrift | grep '.thrift$')
for file in $files
do
    thrift --gen py thrift/$file
    thrift --gen cocoa thrift/$file
    echo "$file"
done
