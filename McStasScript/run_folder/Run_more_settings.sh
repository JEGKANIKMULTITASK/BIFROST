#!/usr/bin/env bash

for i in $(seq 0 1 90)
do
    mcrun -c --mpi=6 backend_Pb_3t.instr -d Pb_290K_70_$i -n 1000000  A4=70  A3=$i
done



for i in $(seq 0 1 90)
do
    mcrun -c --mpi=6 backend_Pb_3t.instr -d Pb_290K_75_$i -n 1000000  A4=75  A3=$i
done