-- api queries

use covid19;

Select state, count(fips), count(cases),count( deaths) 
from covid_us_states
group by state;

Select state, count(fips), count(cases),count( deaths) 
from covid_live_us_states
group by state;

select * 
from covid_us_counties;

Select county,count(fips), count(cases),count( deaths) 
from covid_us_counties
group by county;

Select county, count(fips), count(cases),count( deaths) 
from covid_live_us_counties
group by county;

Select cases, deaths 
from covid_us;

select * 
from covid_live_us;

Select cases, deaths 
from covid_live_us;

Select county, count(fips), count(cases),count( deaths) 
from covid_us_counties  where state = 'california' group by county;

select * from us_zip_code where city = 'atlanta';

SELECT * FROM covid19.Hospital_List where city = 'atlanta' and stat_id='GA';

Select * from covid19.new_facilites;




