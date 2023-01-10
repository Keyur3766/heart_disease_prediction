# Heart Disease prediction

<b> Key-terms : Heart Disease, Machine Learning, Classification Techniques, K-Nearest Neighbors, Logistic Regression </b>

This project aims to build a Webpage that enables the user to find out whether he has the risk of heart disease or not. A website will automatically determine whether a person has heart disease or not using various machine learning classification techniques, such as K-nearest neighbor, Logistic Regression, Linear Regression, etc. The user must provide certain inputs, such as age, gender, cholesterol level, blood pressure level, etc. The main goal here is to find the best model with higher accuracy that can solve the problem by countering the risk of the wrong prediction.  


<h3> Exploratory Data Analysis </h3>

Exploratory Data Analysis (EDA) was carried out to get more insights on the dataset. The correlation analysis of 11 attributes with the output (12th attribute in our dataset) was performed. Removing the correlation is important because the correlation between the attributes can result in false predic- tions. All the attributes have a correlation value less than 0.41 with our output. Hence we can conclude that our attributes aren’t highly correlated.


![image](https://user-images.githubusercontent.com/75409140/211493261-06e0bffa-8f83-46c2-9556-21666c5bf19f.png)



<h3> Confusion matrix for KNN </h3>

<img width="305" alt="image" src="https://user-images.githubusercontent.com/75409140/211493708-72ed35d8-fa92-40a7-9d1a-a677a4084255.png">

<center> Accuracy = 72.36% </center>


<h3> Confusion matrix for Logistic Regression </h3>

<img width="308" alt="image" src="https://user-images.githubusercontent.com/75409140/211493977-794e1213-2a46-4f49-9333-d3107b575732.png">

<center> Accuracy = 71.68% </center>


