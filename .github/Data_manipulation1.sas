data national;
length Country $50 ISO $3 MPI_URBAN 8 Headcount_Ratio_Urban 8 Intensity_of_Deprivation_Urban 8 MPI_Rural 8 Headcount_Ratio_Rural 8 Intensity_of_Deprivation_Rural 8; 
infile 'C:\Users\Julio\OneDrive\Escritorio\SAS\course 1\MPI_national (1).csv' DSD MISSOVER FIRSTOBS=2;
input ISO$ Country$ MPI_URBAN Headcount_Ratio_Urban Intensity_of_Deprivation_Urban MPI_Rural Headcount_Ratio_Rural Intensity_of_Deprivation_Rural;
MPI_Dif = MPI_URBAN - MPI_Rural;
if ISO='NIG' then
substr(ISO,1,3) = 'NGA';
together = catx(',', Country,ISO);
run;

data national2;
set national;
if Intensity_of_Deprivation_Rural=> 40.0;
run;


*LENGTH with numeric variables that have decimals keep it to default: 8 bytes;
*we put the LENGTH statement before the INFILE so that we can move the variables columns; *length control the order of variables;