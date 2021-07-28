data assignment2solution;
length name $30 jobtitles $50 dep $30 fullorpart $1 salorhour $6 typicalh 8 annuals$8. hourlyr $8.;
infile 'C:\Users\Julio\Documents\WPS Workspaces\Workspace1\one\Current_Employee_Names__Salaries__and_Position_Titles (2).csv' DSD MISSOVER FIRSTOBS=2;
input name$ jobtitles$ dep$ fullorpart$ salorhour$ typicalh annuals hourlyr;
annualsnum= input(annuals,comma9.);
hourlyrnum= input(hourlyr,comma9.);
drop annuals hourlyr;
salorhourly=coalesce(annualsnum,hourlyrnum);
*if hourlyrnum=>50; *I did it like this first and then saw the solutions video and corrected it;
run;

proc print data=assignment2solution
(where=(hourlyrnum=>50));
var name hourlyrnum;
format hourlyrnum dollar24.2; *Gave the dollar format to the variable;
run;

proc contents data=assignment2solution;
run;

*repaso: input variable converts text to numeric, using comma9. as informat counts 9 characters, you can put any amount of it;
*coalesce returns the first NOT empty value; 
