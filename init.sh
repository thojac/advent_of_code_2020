if [ $# -eq 0 ]
  then
    echo "No arguments supplied"
    exit
fi

#number=$1
#day=$1

#if (($1 > 0 && $1 < 10)); then
#    day=0$day
#fi

# Init new day
day=day_$1
mkdir $day
cp template.ipynb $day/sketch.ipynb
touch $day/README.md
touch $day/input.txt
touch $day/solution.py