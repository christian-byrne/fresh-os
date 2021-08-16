#!/bin/bash
# Setpup SSH public key first.

IP='143.198.57.139'
USERNAME='root'

if [[ $1 == "connect" ]]
then
    ssh $USERNAME@$IP
elif [[ $1 == "transfer" ]]
then
    sftp $USERNAME@$IP
elif [[ $1 == "website" ]]
then
    if [[ $2 != '' ]]
    then
        arg=$2
        if [[ ${arg:0:1} == ":" ]]
        then
            nohup >/dev/null google-chrome http://$IP$2 & disown
        else
            nohup >/dev/null google-chrome http://$IP/$2 & disown
        fi
    else
        nohup >/dev/null google-chrome http://$IP & disown
    fi
elif [[ $1 == "upload" ]] || [[ $1 == "download" ]]
then
    folder=$(pwd | xargs basename)
    if [[ $1 == "upload" ]]
    then
        echo "put -R * ./$folder/" > sftp-batch-command.txt
    elif [[ $2 != '' ]]
    then
        echo "get -R ./$2/ ./" > sftp-batch-command.txt
    else
        echo "get -R ./$folder/ ./" > sftp-batch-command.txt
    fi
    sftp $USERNAME@$IP -b sftp-batch-command.txt
    rm sftp-batch-command.txt
elif [[ $1 == "ports" ]]
then
    lsof -nP -iTCP -sTCP:LISTEN
elif [[ $1 == "persist" ]]
then
    touch server-logs.txt; nohup >> server-logs.txt node . & disown;
else
    echo $IP
fi
