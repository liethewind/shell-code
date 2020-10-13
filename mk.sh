#!/bin/bash
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
thread 5
while true
do 
 read <&5
  (dd if=/dev/zero of=/dev/null;echo>&5)&
done
wait
exec 5>&-
