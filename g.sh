
files=$(ls ./thrift | grep '.thrift$')
for file in $files
do
    thrift --gen py  -out service/. thrift/$file
    thrift --gen cocoa -out cocoa/. thrift/$file
    echo "$file"
done

