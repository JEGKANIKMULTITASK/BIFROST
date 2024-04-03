#!/usr/bin/env bash

for i in $(seq 0 1 90)
do
    mcrun -c --mpi=6 backend_Pb_3t.instr -d Pb_290K_20_$i -n 1000000  A4=20  A3=$i
done


for i in $(seq 0 1 90)
do
    mcrun -c --mpi=6 backend_Pb_3t.instr -d Pb_290K_15_$i -n 1000000  A4=15  A3=$i
done