# Custom Code for WordPress
<p align="center">
  <img src="https://raw.githubusercontent.com/AtaGowani/custom-wp-table/main/.github/table.png">
</p>
This repo contains a python script that uses data provided in your csv file to create html code to create a **table with a pop-up modal** intended to be used on your WordPress page. Created for the one and only Ammn Meghani.
## Requirements
* Python 3.x.x
## How to use
* Clone the repo locally
* Add your `.csv` file to the root of the repo. **Make sure it is named `data.csv`.** See below to look at the structure of your `.csv` file.
* Run the python script using the command `python3 create-table.csv`
* Once you run the script this will generate the `table.html` file which contains the code that needs to be copied into WordPress. This can be done by adding the "Custom HTML" block.
### Struture of the .csv file
The image below describes how data from the `data.csv` file is transfered over to the html table.
<p align="center">
  <img src="https://raw.githubusercontent.com/AtaGowani/custom-wp-table/main/.github/data_conversion.png">
</p>