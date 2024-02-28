#!/usr/bin/env bash

for i in {30..31}
do
    mcrun -c --mpi=7 backend_mockup.instr -d scan1_A4_85_A3_$i -n 1000000 --format=NeXus  A4=60  A3=$i
done



#for i in {30..35}
#do
   # mcrun -c --mpi=7 backend_mockup.instr -d scan1_A4_45_A3_$i -n 1000000 --format=NeXus  A4=45  A3=$i
#done