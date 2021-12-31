
   # NOW SEND WARNING if trafficlight file is not present in /users_home/csp/sp1/SPS/CMCC-SPS3.5/logs/TAPEARCHIVE/$st/$year
   declare -i trafficlight=10
   if [ ${trafficlight} -ge 1 ]; then
    body="Warning on login03 - You are trying to remove a pre-existing file from TAPE, before crsync it, with: crm dirtocreatefile \n
      This procedure is not allowed by default, unless you are completely sure about it. \n
      To let the program remove file from tape and sync it again for caso you must create a trafficlight file by: \n
      touch file_${trafficlight} \n
      and wait the crontab laucher restart automatically the case_tape_archive.sh for caso . \n
            Script is dirutil ...."
    title="[TAPEARCHIVE] SPS3.5 WARNING"
    #sendmail
    #${DIR_SPS35}/sendmail.sh -m $machine -e $mymail -M "$body" -t "$title"
    #echo $title
    title="${title// /_}"
    title="${title//[/_}"
    title="${title//]/_}"
    #echo $title
    touch $title.txt
    echo $body > $title.txt
    exit 1
  fi
