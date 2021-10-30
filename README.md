# REGRESSION ANALYSIS
---

## OVERVIEW
* Regression Analysis / Regression Algorithm is one of the basic technique in Machine Leaning.
* Regression used to predict the continueos number in a specific trend depend upon the other parameters.
* This trend we are predicting is the dependant variable and upon which we analysing the dependant variable is/are the independant variable /variables.
* There are serval methods to do a regression analysis , depend upon the data we are analysisng. will see in the article about it. 

## Introduction
<p>The first thing people think as they hear about regression is 'Linear Regression' and 'Logistic Regression'.Its becausue people assumes that this are the  only algorithms for regression  or some think this are the only important one  over other. </p>
<p>There are different types of Regression algorithms that we can use. Each has their specific advantage and a specific condition where it can be applied more effectively.Beacause it's not the case that the line alaways FIT!</p>
<p>I took Some of the examples of this different algorithms in this Repository.</p>

## Table Of Content :
1. [What is Regression](#What-is-Regression)
2. [Types of Regression](#Types-of-Regression)
    * [Linear Regression](#Linear-Regression)
    * [Logistic Regression](#Logistic-Regression)
    * [Polynomial Regression](#Polynomial-Regression)
    * [Ridge Regression](#Ridge-Regression)
    * [Lasso Regression](#Lasso-Regression)
    * [ElasticNet Regression](#ElasticNet-Regression)
    * [Stepwise Regression](#Stepwise-Regression)
3. [How to select right Regression Algorithm](#How-to-select-right-Regression-Algorithm)

## What is Regression
<p>The Releation between an depndant variable (Target) and the independant variable/variables (Features) that use to predict the target value in continueos number format is regression.This technique can be used  to predict the pattern or effect of parameters on a specific feature/target.For example , The Relation of various paramters like size of tyre , weight of veichale , days scince last service , Air Pressure in Tyres ,Type of material used in specific parts and more paramters that cann't be explained by a mathematical formula  and how they affect on the performance of a veichale or  economy can be predicted by using regression analysis.</p></br>
<p>We Fit the data points in n-dimensional space and find a perfect line/plane/curve passing through the points in such a way that the distance between the points and the plane/line/curve is minumum.This is called Best fit line.(For convinence we assuming data in a 2-D Plane that refers to using curve or line.)</p>

## Types of Regression
The Basic metrics that divide the regression techniques are : </br> 
    <p>- Number of Independant Variable.</p>
    <p>- Type of Dependant Variable.</p>
    <p>- Shape of Regression line.</p>

### Linear Regression
The one of the most widely knows and mostly used regression technique.The nature of the regression line say the best fit line is Linear hence its called as **Linear Regression**.
Basic Equation on which Linear regression works is <img src="https://render.githubusercontent.com/render/math?math=Y=a+b(X)+e">  , where a is intercept,b is slope and e is error.<br>
The Linear Regression can be classified as :<br>
<li>Simple Linear Regression</li>
<li>Multiple Linear Regression</li>
<p> It is simple to classify as Simple Linear Regression is one with having only one independant variable on which the target variale dependant.But in Multiple Linear Regression the target variable depndant on more than one independant variable.</p>
Example of Best Fit line in Linear Regression:<br>

<img src=https://static.wixstatic.com/media/02b811_fc93f61330d84649888709f7755c5dab~mv2.png/v1/fill/w_1000,h_626,al_c,usm_0.66_1.00_0.01/02b811_fc93f61330d84649888709f7755c5dab~mv2.png width=700 height=400>

### Logistic Regression
Logistic is mostly considerd as a classification technique beacause it use to predict a outcome in a binary format ( yes/no , 1/0).But as it actually finds the probabilities of an event and its  log odds.Hence LOGIt Function is used in Logistic Regression.This predict the maximum likelihood of an event rather than minimizing the sum of errors:
The Equation for Logistic Regression :

<image src=https://quantifyinghealth.com/wp-content/uploads/2021/05/Logistic-regression-equation.png>


And the Best Fit line / curve  is like :

<image src=https://editor.analyticsvidhya.com/uploads/711091.png width=700 height=400>

### Polynomial Regression

If the Linear line of linear regression gives high sum of square error and on plot we able to detect that the data is curvy in nature rather than linear, we can plot a curve.It shows that the independant variable has  degree more than 1.<br>
Equation For Polynomial regression :<img src="https://render.githubusercontent.com/render/math?math=y=a+(b*x^2)">
                               

The Best Fit Line looks like :

<image src=https://static.wixstatic.com/media/2d2ac8_67543b18eadb49568976e64ac909fb91~mv2.png/v1/fill/w_1000,h_519,al_c,usm_0.66_1.00_0.01/2d2ac8_67543b18eadb49568976e64ac909fb91~mv2.png width=700 height=400>

### Ridge Regression

Ridge Regression used in special cases according to the data.Data consisting multiple features and they show multicolinearity .It works on the principal od Bias-Variance Tredoff. when a model has high variance , some degree of bias added for lowering  variance and getting good results.This added bias in the error with a **Shrinkage Parameter** <img src="https://render.githubusercontent.com/render/math?math=\lambda">(lambda).This extra term added called as Penalty.The penalty in Ridge regression can make coefficent close to 0.<br>
* This is an reguliztion method and uses L2 Regulizaion.<br>

**Formula :**<br>
<image src=https://i.ytimg.com/vi/Ddc5z-YujOQ/maxresdefault.jpg  width=700 height=400>

### Lasso Regression
Lasso (Least Absolute Shrinkage and Selection Operator)) is similar to the Ridge, the only difference between them is the penalty.Lasso can shrink the size of regression coefficent to absolute 0.That makes the elemination of an variable.causing feature selection,reducing multicolinearity and improving accuracy of model.The Shrinkage paramter here is <img src="https://render.githubusercontent.com/render/math?math=\alpha">(Alpha).<br>
* This is a Regulization method and uses L1 regulization.

Formula :<br>
<img src= https://user.oc-static.com/upload/2019/10/07/15704536640472_lasso.png>

### ElasticNet Regression

ElasticNet is a combined method of Ridge and Lasso Regression.When There are multiple features that are correlated ElasticNet is useful.It is an trade off method between Lasso and Ridge.
<br>
Formula : <br>
<img src=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAXAAAACGCAMAAADzeyG9AAAAilBMVEX///8AAAD//+q6cgByuur/6rrq//8AcrpyAACb1P/U///UmwDqunIAAJv//9S66v//1JsAm9SbAACbAHIAAHJyAJu6cnJyAHJycrq6cpsAcnKbcrrU/9SbAJsAm7rq1Juburr/1Lrq6roAcpubcpvU/+q6mwDUunKb1NS66tRyutTq/9Sb1Oq617rJjRHHAAAITElEQVR4nO2dCZebRgzHYX0vrEPctE2btkmb3sf3/3plLhjNwTAaMY4T/d/bt89gC80PoTnActOwWCwWi8VioTW07el4bye+IB3eHq+3y729+LL09N3zvV3I1OHctm9e4fffRV1rckn/cAF+OO+L9t9JTzsJvP8knVtUPeB9SxiNCvjIe8g0SuoFRvWAP+2ogYt0l8uP1AuMHhn43b3ACAAd2g/ndh/fX6SxqUN2QMaN4YHTeYERBNqdjgNsCSnw6zuqaUoJcDovMHKAX5oNgRNGVgHwu8Z3XeCXvqUzho9wOi8wcnL4yw83GACUw8KXZ7K2ooGTeoHRY098HlAMvLIYeGUx8MpSQPvW08XeX6S4cbzygW/hBUYK6Dg6fbEXlsfXdMDjxkts5gLfwguMNNDDuX0NN9MBjxvHC5FSNvACIwN0vOJsstMaD0kOjxnHC5PD6b3AaALawRs7HSXwmHG8UJ0muRcYTUCvt+AdcBrgEeN4oYCTe4HRDNTNce7+wsOEjHvq/DcNL6HbxLhhYcCL61fuDVt/C6ksoH1ooEQ1Dg8adxR+5iG4FTkO9724J/Axx/nRFAXudvJdgkDIONTTLnyow9f+B7ETH8+LZeDiJh5xFrKBhnJcDHjvv/PbxchIJ9Bw8mhMogGNTwF3R91RLxRe27YF/Hrbj39rcmFUveuGszzrLVxGgIeiLgosahwoFuDaMGx8ELj10MRwiZhzvZB4gW0LuKTlh1aOloEHclwYeLA1cWIx40Dxp9bkHtj4FPBRQzgyHS8kXmDbAi7TZKAjLxEE6l+JZq3lMu6bjxxOH4lYcI07RofoA17yTMLGrwB+/TF4wTleSLzAtg38tRWi4uac0nTorhW2zG2bMV2Jne/ly9NRntlx37Pab8w4ETx+CJ5Qtf9wFlvnmJEXubw9aPufyCmucceoatnYhsvBfXRANBw0flWER04g9EIBt20D4NdbvE3iwpN4ho+//ra7iNiR8SMgyyaI8zioM/IsspZuNWzb4IS43i9P/9M3xhUVy9KI5V+i2/SMQ6P6+hBeunNAuQ00Pg08vjgFvNDALdtOhC+Pi+XFp06tTHyGsdzeG+Bmg5BrL/K6l2ym1QcNR0SFlSr1SDFw7YWNQ6MmIXWn311SCrj9eRe4f8z+9D46oLV2TBE+T7kh8Cn0/UPILXtzZc8RngPcixwQ4S7w8aTOUZ+OcNd4FwRu9xXmjRq4nVATET66dngb7FLgRyfgk20XeDRRiuaqCFfvEDlcmM4CHhvFSBozUONEd/pD+KRTQCqHu8aNUXXSzN7uT5nuRpvTyTQ5XBxBbUwCH62pXtNzCnoxAze2beBvXi2M+EUm6a0IN97OwDXsBeD+GvG0Xr63h30G/eFs90yJUYpnHBrVnVx3aaYORkuNUkDjU8Cl293+579u3zszBscLBdy2bQP/abcw0xQZ5e+d7OPNGKJV/eXpKPp+8YWYX87qT2zYz55NR/dnVWb/oNNV++E8emAwqf9De5lfRBUwro2qR4hlpzN6LQdUe2HTPFqsuiPdeLUxAfxpJxAMYjjiTNFcLxRw27abUtZKZrDUXMQB3qXXUrrTP++O04Wqv/GhUkoiowSMa6k07vgqUsrOSlWm8ebNyWGhaQAE7noxpxRjGwu8V/Ph1BKdDTQ0cvWAz13cSFs3UW5MdJnxeY0BC0+YBVy2ewXwoCBwzws64CqlJJdELaDBEWcM+Ljj352ZQXSX5Grh0nBWg4UhPgNXyEiA+14sAt9C8aFt0MUh9A2rIb2EuQjIRLJ9PQqbartzlWYC71prtSrwKYC3LvA+eM0T3YAIG9eax/LwGpbb3Z5hYViI8QICd4aFW2gCGnlqgAb44iMJsZ59aUkSBTz1YER6iEEgA9QdLpkxNQnwmHG8MMDpvcDIAHWHS+biJgEeM44XBji9FxhpoIMznlFLpw0N8KhxvBDAN/ACI7Pe7T3pGFlNRB0iZhyvfOBbeIGRBDqvPG4AfMF4idFM4Jt4gRE/H15ZDLyyGHhlTcNC0IXP0zsK4PZdofRtinUm84Fv4AVGYPFK9CTj7PdqrdpTRbgxfvXuCKCEjHBiLzAKj8MPpMBhjZLQQ1vZQgDfwAuMwimFFjj8rsG9gG/gBUYW8CmlbAF8Nn5P4MReYMQRXllTDrcbYK3akwPvSKZ4pcBpvMCoxjgcDshIVDwsvJsqAN9iXR/zxdhPYwbHM83KevDKnCwWi8VifRbirq26Hnfw9qBi4ERaW4SbgRNpbTEdBk4kBl5Za4twM3AirS3CzcCJtLYINwMn0toi3AycSGuLcDPwymLglcXAK4uBVxYDL1VmEW4GXqrMItwMvFh5RbgZeLmyinAzcALlFOFm4ATKKcLNwCm0ohS4+flzBk6iZCnw6efPGTiN0qXAdTEsBp6n1UW4hWBt814XVWLgSWGKcDduee/eVNlj4ElhinA3Tglu8/PnDHyFMEW4G1iCe/r5cwa+Qpgi3I1b3luLga8Qpgh3E6ltzsCXhS7C3URqmzPwFcIU4W6cEtzRd7F8hYpwD96D3l66huW9tRj4CgWKcP9npurWHu9XA0K1zRn4CgWLcJu61VqBUuCwvPdkgYEnFSzCrafqRoFS4LD4cWNeMHCc0oNzBk4pM1VXCn4bnIETapqqSy1TZODkWiwF3vCwkFqpByPgygADL1VWEW4GXq6sItwMvFh5RbgZeKkyi3Az8ELlFuFm4JXFwCuLgVcWAy+WU20xUYWbgZMoWGc8KAZerD5WZzwoBl4s5xsPDHxrwSLcDHxzcYRXFgSeqsLNwIuVV4SbgZcqswg3A68qrszJYrFYrLvof1LvasopQXSAAAAAAElFTkSuQmCC>

### Stepwise Regression

When the data is huge and has multiple independant variables and we unware of their importance on targt variable, Stepwise Regression can be used for better results.This Method uses automatic selection of features.This method apply metrics like R-square,AIC,t-stats on variables to find it's importance.and then create regression multiple times by adding and droping the variables.<br>
Steps:
* Standerd Stepwise regression adds and removes features at each step.
* Forward selection start with most important features and then add features at each step.
* Backward Elemination Starts with removing the least important fetures at each step.

## How to select right Regression Algorithm

Higher the number of options available , more difficult it becomes to choose the right one. A similar case happens with regression models.

Within multiple types of regression models, it is important to choose the best suited technique based on type of independent and dependent variables, dimensionality in the data and other essential characteristics of the data. Below are the key factors that one should practice to select the right regression model:

1. Data exploration is an inevitable part of building predictive model. It should be first step before selecting the right model like identify the relationship and impact of variables.
2. To compare the goodness of fit for different models, we can analyse different metrics like statistical significance of parameters, R-square, Adjusted r-square, AIC, BIC and error term. Another one is the Mallow’s Cp criterion. This essentially checks for possible bias in your model, by comparing the model with all possible submodels (or a careful selection of them).
3. Cross-validation is the best way to evaluate models used for prediction. Here you divide your data set into two group (train and validate). A simple mean squared difference between the observed and predicted values give a measure for the prediction accuracy.
4. It’ll also depend on objective. It can occur that a less powerful model is easy to implement as compared to a highly statistically significant model.
5. Regression regularization methods(Lasso, Ridge and ElasticNet) works well in case of high dimensionality and multicollinearity among the variables in the data set.
   






