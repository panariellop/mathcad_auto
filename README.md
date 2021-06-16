#Mathcad Anchorage Automation 
**Written by Piero Panariello**

###About:
This program is designed to help automate the heavy lifting of data entry into Mathcad for the equipment anchorage process. It helps you view and modify values taken from an excel spreadsheet before generating a mathcad report. 

###Installation and Use:
1) Download the program and save it to any folder of your choice 
2) Double click the application to launch it 
3) Select the excel file containing the equipment and the input data. The excel sheet should follow this format:

| Equipment Name             	| Mounting Location 	| W_p 	| S_DS  	| a_P 	| R_P 	| I_P 	| z  	| h  	| A  	| B    	| a   	| b    	| H     	|
|----------------------------	|-------------------	|-----	|-------	|-----	|-----	|-----	|----	|----	|----	|------	|-----	|------	|-------	|
| Anesthesia Machine         	| Wall+Floor        	| 335 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 0  	| 75 	| 30 	| 20.5 	| 1.5 	| -1.5 	| 74.25 	|
| Warming Cabinet            	| Floor             	| 137 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 3  	| 75 	| 30 	| 21.5 	| 1.5 	| -3.5 	| 24.5  	|
| Surgical Scrub Sink        	| Wall              	| 295 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 4  	| 75 	| 64 	| 28   	| 1.5 	| -3.5 	| 39.5  	|
| Retractable Ceiling Column 	| Ceiling           	| 400 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 15 	| 75 	|    	|      	| 14  	| 14   	| 45    	|

4) Select your Mathcad template file. I have provided one to help with getting started. 
5) Click the Previous or Next buttons to scroll the equipment listed in your excel file. 
6) Click the Calculate button to preview the output values. 
7) Provide a file name and click the Generate button to generate a report for the equipment. 
**Note: use the status indicator at the bottom of the screen to view important information about the application. It will indicate if files are saved properly and the proper information is entered.**
**Note: all generated reports are saved in the folder called "Output"**