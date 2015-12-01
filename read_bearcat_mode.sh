#!/bin/bash
#function:check the mode of array 
#date:2015.08.23
#writer:Jinli
function check_ping()
{
    ping -c 1 -W 2 $1 >/dev/null 2>&1 && return 0 || return 1
}

function get_sp_mode()
{
    ip=$1
        #ip_vm=$(ifconfig -a | grep inet | grep -v 127.0.0.1 | grep -v inet6 | sed 's/^.*addr://g' | sed 's/  Bcast.*//g')
        password=c4proto!

    /usr/bin/expect <<EOF
            set timeout -1
            spawn ssh root@$ip
                    expect {
                            "Windows Authentication" { exit 1 }
                            "(yes/no" {
                                    send "yes\r";exp_continue
                                    expect "Password:"
                                    send "$password\r"
                    				expect "~>"
                    				        send "/sbin/get_boot_mode >> /root/mode_$ip.txt\r"
                    				expect "~>"
                    				send "exit\r"
                    				         }
                            "Password:" { send "$password\r"
                    expect "~>"
                            send "/sbin/get_boot_mode >> /root/mode_$ip.txt\r"
                    expect "~>"
                    send "exit\r"
                }
                            "~>" {
                            send "/sbin/get_boot_mode >> /root/mode_$ip.txt\r"
                    expect "~>"
                    send "exit\r"
                }
				eof {exit 1}
                  }

                spawn scp root@$ip:/root/mode_$ip.txt /home/
                    expect {
                            "(yes/no" {
                                    send "yes\r";exp_continue
                                    expect "Password:"
                                    send "$password\r";exp_continue
                                    expect "100%"
                                    send ""
                             }
                            "Password:" {
                                    send "$password\r";exp_continue
                                    expect "100%"
                                    send ""
                            }
                    "100%" {
                                    send ""
                    }
                    }
            expect eof
EOF
    return 0
}

function checkmode()
{
        ip=$1
    machinespec_sp=$2
    echo "" > /home/mode_$ip.txt
    get_sp_mode $ip
   # [[ -f /home/mode_$ip.txt ]] || return 0
    grep "Normal Mode" /home/mode_$ip.txt > /dev/null && { printf "%-20s %-20s %-20s\n" $machinespec_sp $ip "Normal Mode" >> /home/mode.txt;rm /home/mode_$ip.txt;return 0; }
    grep "Service Mode" /home/mode_$ip.txt > /dev/null && { printf "%-20s %-20s %-20s\n" $machinespec_sp $ip "Service Mode" >> /home/mode.txt;rm /home/mode_$ip.txt;return 1; }
    grep "Rescue Mode" /home/mode_$ip.txt > /dev/null && { printf "%-20s %-20s %-20s\n" $machinespec_sp $ip "Rescue Mode" >> /home/mode.txt;rm /home/mode_$ip.txt;return 1; }
    grep "Mode" /home/mode_$ip.txt > /dev/null || { printf "%-20s %-20s %-20s\n" $machinespec_sp $ip "ssh fail" >> /home/mode.txt;rm /home/mode_$ip.txt;return 1; }
}


echo "waiting......."

[[ -f /home/mode.txt ]] && rm /home/mode.txt
 while read myline

               do 
                { echo $myline |grep "Be" > /dev/null || continue
                machinespec=$(echo $myline | cut -d ' ' -f 1)
                machinespec_spa=$machinespec"-spa"
                machinespec_spb=$machinespec"-spb"
                ip_spa=`echo $myline | cut -d ' ' -f 2`
                ip_spb=`echo $myline | cut -d ' ' -f 3`
                { check_ping $ip_spa
                                  if [ $? -eq 0 ];then
                                        checkmode $ip_spa $machinespec_spa
                                  else
                                        printf "%-20s  %-20s %-20s\n" $machinespec_spa $ip_spa "ping fail" >> /home/mode.txt
                                  fi;
                                } &

                { [[ "$ip_spb" != "" ]] && check_ping $ip_spb
                                if [ $? -eq 0 ];then
                                        checkmode $ip_spb $machinespec_spb
                                else
                                        printf "%-20s %-20s %-20s\n" $machinespec_spb $ip_spb  "ping fail" >> /home/mode.txt
                                fi;
                } 
                wait; }>/dev/null  &
            done  < machine_info.txt
           wait
                    printf "%s\n" "-----------------------------------------------------"
                    printf "%-20s  %-20s %-20s\n" "MachineSpec" "Ip" "Status"
                    printf "%s\n" "-----------------------------------------------------"
                    [[ -f /home/mode.txt ]] && cat /home/mode.txt | grep -v -E 'MachineSpec|---' | sort && rm /home/mode.txt
                    printf "%s\n" "----------------------------------------------------"
exit 0

