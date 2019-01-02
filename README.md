# MAIS 202 - Application Coding Challenge

Loans are an extremely powerful financial instrument; they have the potential to create opportunities and foster growth. To learn more about loans and what influence them, we have provided you with a csv file called *data.csv* that contains information about loans such as their interest rate, purpose, length, grade, and amount in a comma seperated format as shown below.

<img width="645" alt="screen shot 2018-11-20 at 12 46 36 pm" src="https://user-images.githubusercontent.com/10730760/48796196-fc966b80-eccc-11e8-838e-720310b743c3.png">

## Instructions

Your challenge will be as follows:

1. Make a copy of this repository on your own personal github account (you can fork or download it). 

2. Write a python script which loads the dataset, parses the information, and uses it to calculate the average interest rates for each of the listed purposes. 

3. Plot the results onto a graph.

## Sample Results

The output of your script should be similar to the results shown below. 

<div style="display=block;">

<img width="200" alt="screen shot 2018-11-20 at 12 53 02 pm" src="https://user-images.githubusercontent.com/17223266/50552772-788ab880-0c68-11e9-81d1-9441d1cc858a.png" style="float=left;">

<img width="500" alt="screen shot 2018-11-20 at 2 04 19 pm" src="https://user-images.githubusercontent.com/10730760/48796324-4717e800-eccd-11e8-9b14-a479928905f3.png" style="float=left;">

</div>

# Instructions
Simple script written using Python 3.5 to parse through a csv and calculate the average interest rate of a loan based on loan purpose.

## (Optional) Setup Virtual Env
```
virtualenv -p python3 <name of virtual environment>
source <name of virtual environment>/bin/activate
```

## Install packages
* Numpy
* Matplotlib
* Pandas
```
pip install -r requirements.txt
```

## Run script
With data.csv in the same directory, run the following command
```
python interest_avg.py
```

## Output
![Graph](./readme_img/graph.png)

![Table](./readme_img/table.png)


