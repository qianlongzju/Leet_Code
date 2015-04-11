cat words.txt | tr ' ' '\n' | sed -n '/[a-z]/p' | sort | uniq -c | sort -r -n | awk '{print $2, $1}' 
