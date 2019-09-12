#! /bin/bash 
###########################################
#
###########################################

# constants
baseDir=$(cd `dirname "$0"`;pwd)

# functions

# main 
[ -z "${BASH_SOURCE[0]}" -o "${BASH_SOURCE[0]}" = "$0" ] || return
cd $baseDir/..

if [ ! -f $baseDir/localrc ]; then
  echo "Copy sample localrc as localrc and modify it."
  echo "cp " $baseDir/localrc.sample $baseDir/localrc
  exit 1
else
  source $baseDir/localrc
fi

python tests/tst-demo.py  --verbosity 1 --CL_HOST=$CL_HOST --CL_PORT=$CL_PORT
