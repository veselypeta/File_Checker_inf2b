#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:19:48 2019

@author: Petr Vesely
"""
def check_files (env = 'py'):
    import os    
    current_files = os.listdir()
    
    # Report Files
    required_files = ['report_task{}.pdf'.format(i) for i in range(1,3)]
    # Common Funcions
    required_files += (['My{}.{}'.format(x,env) for x in ['Mean', 'Cov', 'SqDist']])
    
    #All Task Files
    required_files += ['task1_{}.{}'.format(i, env) for i in range(1,9)]
    required_files += ['task2_{}.{}'.format(i, env) for i in range(1,9)]
    
    # Other function files
    required_files.append('comp_pca.{}'.format(env))
    required_files.append('my_kMeansClustering.{}'.format(env))
    required_files.append('run_knn_classifier.{}'.format(env))
    required_files.append('comp_confmat.{}'.format(env))
    required_files.append('run_gaussian_classifiers.{}'.format(env))
    required_files.append('run_mgcs.{}'.format(env))
    
    
    # Required MAT Files
    required_files.append('task1_2_M.mat')
    required_files += ['task1_3_{}.mat'.format(arg) for arg in ['evecs', 'evals' ,'cumvar', 'mindims']]
    # Task 1.5
    required_files += ['task1_5_{}_{}.mat'.format(arg, k) for arg in ['c', 'idx', 'sse'] for k in [1,2,3,4,5,7,10,15,20]]
    required_files += ['task1_7_dmap_{}.mat'.format(k) for k in [1,2,3,5,10]]
    required_files += ['task2_1_cm{}.mat'.format(k) for k in [1,3,5,10,20]]
    required_files += ['task2_2_dmap_{}.mat'.format(k) for k in [1,3]]
    required_files.append('task2_4_corrs.mat')
    required_files += ['task2_5_{}.mat'.format(arg) for arg in ['cm', 'm10', 'cov10']]
    required_files.append('task2_6_dmap.mat')
    required_files += ['task2_7_cm_{}.mat'.format(r) for r in range(30,100,10)]
    required_files += ['task2_8_cm_{}.mat'.format(l) for l in [2,5,10]]
    required_files += ['task2_8_g{}_{}.mat'.format(l, arg) for arg in ['m1', 'cov1'] for l in [2,5,10]]
    
    # Required .pdf files
    required_files += ['task1_1_imgs_class{}.pdf'.format(k) for k in range(1, 11)]
    required_files.append('task1_2_imgs.pdf')
    required_files.append('task1_3_graph.pdf')
    required_files.append('task1_4_imgs.pdf')
    required_files += ['task1_6_imgs_{}.pdf'.format(k) for k in [1,2,3,4,5,7,10,15,20]]
    required_files += ['task1_7_imgs_{}.pdf'.format(k) for k in [1,2,3,5,10]]
    required_files += ['task2_2_imgs_{}.pdf'.format(k) for k in [1,3]]
    required_files.append('task2_3_img.pdf')
    required_files.append('task2_6_img.pdf')
        
    
    # Missing Files
    missing_files = []
    for req_file in required_files:
        if req_file not in current_files:
            missing_files.append(req_file)
    
    # Print The Results
    if missing_files == []:
        print("All Files are present!")
    else:
        print("You are missing the following files")
        for f in missing_files:
            print(" -- > {}".format(f))
    
    return missing_files

while True:
    env = input("Type 'py' for Python and 'm' for MATLAB -----  ")
    if env == 'py' or env == 'm':
        break
    else:
        env = input("Type 'py' for Python and 'm' for MATLAB -----  ")

a = check_files(env=env)
input("Press any key to exit")