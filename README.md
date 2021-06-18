<h2>Mathcad Anchorage Automation</h2>
<b>Written by Piero Panariello</b>

<h4>About:</h4>
<p>This program is designed to help automate the heavy lifting of data entry into Mathcad for the equipment anchorage process. It helps you view and modify values taken from an excel spreadsheet before generating a mathcad report.</p>
<p>This version is still in alpha, so not all functionality is available at the moment.</p>

<h4>Installation and Use:</h4>
<ul>
<li>Click on the green Download Code button on Github and download the zip file. Save and extract it to any folder of your choice.</li>
<li>Double click the application_v1.exe file to launch the application</li>
<li>Select the excel file from the templates folder containing the equipment and the input data. The excel sheet should follow this format:</li>

| Equipment Name             	| Mounting Location 	| Tags         	| W_p 	| S_DS  	| a_P 	| R_P 	| I_P 	| z  	| h  	| A  	| B    	| a   	| b    	| H     	|
|----------------------------	|-------------------	|--------------	|-----	|-------	|-----	|-----	|-----	|----	|----	|----	|------	|-----	|------	|-------	|
| Anesthesia Machine         	| Wall+Floor        	| Medical, ICU 	| 335 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 0  	| 75 	| 30 	| 20.5 	| 1.5 	| -1.5 	| 74.25 	|
| Warming Cabinet            	| Floor             	| Medical      	| 137 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 3  	| 75 	| 30 	| 21.5 	| 1.5 	| -3.5 	| 24.5  	|
| Surgical Scrub Sink        	| Wall              	| Medical      	| 295 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 4  	| 75 	| 64 	| 28   	| 1.5 	| -3.5 	| 39.5  	|
| Retractable Ceiling Column 	| Ceiling           	| Medical      	| 400 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 15 	| 75 	|    	|      	| 14  	| 14   	| 45    	|
</br>
<i>Note: Tags should be seperated by comma. All units are the default units indicated on the template file.</i>
<li>Select your Mathcad template file from the templates folder. I have provided one to help with getting started (01_LPCH ERCP_Anchorage_Template.mcdx)</li>
<li>Click the Previous or Next buttons to scroll the equipment listed in your excel file. </li>
<li>Click the Calculate button to preview the output values. 
<li>Provide a file name and click the Generate button to generate a report for the equipment. </li>
<li>The application is processing your request when the button you clicked turns white. Please be patient - the Mathcad API is a little slow.</li>
</ul>
<b>Note: use the status indicator at the bottom of the screen to view important information about the application. It will indicate if files are saved properly and the proper information is entered.</b> </br>
<b>Note: all generated reports are saved in the folder called "Output"</b>


<h4>Including your own files:</h4>
<ul>
<li>If you want to include your own excel and mathcad template files, then simply copy them into the templates folder. </li>
</ul>
<b>Note: Do not delete any folders!</b></br>