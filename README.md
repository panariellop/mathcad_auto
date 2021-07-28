About
=====

This program is designed to help automate the heavy lifting of data
entry into Mathcad for the equipment anchorage process. It helps you
view and modify values taken from an excel spreadsheet before generating
a mathcad report.

Please note that this is only compatible with Mathcad Prime 3.1 and
above. [Tutorial Video](https://youtu.be/WerhVoz60nI)

Installation
============

1.  Go to the releases tab on this github page, find the latest
    distribution and download it. Download the template files provided
    to get started.
2.  Double click the **application_v1.exe** file to launch the
    application.

Use
===

Select the excel file from the templates provided containing the
equipment and the input data. The excel sheet should have the following
key headers:
<table>
<tr>
<th>eqpt_name</th><th>mounting_location</th><th>project_number</th><th>tags</th>
</tr>
<tr>
  <td>Anesthesia machine</td><td>Wall, Floor</td><td>1111</td><td>Medical, ICU, something</td>
</tr>
<tr>
  <td>Warming Cabinet</td><td>Floor</td><td>1111</td><td>Medical</td>
</tr>
<tr>
  <td>Surgical Scrub Sink</td><td>Wall</td><td>1111</td><td>Medical</td>
</tr>
<tr>
  <td>Retractable Ceiling Column</td><td>Ceiling</td><td>1111</td><td>Medical</td>
</tr>
</table

Note: Tags should be separated by comma. If you decide to include units,
put parentheses around the unit and do not include any spaces in the
header. There must be two sheets - **values** and **preview_images**. Take a
look at **example_sheet.xlsx** for reference.

1.  Select your Mathcad template file for each mounting location. I have
    provided a single file that works for each location to help you get
    started. It is located on the same page as the latest distribution.
2.  You can always go back to the file selection screen by clicking
    **Change Input Files**. You can reload the information from the
    excel spreadsheet by clicking **Refresh**.
3.  If you want to save details about the report to the database, then
    click **Save to Database**. See the section `Database` for more
    information.
4.  Click the Previous or Next buttons to scroll the equipment listed in
    your excel file.
5.  Click the \"Preview Calculation Outputs\" button to preview the
    output values.
6.  Click the Generate button and provide a file name to generate a
    report for the equipment. You do not need to provide a filename if
    you are generating a report for all equipment entries.
7.  The application is processing your request once you click **Generate
    Report** or **Generate Report For All**. A confirmation popup will
    appear when the processing is complete.

Database
========

1.  The \"database\" is a .csv file containing all the calculations you
    have performed with the automation software. This helps with
    organization and future reference.
2.  Choose the database that you want to make an entry into. If you
    choose an already existing database, your new reports will be
    appended. You can leave this field blank, and the software will
    automatically generate a database file saved to the same folder as
    the generated reports.

Important Information
=====================

1.  Make sure to select the appropriate Mathcad template file from the
    teplates provided. If you are using Mathcad Prime 5.0, you must use
    a file compatible with that version. Mathcad Prime is backward
    compatible, however, and older files can be run on more modern
    versions of the software.
2.  All Generated reports are saved to a folder called
    **mathcad_automation_output**. This folder is created (if it
    doesn\'t exist already) in the same directory as the application.
3.  Customizing the App: a. If you decide to you want to include your
    own inputs and outputs, make sure to label your inputs
    **\<my_label\>\_input**. For example, **alpha_input** would work,
    but **alpha_something** would not. b. To use your own custom Mathcad
    template, choose it using the **Change Input Files** button. Ensure
    the format follows the example Mathcad template provided. c. To use
    your own custom excel file, choose it using the **Change Input
    Files** button. Your custom file must follow the formatting rules
    explicitly defined in the example excel document.
