#!/bin/bash
#多线程函数
function thread {
        pipefile=/tmp/$$.fifo
        mkfifo $pipefile
        exec 5<>$pipefile
        rm -rf $pipefile

        for ((i=0;i<$1;i++))
        do
                echo
        done>&5
}
#设定线程数
thread 5
#多线程指令
while true
do 
 read <&5
  #CPU负载100%指令
  (dd if=/dev/zero of=/dev/null;echo>&5)&
done
wait
exec 5>&-
