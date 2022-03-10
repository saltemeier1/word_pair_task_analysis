WPAnalysis.py takes raw data from the Word Pair Tasks and creates a csv summarizing the statistics. 
The output includes: the Patient ID, Pre Sleep Accuracy, Post Sleep Accuracy, # of Practice Rounds, and Practice Accuracy.

RUNNING WPAnalysis.py:::::::::::::::::::::::::::::::::::::::::

Open file explorer and navigate to J:\tasks\SPARCS word pairs\WPTScript
This folder holds the script, a folder for the output of the script, and a folder in which all reports that you 
want analyzed should go into.
So, from J:\tasks\SPARCS word pairs\results you should grab any raw data that you want analyzed and copy and paste
it into J:\tasks\SPARCS word pairs\WPTScript\Reports
Once this is done, you should open a command prompt and type

j:

into the command window, and then press enter. Next, type

cd tasks\SPARCS word pairs\WPTScript

and press enter. Then, from here, you can then run

python WPAnalysis.py

Now, you can open back up a file explorer and navigate to J:\tasks\SPARCS word pairs\WPTScript\SummaryStatistics
and the summary of what you just ran will be named month_day_WPT_Summary_HH_MM. For example, if I ran the script on 
October 14th at 11:49, the name of the summary would be 10_14_WPT_Summary_11_49.