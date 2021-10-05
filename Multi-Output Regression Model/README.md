# Gas Turbine - NOX and CO emmission prediction


## Table Of Content 
* [Overview](#overview)
* [Motivation](#motivation)
* [Technical Aspect](#technical-aspect)`m
* [Results](#results)


## Overview
Multivariate or Multi-Output regression are the problems having more than one vairable to predict.One of the such case is this Gas Turbine CO and NOx Emission Data Set .Here We need to predict the emission of two gases from the data available


## Motivation

One target vaariable affected by other features in datasetcan be a problem to solve.but considering two might be a challenge.there are problems that requires two variable to be detected at same instance.like co-oridnates ,price of house and area of house , price of car and Milage etc. a multioutput regression can be useful in such scenario rather than creating two different models. 

## Technical Aspect

* This Notebook contains multioutput regresion technique using-
    - Linear Regression.
    - Decision Tree Regression.
- Using both kind of scaler transformation and two regression algorithms,Decision tree Regressor and Linear Regression a Multioutput model is built. 
- One of the model giving best result taken for individual regression of target variable keeping one target variable constant.

## Results
    
|Results|By Multioutput Model|By Combining Result|
|-------|--------------------|-------------------|
|R2 score|0.637|0.682|
|MSE|12.427|12.376|
|RMSE|3.525|3.518|

<b>The results I got from both methods are close toeach other , its just the prefrence we need to decide based on the Time we have for prediction either by  multioutput model or individual model.</b>
