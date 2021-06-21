<h1>Mathcad Anchorage Automation</h1>
<b>Written by Piero Panariello</b>

<h3>About:</h3>
<p>This program is designed to help automate the heavy lifting of data entry into Mathcad for the equipment anchorage process. It helps you view and modify values taken from an excel spreadsheet before generating a mathcad report.</p>
<p>This version is still in alpha, so not all functionality is available at the moment.</p>

<h3>Installation and Use:</h3>
<ul>
<li>Go to the releases tab on this github page, find the lastest distribution and download it. Download the template files provided to get started.</li>
<li>Double click the application_v1.exe file to launch the application.</li>
<li>Select the excel file from the templates provided containing the equipment and the input data. The excel sheet should follow this format:</li>

| Equipment Name             	| Mounting Location 	| Tags         	| W_p 	| S_DS  	| a_P 	| R_P 	| I_P 	| z  	| h  	| A  	| B    	| a   	| b    	| H     	|
|----------------------------	|-------------------	|--------------	|-----	|-------	|-----	|-----	|-----	|----	|----	|----	|------	|-----	|------	|-------	|
| Anesthesia Machine         	| Wall,Floor        	| Medical, ICU 	| 335 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 0  	| 75 	| 30 	| 20.5 	| 1.5 	| -1.5 	| 74.25 	|
| Warming Cabinet            	| Floor             	| Medical      	| 137 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 3  	| 75 	| 30 	| 21.5 	| 1.5 	| -3.5 	| 24.5  	|
| Surgical Scrub Sink        	| Wall              	| Medical      	| 295 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 4  	| 75 	| 64 	| 28   	| 1.5 	| -3.5 	| 39.5  	|
| Retractable Ceiling Column 	| Ceiling           	| Medical      	| 400 	| 1.121 	| 1   	| 2.5 	| 1.5 	| 15 	| 75 	|    	|      	| 14  	| 14   	| 45    	|
</br>
<i>Note: Tags should be seperated by comma. All units are the default units indicated on the template file.</i>
<li>Select your Mathcad template file. I have provided one to help you get started (01_LPCH ERCP_Anchorage_Template.mcdx).</li>
<li>If you want to save details about the report to a database, then click "Save to database?".</li>
<li>Choose the database that you want to make an entry into. You can leave this field blank, and the software will automatically generate a database file saved to the same folder as the generated reports. </li>
<li>Click the Previous or Next buttons to scroll the equipment listed in your excel file. </li>
<li>Click the Calculate button to preview the output values. 
<li>Provide a file name and click the Generate button to generate a report for the equipment. </li>
<li>The application is processing your request when the button you clicked turns white. Please be patient - the Mathcad API is a little slow.</li>
</ul>
<b>Note: use the status indicator at the bottom of the screen to view important information about the application. It will indicate if files are saved properly and the proper information is entered.</b> </br>
<b>Note: all generated reports are saved in the folder called "mathcad_automation_output".</b>


<h3>Using your own files:</h3>
<ul>
<li>To use your custom template, just choose it using the graphical user interface.</li>
<li>If you decide to create your own custom template, then ensure that the inputs and outputs follow the format of the template provided</li>
</ul>