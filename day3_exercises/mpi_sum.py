#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 11:08:24 2023

@author: marmo435
"""

from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

rank_list = comm.gather(rank)

if rank == 0:
    print("Sum of all ranks: ", sum(rank_list))