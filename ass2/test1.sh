!/bin/dash

for i in 1 2 3
do
    echo $i
done

echo hello world # This is also a comment
echo *


for file in *.c
do
    echo $file
done

echo What is your name:
read name

echo What is your quest:
read quest

echo What is your favourite colour:
read colour

echo What is the airspeed velocity of an unladen swallow:
read velocity

echo Hello $name, my favourite colour is $colour too.