#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import ADS1263
import RPi.GPIO as GPIO
import csv

REF = 5.08          # Modify according to actual voltage
                    # external AVDD and AVSS(Default), or internal 2.5V


try:
    ADC = ADS1263.ADS1263()
    
    # The faster the rate, the worse the stability
    # and the need to choose a suitable digital filter(REG_MODE1)
    if (ADC.ADS1263_init_ADC1('ADS1263_50SPS') == -1):
        exit()
    adc_mode = input('Select ADC mode: 0-SingleChannel 1-Differential')
    if adc_mode!='1' and adc_mode!='0':
        adc_mode = 1
    else:
        adc_mode = int(adc_mode)
    ADC.ADS1263_SetMode(adc_mode) # 0 is singleChannel, 1 is diffChannel
    print(f'ADC mode {adc_mode}')
    # ADC.ADS1263_DAC_Test(1, 1)      # Open IN6
    # ADC.ADS1263_DAC_Test(0, 1)      # Open IN7

    ADC_Value = []
    isSingleChannel = True
    iteration = 0
    while iteration < 1000:
        ADC_Value.append(ADC.ADS1263_GetChannalValue(0))
    save_filename = 'data_'+str(time.time())+'.csv'
    with open(save_filename,'w') as f:
        write = csv.writer(f)
        write.writerow(ADC_Value)


    ADC.ADS1263_Exit()

except IOError as e:
    print(e)
   
except KeyboardInterrupt:
    print("ctrl + c:")
    print("Program end")
    ADC.ADS1263_Exit()
    exit()
   
