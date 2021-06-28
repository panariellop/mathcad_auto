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

| eqpt\_name                 | mounting\_location | tags         | w\_p\_input(lb) | s\_ds\_input | a\_p\_input | r\_p\_input | i\_p\_input | z\_input | h\_input | capital\_a\_input(in) | capital\_b\_input(in) | a\_input(in) | b\_input(in) | capital\_h\_input(ft) | omega\_input |
| -------------------------- | ------------------ | ------------ | --------------- | ------------ | ----------- | ----------- | ----------- | -------- | -------- | --------------------- | --------------------- | ------------ | ------------ | --------------------- | ------------ |
| Anesthesia Machine         | Wall, Floor        | Medical, ICU | 335             | 1.121        | 1           | 2.5         | 1.5         | 0        | 75       | 30                    | 20.5                  | 1.5          | \-1.5        | 74.25                 | 2.5          |
| Warming Cabinet            | Floor              | Medical      | 137             | 1.121        | 1           | 2.5         | 1.5         | 3        | 75       | 30                    | 21.5                  | 1.5          | \-3.5        | 24.5                  | 2.5          |
| Surgical Scrub Sink        | Wall               | Medical      | 295             | 1.121        | 1           | 2.5         | 1.5         | 4        | 75       | 64                    | 28                    | 1.5          | \-3.5        | 39.5                  | 2.5          |
| Retractable Ceiling Column | Ceiling            | Medical      | 800             | 1.121        | 1           | 2.5         | 1.5         | 15       | 75       |                       |                       | 14           | 14           | 45                    | 2.5          |
</br>
<i>Note: Tags should be seperated by comma. All units are the default units indicated on the template file.</i>
<li>Select your Mathcad template file for each mounting locaiton. I have provided one to help you get started (01_LPCH ERCP_Anchorage_Template.mcdx).</li>
<li>If you want to save details about the report to a database, then click "Save to database?".</li>
<ul>
    <li>The "database" is a .csv file containting all the calculations you have performed with the automation software. This helps with organiziation and future reference.</li>
    <li>Choose the database that you want to make an entry into. If you choose an already existing database, your new reports will be appended. You can leave this field blank, and the software will automatically generate a database file saved to the same folder as the generated reports. </li>
</ul>
<li>Click the Previous or Next buttons to scroll the equipment listed in your excel file. </li>
<li>Click the "Preview Calculation Outputs" button to preview the output values. 
<li>Click the Generate button and provide a file name to generate a report for the equipment. You do not need to provide a filename if you are generating a report for all equipment entries.</li>
<li>The application is processing your request once you click a buttion. A confirmation popup will appear when the processing is complete. Please be patient - the Mathcad API is a little slow.</li>
</ul>
</br>
<b>Note: all generated reports are saved in the folder called "mathcad_automation_output".</b>


<h3>Using your own files:</h3>
<ul>
<li>To use your custom template, just choose it using the graphical user interface.</li>
<li>If you decide to create your own custom template, then ensure that the inputs and outputs follow the format of the template provided.</li>
</ul>