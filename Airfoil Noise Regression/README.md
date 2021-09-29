# Airfoil Self Noise Regression


## Table Of Content 
* [Overview](#overview)
* [Motivation](#motivation)
* [Technical Aspect](#technical-aspect)
* [Results](#results)


## Overview

A Machine Learning model based on Regression used to predict the self noise of an airfoil [NACA 0012](http://airfoiltools.com/airfoil/details?airfoil=n0012-il).Noise genrated by the airfoil is depend on some parameters like frequency,chord length and more.we took some of the parameters to create a regression model and detect the self noise.

## Motivation

Belonging from Aeronautical background,I knew creating protype models to perform analysis is an hectic job.Other way around is an CFD model to perform such experiments,but changing a single parameter in CFD required to run entire model.So i got the idea of an regression model.Though this is for a single airfoil, its possible to train model for a multiple airfoils.This will give us the near value of noise genration without performing the experiment ifself.  

## Technical Aspect

* This Notebook contains basic regresion technique like -
    - ordinary least square method.
    - Linear regression model.
    - Stochastic Gradient Descent.
- Using this methods I calculated coefficient of different features that are related with our target feature.
- After that I created an joblib file that contains the trained model and can be used directly to predict noise of NACA 0012 Airfoil.

## Results

|Features|OLS Model|Linear Regression Model|SGD Regressor Model|SGD|
|--------|---------|-----------------------|-------------------|---|
|const|124.836|124.754|124.753|122.533|
|Frequency|-4.041|-4.076|-4.007|-3.658|
|Angle of attack|-2.496|-2.578|-2.471|-1.465|
|Chord length in meters|-3.337|-3.344|-3.257|-2.649|
|Free-stream velocity|1.554|1.572|1.478|1.367|
|Suction side displacement thickness|-1.936|-1.833|-1.937|-2.383|

<b>From Different model we found the coefficents of diffrent features affecting noise genration of airfoil.</b>
