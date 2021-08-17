**About**

This program is designed to help automate the heavy lifting of data
entry into Mathcad for the equipment anchorage process. It helps you
view and modify values taken from an excel spreadsheet before generating
a Mathcad report.

Please note that this is only compatible with Mathcad Prime 5.0 and
above.

[Tutorial Video](https://youtu.be/aOWT9xCHb2I)

**Installation**

1.  Go to the releases tab on this GitHub page, find the latest
    distribution and download it. Download the template files provided
    to help you get started.

2.  Double click the application executable to launch the application.

**Use**

1.  Select the excel file from the templates provided containing the
    equipment and the input data. The excel sheet should have the
    following key headers:

  ---------------------------------------------------------------------------------------
  eqpt_name     mounting_location   project_number   eqpt_number   tags       eqpt_tags
  ------------- ------------------- ---------------- ------------- ---------- -----------
  Anesthesia    Wall, Floor         1111             1234          Medical    Foo, Bar
  machine                                                                     

  Warming       Floor               1111             1234          Medical    Foo
  Cabinet                                                                     

  Surgical      Wall                1111             1234          Medical    Bar
  Scrub Sink                                                                  

  Retractable   Ceiling             1111             1234          Medical    Foo, Bar
  Ceiling                                                                     
  Column                                                                      
  ---------------------------------------------------------------------------------------

**Note**: Tags should be separated by comma. If you decide to include
units, put parentheses around the unit and do not include any spaces in
the header. There must be two sheets - \*values\* or \*Calculations\*
for holding input values and \*preview_images\* for displaying images
per mounting location. Look at the provided excel template for
reference.

2.  Select your Mathcad template file for each mounting location. I have
    provided a single file that works for each location to help you get
    started. It is located on the same page as the latest distribution.
    If the template you chose does not work, make sure that it is
    compatible with your current Mathcad distribution.

3.  You can always go back to the file selection screen by clicking
    \*File-\>Change Input Files\* from the main screen. You can reload
    the information from the excel spreadsheet by clicking
    \*Edit-\>Revert Inputs\*.

4.  If you want to save details about the report to the database, then
    click \*Save to Database\* in the Change Input Files window. See the
    section Database for more information.

5.  Click the \*Previous\* or \*Next\* buttons to scroll the equipment
    listed in your excel file.

6.  Click the \*Preview Calculation Outputs\* button to preview the
    output values.

7.  Click the \*Generate Report\* button and provide a file name to
    generate a report for the equipment. You do not need to provide a
    filename if you are generating a report for all equipment entries.

8.  The application is processing your request once you click \*Generate
    Report\* or \*Generate Report For All\*. A confirmation popup will
    appear when the processing is complete. Be patient - the Mathcad API
    is not very fast and unfortunately there is no way to speed it up.
    You can do whatever tasks you like in the background.

9.  All reports are saved to the \*mathcad_automation_output\* folder
    generated in the same folder you opened the application from.

**Database**

1.  The \"database\" is a .csv file containing all the calculations you
    have performed with the automation software. This helps with
    organization and future reference.

2.  Choose the database using the \*File-\>Select Input Files\*. All new
    generated reports will appear in the specified file. If you choose
    an already existing database, your new reports will automatically be
    appended. You can leave this field blank: a database file will
    automatically be generated in the \*mathcad_automation_output\*
    folder, and the new reports will be appended.

3.  You can view the database file by clicking \*View Database File\*.
    This will either load the database file specified in the inputs or
    load the default database file generated when you clicked \*Generate
    Report\* or \*Generate Reports for All\*.

**Database Viewer (View Database File)**

1.  You can view the database file by clicking \*View Database File\*.
    You can always load a different database file for viewing by
    clicking \*View Database File\* and then \*File-\>Select Database
    File\*.

2.  You can filter the data displayed by choosing the header you want to
    filter and then typing in a filter query.

3.  Inclusive filter search will filter for partial completions, while
    and exclusive search will only return exact matches to the search
    query.

4.  Sort the data by header and increasing or decreasing. If the column
    contains words, it will sort alphabetically, and if it is numeric,
    it will sort numerically.

5.  You can export the data that is being viewed by clicking
    \*Export-\>Export Visible Data to Clipboard\*. This will copy the
    data that is filtered and sorted to the clipboard. You can easily
    paste this data into excel.

**Bugs/Debugger**

1.  Each distribution comes with a debug log in the \*Help-\>Bugs\* tab.

2.  The debugger is a log of all the actions that you, the user, have
    performed. If you ever encounter a bug, open the tab, and click the
    share button. You can share the log with the developer, who will be
    able to better assess the problem with this information.

**Important Information**

1.  Make sure to select the appropriate Mathcad template file from the
    templates provided. If you are using Mathcad Prime 5.0, you must use
    a file compatible with that version. Mathcad Prime is backward
    compatible; however, older files can be run on more modern versions
    of the software.

2.  If you would like to change the output folder (where all reports and
    the database file are saved) then specify it in \*File-\>Select
    Output Folder\*.

3.  All Generated reports are saved by default to a folder called
    \*mathcad_automation_output\*. This folder is created (if it
    doesn\'t exist already) in the same directory as the application. If
    you specify an output folder, it will be used instead of
    \*mathcad_automation_output\*.

4.  Customizing the App:

    a.  If you decide to you want to include your own inputs and
        outputs, make sure to label your inputs \*\<my_label>\_input\*.
        For example, \*alpha_input\* would work, but \*alpha_something\*
        would not.

    b.  To use your own custom Mathcad template, choose it using the
        \*Change Input Files\* button. Ensure the format follows the
        example Mathcad template provided.

    c.  To use your own custom excel file, choose it using
        \*File-\>Change Input Files\* or the shortcut \*Ctrl-i\*. Your
        custom file must follow the formatting rules explicitly defined
        in the example excel document.

    d.  To save the inputs from the application back to the excel file,
        click \*File-\>Save Inputs To Excel\* or the shortcut
        \*Ctrl-s\*.
