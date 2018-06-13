#! /bin/bash 
#    处理文本data
#    将结果写入result
#    结果包含次数和命令，如“100 ls”

$ cat data1 | cut -c 8- |cut -d ' ' -f 1 | sort -k1 -rn | uniq -dc | sort -t' ' -k1rn -k2  | head -n 3 | cut -c 5- |  > /home/shiyanlou/result
