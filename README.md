
# Table of Contents

1.  [About](#org367d1c1)
2.  [Installation](#org0f202ac)
3.  [Use](#org982c1ea)
4.  [Database](#org416366d)
5.  [Important Information](#org6484698)



<a id="org367d1c1"></a>

# About

This program is designed to help automate the heavy lifting of data entry into Mathcad for the equipment anchorage process. It helps you view and modify values taken from an excel spreadsheet before generating a mathcad report.

Please note that this is only compatible with Mathcad Prime 5.0 and above.
[Tutorial Video](https://youtu.be/WerhVoz60nI)


<a id="org0f202ac"></a>

# Installation

1.  Go to the releases tab on this github page, find the latest distribution and download it. Download the template files provided to help you get started.
2.  Double click the application executable to launch the application.


<a id="org982c1ea"></a>

# Use

Select the excel file from the templates provided containing the equipment and the input data. The excel sheet should have the following key headers:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">eqpt_name</th>
<th scope="col" class="org-left">mounting_location</th>
<th scope="col" class="org-right">project_number</th>
<th scope="col" class="org-right">eqpt_number</th>
<th scope="col" class="org-left">tags</th>
<th scope="col" class="org-left">eqpt_tags</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">Anesthesia machine</td>
<td class="org-left">Wall, Floor</td>
<td class="org-right">1111</td>
<td class="org-right">1234</td>
<td class="org-left">Medical</td>
<td class="org-left">Foo, Bar</td>
</tr>


<tr>
<td class="org-left">Warming Cabinet</td>
<td class="org-left">Floor</td>
<td class="org-right">1111</td>
<td class="org-right">1234</td>
<td class="org-left">Medical</td>
<td class="org-left">Foo</td>
</tr>


<tr>
<td class="org-left">Surgical Scrub Sink</td>
<td class="org-left">Wall</td>
<td class="org-right">1111</td>
<td class="org-right">1234</td>
<td class="org-left">Medical</td>
<td class="org-left">Bar</td>
</tr>


<tr>
<td class="org-left">Retractable Ceiling Column</td>
<td class="org-left">Ceiling</td>
<td class="org-right">1111</td>
<td class="org-right">1234</td>
<td class="org-left">Medical</td>
<td class="org-left">Foo, Bar</td>
</tr>
</tbody>
</table>

Note: Tags should be separated by comma. If you decide to include units, put parentheses around the unit and do not include any spaces in the header. There must be two sheets - **values** or **Calculations** and **preview\_images**. Take a look at the provided excel template for reference.

1.  Select your Mathcad template file for each mounting location. I have provided a single file that works for each location to help you get started. It is located on the same page as the latest distribution. If the template you chose does not work, make sure that it is compatible with your current Mathcad distribution.
2.  You can always go back to the file selection screen by clicking **File->Change Input Files** from the main screen. You can reload the information from the excel spreadsheet by clicking **Edit->Revert Inputs**.
3.  If you want to save details about the report to the database, then click **Save to Database** in the Change Input Files window. See the section `Database` for more information.
4.  Click the **Previous** or **Next** buttons to scroll the equipment listed in your excel file.
5.  Click the **Preview Calculation Outputs** button to preview the output values.
6.  Click the **Generate Report** button and provide a file name to generate a report for the equipment. You do not need to provide a filename if you are generating a report for all equipment entries.
7.  The application is processing your request once you click **Generate Report** or **Generate Report For All**. A confirmation popup will appear when the processing is complete. Be patient - the Mathcad API is not very fast and unfortunately there is no way to speed it up. You can do whatever tasks you like in the background.


<a id="org416366d"></a>

# Database

1.  The "database" is a .csv file containing all the calculations you have performed with the automation software. This helps with organization and future reference.
2.  Choose the database that you want your generated reports to be appended to. If you choose an already existing database, your new reports will automatically be appended. You can leave this field blank: a database file will automatically be generated in the **mathcad\_automation\_output** folder, and the new reports will be appended.


<a id="org6484698"></a>

# Important Information

1.  Make sure to select the appropriate Mathcad template file from the teplates provided. If you are using Mathcad Prime 5.0, you must use a file compatible with that version. Mathcad Prime is backward compatible, however, older files can be run on more modern versions of the software.
2.  All Generated reports are saved to a folder called **mathcad\_automation\_output**. This folder is created (if it doesn't exist already) in the same directory as the application.
3.  Customizing the App:
    -   If you decide to you want to include your own inputs and outputs, make sure to label your inputs **<my\_label>\_input**. For example, **alpha\_input** would work, but **alpha\_something** would not.
    -   To use your own custom Mathcad template, choose it using the **Change Input Files** button. Ensure the format follows the example Mathcad template provided.
    -   To use your own custom excel file, choose it using **File->Change Input Files** or the shortcut **Ctrl-i**. Your custom file must follow the formatting rules explicitly defined in the example excel document.
    -   To save the inputs from the application back to the excel file, click **File->Save Inputs To Excel** or the shortcut **Ctrl-s**.

